"""Read-only integrity checks; these do not establish interface quality."""
from __future__ import annotations
import argparse
from collections import deque
from datetime import date
import hashlib
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
IGNORED = {".git", "__pycache__", ".pytest_cache"}
LINK = re.compile(r'!?\[[^\]\n]*\]\((<[^>]+>|[^)\n]+)\)')
CATEGORIES = {"standards", "product-benchmarks", "visual-inspiration",
              "interaction-patterns", "mobile-patterns", "web-patterns",
              "dashboard-patterns", "motion-patterns", "design-system-references",
              "reference-evaluation"}


def documents(root):
    return sorted(p for p in root.rglob("*.md")
                  if not any(part in IGNORED for part in p.relative_to(root).parts))


def prose(text):
    """Exclude code fences; links inside examples are not live document links."""
    lines, marker = [], None
    for line in text.splitlines():
        fence = re.match(r"^\s*(`{3,}|~{3,})", line)
        if fence:
            char = fence.group(1)[0]
            marker = None if marker == char else char if marker is None else marker
            continue
        if marker is None:
            lines.append(line)
    return "\n".join(lines)


def local_targets(path, text):
    for match in LINK.finditer(prose(text)):
        value = match.group(1).strip()
        if value.startswith("<"):
            value = value[1:-1]
        else:
            value = re.sub(r'\s+["\x27].*$', "", value)
        parts = urlsplit(value)
        if parts.scheme or parts.netloc or not parts.path:
            continue
        yield (path.parent / unquote(parts.path)).resolve(), value
    meta = re.match(r"^---\r?\n(.*?)\r?\n---", text, re.S)
    if meta:
        for line in meta.group(1).splitlines():
            value = re.match(r"^\s+-\s+(.+\.md)\s*$", line)
            if value:
                yield (path.parent / value.group(1).strip()).resolve(), value.group(1)


def check_links(root):
    errors, edges, graph = [], 0, {}
    for path in documents(root):
        text = path.read_text(encoding="utf-8")
        if not text.strip():
            errors.append(f"Empty instruction/document: {path.relative_to(root)}")
        graph[path.resolve()] = []
        for target, value in local_targets(path, text):
            edges += 1
            if not target.is_relative_to(root.resolve()):
                errors.append(f"Link leaves repository: {path.relative_to(root)} -> {value}")
            elif not target.exists():
                errors.append(f"Broken link: {path.relative_to(root)} -> {value}")
            else:
                graph[path.resolve()].append(target)
    return errors, edges, graph


def schema_errors(value, schema, where="$"):
    """The checked schema uses this explicitly supported JSON Schema subset."""
    errors = []
    types = {"array": list, "object": dict, "string": str, "null": type(None)}
    expected = schema.get("type")
    if expected:
        names = expected if isinstance(expected, list) else [expected]
        if not any(isinstance(value, types[name]) for name in names):
            return [f"{where}: expected {names}"]
    if "enum" in schema and value not in schema["enum"]:
        errors.append(f"{where}: invalid enum value")
    if "const" in schema and value != schema["const"]:
        errors.append(f"{where}: does not match constant")
    if isinstance(value, str):
        if len(value.strip()) < schema.get("minLength", 0):
            errors.append(f"{where}: empty required string")
        if schema.get("format") == "date":
            try:
                if date.fromisoformat(value).isoformat() != value:
                    raise ValueError()
            except ValueError:
                errors.append(f"{where}: invalid ISO date")
    if isinstance(value, list):
        if len(value) < schema.get("minItems", 0) or len(value) > schema.get("maxItems", float("inf")):
            errors.append(f"{where}: invalid array length")
        if schema.get("uniqueItems") and len({json.dumps(v, sort_keys=True) for v in value}) != len(value):
            errors.append(f"{where}: duplicate items")
        for i, item in enumerate(value):
            errors.extend(schema_errors(item, schema.get("items", {}), f"{where}[{i}]"))
    if isinstance(value, dict):
        for key in schema.get("required", []):
            if key not in value:
                errors.append(f"{where}: missing {key}")
        props = schema.get("properties", {})
        if schema.get("additionalProperties") is False:
            for key in value.keys() - props.keys():
                errors.append(f"{where}: unknown field {key}")
        for key, item in value.items():
            if key in props:
                errors.extend(schema_errors(item, props[key], f"{where}.{key}"))
    if "anyOf" in schema and all(schema_errors(value, option, where) for option in schema["anyOf"]):
        errors.append(f"{where}: no anyOf branch matches")
    for option in schema.get("allOf", []):
        errors.extend(schema_errors(value, option, where))
    if "if" in schema and not schema_errors(value, schema["if"], where):
        errors.extend(schema_errors(value, schema.get("then", {}), where))
    return errors


