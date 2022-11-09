from services.FrameLoaderService.FrameLoader import FrameLoaderOpenCV
from services.PersonService.runner import PersonRunner
from services.FollowerService.Follower import Follower

import sys
sys.path.append("./")
from src.utils.DisplayUtil import DisplayUtil
from src.utils.DataUtil import DataUtil

from time import perf_counter
from typing import List, Dict, Union
import cv2

DEFAULT_COLOUR = (255, 255, 255)

def video():
    # Initialise machine learning models
    personRunner: PersonRunner = PersonRunner()

    # Begin video capturing
    with FrameLoaderOpenCV() as vid:
        while vid.isOpened():
            timeStartPerFrame = perf_counter()

            # Read frame from video stream
            ret, frame = vid.read()
            print(ret)
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
            try:
                personResults = personRunner.run(frame)
            except Exception as e:
                print(e)

            counter["person"] += len(personResults)
            
            try:
                for personCoordinates in personResults:

                    DisplayUtil.drawRectangleWithText(
                        frame,
                        int(personCoordinates["xmin"]),
                        int(personCoordinates["ymin"]),
                        int(personCoordinates["xmax"]),
                        int(personCoordinates["ymax"]),
                        colour,
                        text = "Person"
                    )
            except Exception as e:
                print(e)
            
            cv2.imshow("Frame", frame)

            timeEndPerFrame = perf_counter()

            print(f"Processed one frame in {(timeEndPerFrame - timeStartPerFrame) * 1000} ms.", f"Found {counter}")

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

def follow():
    follower = Follower()
    follower.follow()
    
if __name__ == "__main__":
    # video()
    follow()
