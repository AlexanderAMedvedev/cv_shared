# [0.4.1]
* extended API for `put_on_frame`

# [0.4.0]
* added `put_on_frame.py`

# [0.3.0]
* added export in `__init__.py`

# [0.2.0]
* added `append_value_to_file()` 

# [0.1.0]
* added `cv_shared.video_source.load_video_source(config_path, default=0)` — reads
  `video_source` from a JSON config. On any failure (missing file, malformed
  JSON, missing key) prints the reason and returns `default`.
* added `cv_shared.video_source.open_video_capture(source)` — opens a
  `cv2.VideoCapture`. For `rtsp://` sources it forces TCP transport: lost UDP
  packets produce corrupted frames, and those frames are used for subpixel
  chessboard corner detection.
* added `pytest` suite covering both functions (6 tests, no camera required).

# References
* [Keep a Changelog](https://keepachangelog.com/en/1.1.0/)
* [Semantic Versioning](https://semver.org/)
