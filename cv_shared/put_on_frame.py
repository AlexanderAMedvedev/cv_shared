import cv2


def put_on_frame(
    text: str,
    text_color: tuple[int, int, int],
    display: cv2.Mat,
    position: tuple[int, int],
    bottom_left_origin: bool = False,
) -> cv2.Mat:
    text_font = cv2.FONT_HERSHEY_SIMPLEX
    text_font_thickness = 1
    text_font_scale = 1
    return cv2.putText(
        display,
        text,
        position,
        text_font,
        text_font_scale,
        text_color,
        text_font_thickness,
        cv2.LINE_4,
        bottomLeftOrigin=bottom_left_origin,
    )
