from services.FrameLoaderService.FrameLoader import FrameLoaderOpenCV
from services.FaceService.runner import FaceRunner
from services.PersonService.runner import PersonRunner
from services.FaceMaskService.runner import FaceMaskRunner

import sys
sys.path.append("./")
from src.utils.DisplayUtil import DisplayUtil
from src.utils.DataUtil import DataUtil

from time import perf_counter
from typing import List, Dict, Union
import cv2

TOTAL_FRAME = 15
DEFAULT_COLOUR = (255, 255, 255)

def video():
    # Initialise machine learning models
    personRunner: PersonRunner = PersonRunner()
    faceRunner: FaceRunner = FaceRunner()
    faceMaskRunner: FaceMaskRunner = FaceMaskRunner()

    # Begin video capturing
    with FrameLoaderOpenCV(0) as vid:
        while vid.isOpened():
            timeStartPerFrame = perf_counter()

            # Read frame from video stream
            ret, frame = vid.read()
            
            # If fail to read frame, continue
            if not ret:
                continue
            
            # Colour for display
            colour = DEFAULT_COLOUR

            # Store the objects counter
            counter: Dict[str, int] = {
                "person": 0,
                "face": 0,
                "face_mask": 0
            }
            
            # Get persons
            personResults = personRunner.run(frame)
            counter["person"] += len(personResults)
            for personCoordinates in personResults:
                # Get person frame
                personFrame = DataUtil.cropFrame(frame, personCoordinates)
                
                # Get face frame
                faceResult: Union[Dict[str, int], bool] = faceRunner.run(personFrame)
                if faceResult is not None:
                    counter["face"] += 1
                    faceFrame = DataUtil.cropFrame(personFrame, faceResult)

                    # Infer face mask
                    faceMaskResult: bool = faceMaskRunner.run(faceFrame)
                    if faceMaskResult:
                        counter["face_mask"] += 1
                        colour = (10, 255, 0)
                    else:
                        colour = (10, 0, 255)

                DisplayUtil.drawRectangleWithText(
                    frame,
                    personCoordinates["xmin"],
                    personCoordinates["ymin"],
                    personCoordinates["xmax"],
                    personCoordinates["ymax"],
                    colour,
                    text = "Person"
                )

            cv2.imshow("Frame", frame)

            timeEndPerFrame = perf_counter()

            print(f"Processed one frame in {(timeEndPerFrame - timeStartPerFrame) * 1000} ms.", f"Found {counter}")

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break


            
    
if __name__ == "__main__":
    video()