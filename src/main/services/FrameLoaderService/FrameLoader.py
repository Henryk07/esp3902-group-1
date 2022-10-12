from typing_extensions import Self
import cv2

GSTREAMER_SOURCE = "nvarguscamerasrc sensor_id=0 ! video/x-raw(memory:NVMM), width=1920, height=1080, framerate=30/1 ! nvvidconv flip-method=2 ! video/x-raw, width=960, height=540, format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink"

class FrameLoaderOpenCV:
    def __init__(self, source = GSTREAMER_SOURCE, width: int = None, height: int = None) -> None:
        self.video = cv2.VideoCapture(source, cv2.CAP_GSTREAMER)
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

