# cv_shared

Shared utilities for computer vision projects.

## Install

```bash
pip install git+https://github.com/AlexanderAMedvedev/cv_shared.git@v0.1.0
```

Pin a tag rather than tracking `main`: pip compares version numbers, not
commits, so an unpinned install gives you whatever `main` holds today.
`opencv-python` and `numpy` are installed automatically as dependencies.

## Usage

```python
from pathlib import Path

from cv_shared.video_source import load_video_source, open_video_capture

# Where the config lives is the caller's business, not the package's.
CONFIG_PATH = Path(__file__).resolve().parent.parent / 'camera_config/camera_config.json'
DEFAULT_VIDEO_SOURCE = 0

cap = open_video_capture(load_video_source(CONFIG_PATH, DEFAULT_VIDEO_SOURCE))
```

Config file format:

```json
{"video_source": "rtsp://user:pass@192.168.1.10:554/stream1"}
```

If the file is missing, malformed, or lacks the key, `load_video_source`
prints the reason and returns `default` — so a project falls back to the
built-in camera (index `0`) instead of crashing.

## Development

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e '.[dev]'
pytest
```
## Releasing

Consumers install by tag, and pip skips an upgrade when the version is
unchanged. So any push meant for other projects needs all three:

1. bump `version` in `pyproject.toml`
2. add a section to `CHANGELOG.md`
3. `git tag vX.Y.Z && git push --tags`

While the version stays `0.x`, the API is not stable and breaking changes go
in the minor position.
