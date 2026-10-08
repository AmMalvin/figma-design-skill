# Media components

Owns content controls: image/viewer, audio/video, gallery, file preview and upload. They share asset styling but have distinct behavior/APIs.

Preserve aspect/subject, reserve dimensions, specify missing/failed/unsupported media and meaningful metadata. Do not autoplay disruptive media or hide essential content in a carousel.

Playback defines play/pause/seek/speed where applicable, visible controls, keyboard names/state, captions/transcripts and appropriate alternatives to essential visual information. Verify actual media access; captions cannot be promised merely because a design has a toggle.

Viewers define zoom/reset, exit, focus and context restoration. Touch gestures need alternatives. Carousel navigation remains visible and pause/control behavior explicit.

Uploads state types/limits before selection; support native/browse entry alongside drag, per-file progress/cancel/retry, partial failure and replace/remove. Do not conflate upload completion with processing/acceptance.

Licensing/asset choices live in [Imagery & Illustration](../02-Visual-System/Imagery%20%26%20Illustration.md). Workflow uploads live in [Form Workflows](../06-Patterns/Form%20Workflows.md). Verify long filenames, accessibility, fallback, slow network and narrow layout.
