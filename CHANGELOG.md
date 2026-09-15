# CHANGELOG

Format based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
versioning follows [Semantic Versioning](https://semver.org/).

## [0.2.0]
### Added
* `append_value_to_file()` 

## [0.1.0]
### Added
* `cv_shared.video_source.load_video_source(config_path, default=0)` — reads
  `video_source` from a JSON config. On any failure (missing file, malformed
  JSON, missing key) prints the reason and returns `default`.
* `cv_shared.video_source.open_video_capture(source)` — opens a
  `cv2.VideoCapture`. For `rtsp://` sources it forces TCP transport: lost UDP
  packets produce corrupted frames, and those frames are used for subpixel
  chessboard corner detection.
* `pytest` suite covering both functions (6 tests, no camera required).
