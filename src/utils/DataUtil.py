from math import ceil, floor
from time import perf_counter
import cv2

class DataUtil:
    def __init__(self) -> None:
        pass
    
    def getFrame(framePath):
        return cv2.imread(framePath)

    def cropFrame(frame, coordinates):
        coordinates["xmin"], coordinates["ymin"] = map(floor, (coordinates["xmin"], coordinates["ymin"]))
        coordinates["xmax"], coordinates["ymax"] = map(ceil, (coordinates["xmax"], coordinates["ymax"]))

        croppedFrame = frame[coordinates.get("ymin"): coordinates.get("ymax"), coordinates.get("xmin"): coordinates.get("xmax")]
        
        return croppedFrame

    def loadSavedFrame(filepath):
        return cv2.imread(filepath)

    def getNewFrameCv2(filepath = None):
        vid = cv2.VideoCapture(0)
        for i in range(3):
            _, frame = vid.read()
        vid.release()
        cv2.destroyAllWindows()

        if filepath is not None:
            cv2.imwrite(filepath, frame)

        return frame
    
    def getNewFramesCv2(numOfFrames) -> list:
        frames = list()

        vid = cv2.VideoCapture(0)
        for i in range(2): # Buffer
            vid.read()

        start = perf_counter()
        for i in range(numOfFrames):
            _, frame = vid.read()
            frames.append(frame)
        end = perf_counter()

        print(f"Captured {numOfFrames} frames in {(end - start) * 1000} ms")

        vid.release()
        cv2.destroyAllWindows()

        return frames
        