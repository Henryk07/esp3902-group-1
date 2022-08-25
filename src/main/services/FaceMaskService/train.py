from main.services.FaceMaskService.model import FaceMaskModel
import torch
from pathlib import Path
from pytorch_lightning.loggers import TensorBoardLogger
from pytorch_lightning import Trainer
from pytorch_lightning.callbacks import ModelCheckpoint

def train():
    model = FaceMaskModel(Path('datasets/face_mask/face_mask.csv'))
    logger = TensorBoardLogger("tensorboard", name="face_mask")
    checkpointCallback = ModelCheckpoint(
        filename='{epoch}-{val_loss:.2f}-{val_acc:.2f}',
        verbose=True,
        monitor='val_acc',
        mode='max'
    )
    trainer = Trainer(gpus=1 if torch.cuda.is_available() else 0,
                      max_epochs=10,
                      logger=logger,
                      callbacks=[checkpointCallback])

    trainer.fit(model)


if __name__ == "__main__":
    train()