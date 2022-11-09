import sys
sys.path.append("./")
sys.path.append("./src/main/")

from services.PersonService.runner import PersonRunner
from services.MotorService.Motor import Motor
from services.FrameLoaderService.FrameLoader import FrameLoaderOpenCV

from src.utils.DisplayUtil import DisplayUtil

from time import perf_counter
import cv2

class Follower:
    def __init__(self):
        self.person_runner: PersonRunner = PersonRunner()
        self.motor: Motor = Motor()
        self.motor.rotate(90.0)
        self.motor.tilt(90.0)
        self.camera_angle_x: float = 30.0
        self.camera_angle_y: float = 15.0
        self.angle_tolerance: float = 1.0
        self.buffer: int = 10
        self.counter: int = 0
        pass

    def follow(self) -> None:
        with FrameLoaderOpenCV() as vid:
            while vid.isOpened():
                
                if self.counter != 0:
                    self.counter = (self.counter + 1) % self.buffer
                    vid.read()
                    continue
                
                self.counter += 1
                
                time_per_frame_start = perf_counter()

                # Read frame from video stream
                ret, frame = vid.read()
                
                # If fail to read frame, continue
                if not ret:
                    continue
                
                # Get objects (only person for now)
                objects = self.person_runner.run(frame)

                # If there are no object captured, continue
                if len(objects) == 0:
                    continue

                # Assume only 1 object captured in frame
                object_to_track = objects[0]

                # Show the frame with the object that is being followed
                DisplayUtil.drawRectangleWithText(
                    frame,
                    int(object_to_track["xmin"]),
                    int(object_to_track["ymin"]),
                    int(object_to_track["xmax"]),
                    int(object_to_track["ymax"]),
                    (255, 255, 255),
                    text = f"Following this object"
                )
                
                cv2.imshow("Frame", frame)
                
                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break

                # Calculate the position of the object relative to the center of the frame
                object_center_x = (object_to_track["xmin"] + object_to_track["xmax"]) // 2
                object_center_y = (object_to_track["ymin"] + object_to_track["ymax"]) // 2

                frame_center_x = len(frame[0]) / 2
                frame_center_y = len(frame) / 2

                frame_max_x = len(frame[0])
                frame_max_y = len(frame)

                position_x = object_center_x - frame_center_x
                position_y = object_center_y - frame_center_y

                deviation_x = position_x * (self.camera_angle_x / 2) / (frame_max_x / 2)
                deviation_y = position_y * (self.camera_angle_y / 2) / (frame_max_y / 2)

                # If deviation is low enough, continue
                if abs(deviation_x) <= self.angle_tolerance and abs(deviation_y) <= self.angle_tolerance:
                    continue

                # Else, move (rotate and tilt) the camera based on the deviation
                if abs(deviation_x) > self.angle_tolerance:
                    self.motor.rotate(self.motor.rotate_angle - deviation_x)
                    print(f"Rotated {deviation_x:.3f}")
                
                if abs(deviation_y) > self.angle_tolerance:
                    self.motor.tilt(self.motor.tilt_angle + deviation_y)
                    print(f"Tilted {deviation_y:.3f}")

                time_per_frame_end = perf_counter()

                print(f"Finished one iteration in {(time_per_frame_end - time_per_frame_start) * 1000} ms.")
        return