def check_references(root):
    schema = json.loads((root / "references/catalog.schema.json").read_text(encoding="utf-8"))
    errors, seen, coverage, count = [], set(), set(), 0
    for filename in ("catalog.json", "intake.json"):
        values = json.loads((root / "references" / filename).read_text(encoding="utf-8"))
        errors.extend(schema_errors(values, schema, filename))
        if not isinstance(values, list):
            continue
        for record in values:
            if not isinstance(record, dict):
                continue
            count += 1
            identity = record.get("id")
            if identity in seen:
                errors.append(f"Duplicate reference ID: {identity}")
            seen.add(identity)
            if filename == "catalog.json":
                coverage.update(record.get("categories", []))
            url = record.get("url", "")
            if url and (urlsplit(url).scheme not in {"http", "https"} or not urlsplit(url).netloc):
                errors.append(f"Invalid reference URL: {identity}")
            for key in ("reviewed_date", "checked_date"):
                val = record.get(key)
                if val and val > date.today().isoformat():
                    errors.append(f"Future reference date: {identity}.{key}")
    if CATEGORIES - coverage:
        errors.append(f"Missing reference categories: {sorted(CATEGORIES - coverage)}")
    return errors, count


def check_preservation(root):
    baseline = json.loads((root / "09-QA/audit-baseline.json").read_text(encoding="utf-8"))
    errors = []
    original = {f["path"]: f for f in baseline["files"]}
    for filename in original:
        if not (root / filename).is_file():
            errors.append(f"Original file missing: {filename}")
    for filename in baseline["original_user_edits"]:
        path = root / filename
        if path.exists():
            content = path.read_bytes()
            raw_matches = hashlib.sha256(content).hexdigest() == original[filename]["sha256"]
            # Git may convert CRLF/LF during checkout; every other byte is protected.
            expected_lf = original[filename].get("sha256_lf")
            lf_matches = expected_lf is not None and hashlib.sha256(
                content.replace(b"\r\n", b"\n")
            ).hexdigest() == expected_lf
            if not raw_matches and not lf_matches:
                errors.append(f"Pre-existing user edit changed: {filename}")
    return errors, len(baseline["original_user_edits"])


def reachable(start, graph):
    found, queue = set(), deque([start])
    while queue:
        path = queue.popleft()
        if path in found:
            continue
        found.add(path)
        queue.extend(graph.get(path, []))
    return found


def check_scenarios(root, graph):
    data = json.loads((root / "09-QA/evaluations/scenarios.json").read_text(encoding="utf-8"))
    scenarios = data["scenarios"]
    errors, ids = [], set()
    routes = reachable((root / "SKILL.md").resolve(), graph)
    for scenario in scenarios:
        sid = scenario["id"]
        if sid in ids:
            errors.append(f"Duplicate scenario: {sid}")
        ids.add(sid)
        for key in ("prompt", "platform", "deliverable"):
            if not scenario.get(key, "").strip():
                errors.append(f"Scenario {sid} missing {key}")
        if not scenario["fixture"]["existing_system"] or not scenario["fixture"]["constraints"]:
            errors.append(f"Scenario {sid} missing system/stress fixture")
        if not scenario["evaluator"]["criteria"] or not scenario["evaluator"]["anti_patterns"]:
            errors.append(f"Scenario {sid} missing evaluator contract")
        for name in scenario["required_routes"]:
            path = (root / name).resolve()
            if not path.is_relative_to(root.resolve()) or path not in routes:
                errors.append(f"Scenario {sid} route not reachable from skill: {name}")
    return errors, len(scenarios)


def validate(root):
    errors, edges, graph = check_links(root)
    summary = {"documents": len(documents(root)), "local_edges": edges}
    for check, key in ((check_references, "reference_records"), (check_preservation, "preserved_user_files")):
        try:
            findings, count = check(root)
            errors.extend(findings)
            summary[key] = count
        except (OSError, ValueError, KeyError, TypeError) as exc:
            errors.append(f"{key}: {exc}")
    try:
        findings, count = check_scenarios(root, graph)
        errors.extend(findings)
        summary["scenarios"] = count
    except (OSError, ValueError, KeyError, TypeError) as exc:
        errors.append(f"scenarios: {exc}")
    summary["errors"] = errors
    return summary


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()
    result = validate(args.root.resolve())
    print(json.dumps(result, indent=2))
    return 1 if result["errors"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
