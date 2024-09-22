import torch
import time
import threading
import torch.nn.functional as F
import torchvision
import torchvision.transforms as transforms
import torchvision.models as models
import pyautogui
from PIL import Image
import matplotlib.pyplot as plt

# ����ת����������PILͼ��ת��Ϊ3*224*224��Tensor
def transform_image(img):
    transform = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])
    return transform(img).unsqueeze(0)

# ����Ļ�����ȡͼƬ
def get_img():
    return  pyautogui.screenshot()

# ��ʾͼ��
def show_img(img):
    plt.imshow(transforms.ToPILImage()(img))
    plt.show()

class envs():
    def __init__(self,flash_time=0.1):
        self.action_space = [
    'a', 'd', 'w', 's', 'q', 'e', 'r', 'z', 'x', 'c', 'v', ' ',
    'ctrl', 'ml', 'mm', 'mr',
    'move_up', 'move_down', 'move_left', 'move_right',
    'none', 'none', 'none'
    ]
        self.observation_space = (224, 224, 3)
        self.action_dim = len(self.action_space)
        self.flash_time = flash_time
        ##�ϸ�ʱ��Ѫ����������������
        self.health=1000
        self.mana=100
        self.stamina=100

        self.line_number=[] ##�кţ����ⶨ
        self.fcolour=[] ##��ɫ�����ⶨ
        self.findready=[] ##�Ƿ���Ե�����������ⶨ

    def _simulate_key_press(self, key):
        if key == 'ctrl':
            pyautogui.keyDown('ctrl')
            time.sleep(self.flash_time)
            pyautogui.keyUp('ctrl')
        elif key in ['ml', 'mm', 'mr']:
            if key == 'ml':
                pyautogui.click(button='left')
            elif key == 'mm':
                pyautogui.click(button='middle')
            elif key == 'mr':
                pyautogui.click(button='right')
        elif key in ['move_up', 'move_down', 'move_left', 'move_right']:
            if key == 'move_up':
                pyautogui.moveRel(0, -10)
            elif key == 'move_down':
                pyautogui.moveRel(0, 10)
            elif key == 'move_left':
                pyautogui.moveRel(-10, 0)
            elif key == 'move_right':
                pyautogui.moveRel(10, 0)
        else:
            pyautogui.keyDown(key)
            time.sleep(self.flash_time)
            pyautogui.keyUp(key)
    from PIL import Image

def find_color_length(image_path, y, target_color):
    # ��ͼƬ
    img = Image.open(image_path)
    
    # ��ȡͼƬ�ߴ�
    width, height = img.size
    
    # ��ʼ��������ɫ����
    length = 0
    max_length = 0
    
    # ����ָ���е���������
    for x in range(width):
        # ��ȡ������ɫ
        pixel_color = img.getpixel((x, y))
        
        # �����ɫƥ�䣬�����ӳ���
        if pixel_color == target_color:
            length += 1
            max_length = max(max_length, length)
        else:
            # �����ɫ��ƥ�䣬�����ó���
            length = 0
    
    return max_length

    ##ͨ������tensor��Ӧͼ��ָ���������ػ�õ�ǰ����״̬
    def get_reward(self,img):
        ##ʶ��ͼ�����״̬ʶ�𣬴�����
        return reward
    def step(self,actions_tensor):
        if not isinstance(actions_tensor,torch.Tensor):
            raise TypeError('actions_tensor must be a torch.Tensor')

        _,top_indices = torch.topk(actions_tensor, 2)
        # ������ת��Ϊ��Ӧ�İ���
        keys = [self.action_space[index.item()] for index in top_indices]

        # �����߳��б�
        threads = []

        # �����߳�
        for key in keys:
            thread = threading.Thread(target=self._simulate_key_press, args=(key,))
            threads.append(thread)
            thread.start()

        # �ȴ������߳����
        for thread in threads:
            thread.join()