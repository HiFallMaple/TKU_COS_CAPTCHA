from cnn_translate import CAPTCHA_Translater
import config
import cv2

filename = '000998_3.jpg'
img = cv2.imread(f'{config.CAPTCHA_DIR}/{filename[:6]}/{filename}')
translater = CAPTCHA_Translater()
print(translater.translate(img))