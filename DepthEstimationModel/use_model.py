import torch
from model import UNet
from PIL import Image
import torchvision.transforms as transforms
import torchvision.transforms.functional as F
import matplotlib.pyplot as plt
from scipy import ndimage

# Load PNG Image File
input_image = Image.open('train_data_new2/test/rgb/002.png').convert('RGB')
r, g, b = input_image.split()
input_image = b

# Transfor to PyTorch tensor
transform = transforms.ToTensor()
input_data = transform(input_image).unsqueeze(0)
model = UNet()

# Load model parameter
checkpoint_path = './model/model_L4_test_bs30_lr0.0001_epoch400_ReverseHuber_Loss0.0044_seed105.pth'
checkpoint = torch.load(checkpoint_path)
model.load_state_dict(checkpoint)

# set model to evaluation model
model.eval()

# predicting
with torch.no_grad():
    output = model(input_data)

output_image = F.to_pil_image(output.squeeze())

# Show Image
output_image.show()

output_np = output.squeeze().cpu().numpy()

# Draw Image
plt.imshow(output_np, cmap='inferno')

# Show Plot
plt.show()