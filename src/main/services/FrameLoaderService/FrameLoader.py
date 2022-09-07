from typing_extensions import Self
import cv2 

class FrameLoaderOpenCV:
    def __init__(self, source) -> None:
        self.video = cv2.VideoCapture(source)

    def __enter__(self) -> Self:
        print("Entered FrameLoaderOpenCV")
        return self.video

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        self.video.release()
        cv2.destroyAllWindows()
        print("Exited FrameLoaderOpenCV")
        return True