"""
Источник видео: чтение настроек и открытие потока.

Функции перенесены из camera_calibration/calibrate_camera.py. В отличие от
исходной версии, путь к конфигу передаёт вызывающая сторона — пакет ничего
не знает про раскладку каталогов конкретного проекта.
"""

import json
import os
from pathlib import Path

import cv2


def load_video_source(config_path: Path,
                      default: int | str = 0) -> int | str:
    try:
        with open(config_path) as f:
            return json.load(f)['video_source']
    except (OSError, ValueError, KeyError) as error:
        print(f'Конфиг {config_path} не прочитан ({error}), '
              f'используем источник по умолчанию: {default}')
        return default


def open_video_capture(source: int | str) -> cv2.VideoCapture:
    if isinstance(source, str) and source.startswith('rtsp://'):
        # У VideoCapture нет параметра для транспорта RTSP, ffmpeg читает опции
        # из этой переменной окружения в момент открытия потока. TCP вместо UDP:
        # при потере пакетов кадр приходит с артефактами, а по нему ищут углы
        # доски с субпиксельной точностью — битый кадр испортит калибровку.
        os.environ.setdefault('OPENCV_FFMPEG_CAPTURE_OPTIONS',
                              'rtsp_transport;tcp')

    cap = cv2.VideoCapture(source)
    if not cap.isOpened():
        raise RuntimeError('Не удалось открыть источник видео')
    return cap
