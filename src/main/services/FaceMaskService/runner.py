from services.FaceMaskService.model import FaceMaskModel
from services.FaceMaskService.dataset import FaceMaskDataset
import torch

class FaceMaskRunner:
    def __init__(self) -> None:
        self.device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
        self.stateDict = torch.load("src/main/services/FaceMaskService/models/face_mask.pt", map_location = self.device).get("state_dict")
        self.model = FaceMaskModel()
        self.model.load_state_dict(self.stateDict, strict=False)
        self.model.eval()

    def run(self, frame) -> bool:
        transformations = FaceMaskDataset().transformations
        try:
            output = self.model(transformations(frame).unsqueeze(0).to(self.device))
        except ValueError as e:
            print(e)
            print(frame)
            return None
        _, predicted = torch.max(output.data, 1)
        
        return bool(predicted)