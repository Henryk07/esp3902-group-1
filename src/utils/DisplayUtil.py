import cv2

class DisplayUtil:
    def __init__(self) -> None:
        pass

    def drawRectangleWithText(
        frame, 
        xMin: int,
        yMin: int,
        xMax: int,
        yMax: int,
        color: tuple, 
        thickness: int = 2, 
        text: str = "Object",
        font: str = cv2.FONT_HERSHEY_SIMPLEX
    ) -> None:

        cv2.rectangle(frame, (xMin, yMin), (xMax, yMax), color, thickness)
        textSize = cv2.getTextSize(text, font, 1, 2)[0]
        cv2.putText(frame, text, ((xMin + xMax) // 2 - textSize[0] // 2, yMin - 20), font, 1, color, 2)

