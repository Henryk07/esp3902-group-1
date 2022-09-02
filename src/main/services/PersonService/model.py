import torch
import json
from typing import List, Dict

class PersonModel:

    def __init__(self) -> None:
        self.device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
        self.model = torch.hub.load("ultralytics/yolov5", "yolov5m", pretrained = True)
        # TODO load model without using pytorch hub, i.e. load from downloaded model
        # torch.save(self.model, "src/main/services/PersonService/models/person.pt")
        # self.model = torch.load("src/main/services/PersonService/models/person.pt", map_location = self.device)
        self.model.classes = 0
        self.model.to(self.device)
        self.model.eval()

    def infer(self, frame: str) -> List[Dict[str, object]]:
        return json.loads(self.model(frame).pandas().xyxy[0].to_json(orient="records"))
    