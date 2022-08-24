import torch

def ckptToPt(filepathFrom, filepathTo):
    model = torch.load(filepathFrom)
    torch.save(model, filepathTo)

if __name__ == "__main__":
    ckptToPt("models/face_mask/face_mask.ckpt", "models/face_mask/face_mask.pt")