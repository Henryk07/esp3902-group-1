from typing_extensions import Self
import cv2 

class FrameLoaderOpenCV:
    def __init__(self, source, width: int = None, height: int = None) -> None:
        self.video = cv2.VideoCapture(source)
        if width is not None and width <= self.video.get(cv2.CAP_PROP_FRAME_WIDTH):
            self.video.set(cv2.CAP_PROP_FRAME_WIDTH, width)

        if height is not None and height <= self.video.get(cv2.CAP_PROP_FRAME_HEIGHT):
            self.video.set(cv2.CAP_PROP_FRAME_HEIGHT, height)


    def __enter__(self) -> Self:
        print("Entered FrameLoaderOpenCV")
        print(f"Resolution: {int(self.video.get(cv2.CAP_PROP_FRAME_WIDTH))}x{int(self.video.get(cv2.CAP_PROP_FRAME_HEIGHT))}")
        return self.video

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        self.video.release()
        cv2.destroyAllWindows()
        print("Exited FrameLoaderOpenCV")
        return True