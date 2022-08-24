from services.FaceService.model import FaceModel

class FaceRunner:
    def __init__(self) -> None:
        self.model = FaceModel()

    def run(self, frame):
        result = self.model.detect(frame)
        if len(result) == 0:
            return None

        xMin, yMin, xLength, yLength = self.model.detect(frame)[0]
        return {
            "xmin": xMin,
            "ymin": yMin,
            "xmax": xMin + xLength,
            "ymax": yMin + yLength
        }