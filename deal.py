import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import torch
from env import *
from torchvision.transforms import ToTensor, ToPILImage

# ��ȡͼ��
image_path = r"E:\ANNprogram\data\BM\sample.png"  # ʹ��ԭʼ�ַ���
image = Image.open(image_path)

# ��ͼ��ת��Ϊ Tensor
tensor_image = ToTensor()(image)

# ���� show_img ������ʾԭʼͼ��
show_img(tensor_image)

# ��ͼ��� Tensor ת���� NumPy ���飬��ȥ�� Alpha ͨ��
data = tensor_image.numpy().transpose(1, 2, 0)[:, :, :3]  # ȥ�� Alpha ͨ��
print(data.shape)
#��ʾ�������
plt.imshow(data)
plt.axis('off')  # ����ʾ������
plt.show()
# ����Ѫ���� RGB ��Χ
lower_bound = np.array([0.70, 0.70, 0.70])  # ʾ������ֵ
upper_bound = np.array([0.87, 0.87, 0.87])  # ʾ������ֵ

# ������Ĥ
mask = np.all((data >= lower_bound) & (data <= upper_bound), axis=-1)

# ��ȡѪ������
blood_bar = np.zeros_like(data)
blood_bar[mask] = data[mask]

# ��Ѫ������ת��Ϊ Tensor
tensor_blood_bar = torch.from_numpy(blood_bar).permute(2, 0, 1)

# ��ʾѪ������
show_img(tensor_blood_bar)

# ��ȡ��������
pixels = blood_bar[blood_bar > 0]
print(pixels)
print(pixels.size)