import logging
from torchvision import transforms

logging.basicConfig(level=logging.INFO)

# 驗證碼內會有的符號
CHAR_LIST = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

CAPTCHA_LEN = 6 # 驗證碼長度（６個數字）
CAPTCHA_DIR = 'CAPTCHA'
TRAIN_CSV = 'train.csv'
TEST_CSV = 'test.csv'
IMAGE_WIDTH = 120
IMAGE_HEIGHT = 32
LEARNING_RATE = 0.001
TRAIN_RESULT_PATH = './captcha_cnn.pth'
TRAIN_DATA_RATE = 0.025
TEST_DATA_RATE = 0.1
EPOCH = 10

transform = transforms.Compose(
    [transforms.ToTensor(),
     transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])