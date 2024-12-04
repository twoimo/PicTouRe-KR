import torch
from torchsummary import summary

# ...existing code...

model_path = "C:/Users/twoimo/Documents/GitHub/PicTouRe-main/backend/models/sun_chillout.pth"
model = torch.load(model_path, map_location=torch.device('cpu'))
model.eval()

# Assuming the model is a typical CNN, adjust input size as needed
summary(model, (3, 224, 224))

# ...existing code...
