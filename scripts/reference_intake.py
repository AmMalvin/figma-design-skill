"""Local metadata inbox; never fetches, executes or publishes a submitted source."""
import argparse
import json
from pathlib import Path
import tempfile
from urllib.parse import urlsplit
import uuid

from validate_repository import schema_errors

ROOT = Path(__file__).resolve().parents[1]


def pending_record(source, question, platform, kind):
    remote = urlsplit(source).scheme in {"https", "http"} and bool(urlsplit(source).netloc)
    if kind in {"url", "figma", "website", "article"} and not remote:
        raise ValueError("This source kind requires an http or https URL.")
    if not question.strip():
        raise ValueError("A study question is required.")
    return {
        "id": "intake-" + uuid.uuid4().hex[:12], "source_name": source,
        "url" if remote else "local_source": source,
        "kind": kind, "question": question, "product_studio": "Unidentified; inspect source",
        "platform": [platform], "screen_flow": "Not inspected; see study question",
        "pattern_category": "To classify after inspection", "categories": ["reference-evaluation"],
        "authority_class": "project-evidence", "why_reference_matters": question,
        "qualities_to_study": [question], "interaction_principles": [], "visual_principles": [],
        "ux_principles": [], "do_not_copy": ["No design inference before inspection"],
        "adaptation_to_current_system": "Inspect project system before extracting useful principles.",
        "reviewed_date": None, "checked_date": None, "status": "pending",
        "evidence_limits": "Metadata only; source content and access have not been inspected."
    }


def add(root, record):
    inbox = root / "references/intake.json"
    records = json.loads(inbox.read_text(encoding="utf-8"))
    if not isinstance(records, list):
        raise ValueError("Inbox must be a JSON array.")
    records.append(record)
    schema = json.loads((root / "references/catalog.schema.json").read_text(encoding="utf-8"))
    errors = schema_errors(records, schema)
    if errors:
        raise ValueError("\n".join(errors))
    # Atomic replacement protects the queue from a partial write. One writer at a time.
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=inbox.parent, delete=False,
                                     suffix=".tmp") as handle:
        json.dump(records, handle, indent=2, ensure_ascii=False)
        handle.write("\n")
        temporary = Path(handle.name)
    try:
        temporary.replace(inbox)
    finally:
        temporary.unlink(missing_ok=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    actions = parser.add_subparsers(dest="action", required=True)
    actions.add_parser("list")
    create = actions.add_parser("add")
    create.add_argument("--source", required=True)
    create.add_argument("--question", required=True)
    create.add_argument("--platform", default="unspecified")
    create.add_argument("--kind", choices=["url", "figma", "screenshot", "video", "article", "internal", "website"], default="url")
    args = parser.parse_args()
    if args.action == "list":
        print((ROOT / "references/intake.json").read_text(encoding="utf-8"))
    else:
        try:
            record = pending_record(args.source, args.question, args.platform, args.kind)
            add(ROOT, record)
        except (ValueError, OSError) as exc:
            parser.error(str(exc))
        print(f"Queued {record['id']}; content not inspected.")


if __name__ == "__main__":
    main()
