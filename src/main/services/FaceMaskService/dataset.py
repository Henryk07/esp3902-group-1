import numpy as np
import cv2
from torchvision.transforms import Compose, ToPILImage, Resize, ToTensor

from torch.utils.data import Dataset
from torch import tensor, long


class FaceMaskDataset(Dataset):
    def __init__(self, dataFrame = None):
        self.dataFrame = dataFrame
        
        self.transformations = Compose([
            ToPILImage(),
            Resize((100, 100)),
            ToTensor()
        ])
    
    def __getitem__(self, key):
        if isinstance(key, slice):
            raise NotImplementedError('slicing is not supported')
        
        row = self.dataFrame.iloc[key]
        image = cv2.imdecode(np.fromfile(row['image'], dtype=np.uint8),
                             cv2.IMREAD_UNCHANGED)
        return {
            'image': self.transformations(image),
            'mask': tensor([row['mask']], dtype=long)
        }
    
    def __len__(self):
        return len(self.dataFrame.index)
