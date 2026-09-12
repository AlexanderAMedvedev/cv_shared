import json
import os

import cv2
import pytest

from cv_shared.video_source import load_video_source, open_video_capture

RTSP_OPTIONS_ENV = 'OPENCV_FFMPEG_CAPTURE_OPTIONS'


class FakeCapture:
    """Заглушка cv2.VideoCapture: поток «открылся», сеть не нужна."""

    def isOpened(self):
        return True


def write_config(tmp_path, payload):
    config_path = tmp_path / 'camera_config.json'
    config_path.write_text(json.dumps(payload))
    return config_path


def test_reads_source_from_config(tmp_path):
    config_path = write_config(tmp_path, {'video_source': 'rtsp://cam/stream1'})
    assert load_video_source(config_path) == 'rtsp://cam/stream1'


def test_missing_file_returns_default(tmp_path):
    assert load_video_source(tmp_path / 'absent.json', default=0) == 0


def test_malformed_json_returns_default(tmp_path):
    config_path = tmp_path / 'camera_config.json'
    config_path.write_text('{ не json')
    assert load_video_source(config_path, default=0) == 0


def test_missing_key_returns_default(tmp_path):
    config_path = write_config(tmp_path, {'другой_ключ': 1})
    assert load_video_source(config_path, default=0) == 0


def test_unopenable_source_raises(tmp_path):
    with pytest.raises(RuntimeError):
        open_video_capture(str(tmp_path / 'absent.mp4'))


def test_rtsp_source_forces_tcp_transport(monkeypatch):
    # setdefault ничего не сделает, если переменная уже задана снаружи —
    # без delenv тест прошёл бы по неверной причине
    monkeypatch.delenv(RTSP_OPTIONS_ENV, raising=False)
    monkeypatch.setattr(cv2, 'VideoCapture', lambda source: FakeCapture())

    open_video_capture('rtsp://cam/stream1')

    assert os.environ[RTSP_OPTIONS_ENV] == 'rtsp_transport;tcp'
