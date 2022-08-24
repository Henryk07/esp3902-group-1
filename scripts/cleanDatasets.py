from tqdm import tqdm
import cv2
import pandas as pd
from pathlib import Path

def cleanFaceMaskDataset():
    datasetPath = Path("datasets/face_mask")
    maskPath = datasetPath / "AFDB_masked_face_dataset"
    nonMaskPath = datasetPath / "AFDB_face_dataset"
    maskDF = pd.DataFrame(columns = ["image", "mask"])

    for subject in tqdm(list(nonMaskPath.iterdir()), desc='non mask photos'):
        for imgPath in subject.iterdir():
            maskDF = pd.concat([maskDF, pd.DataFrame([{
                'image': str(imgPath),
                'mask': 0
            }])], ignore_index = True)

    for subject in tqdm(list(maskPath.iterdir()), desc='mask photos'):
        for imgPath in subject.iterdir():
            maskDF = pd.concat([maskDF, pd.DataFrame([{
                'image': str(imgPath),
                'mask': 1
            }])], ignore_index = True)

    maskDF.to_csv('datasets/face_mask/face_mask.csv')

def main():
    cleanFaceMaskDataset()

if __name__ == "__main__":
    main()