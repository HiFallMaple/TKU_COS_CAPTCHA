from cnn_model import *
import torch
from torch.autograd import Variable
from tqdm import tqdm
import cv2
import numpy as np

class CAPTCHA_Translater():
    def __init__(self):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        print(f'Using {self.device} device')
        self.cnn = CNN().to(self.device)
        self.cnn.load_state_dict(torch.load(config.TRAIN_RESULT_PATH))
    
    def translate(self, img: np.ndarray):
        img = config.transform(img).to(self.device)
        img = torch.Tensor([img.tolist()]).to(self.device)
        output = self.cnn.forward(img)[0]

        nums = np.array_split(output.detach().cpu().numpy(), config.CAPTCHA_LEN)
        result = str()
        for num in nums:
            result += config.CHAR_LIST[np.argmax(num)]
        return result

