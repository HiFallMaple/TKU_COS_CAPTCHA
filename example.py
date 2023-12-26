from cnn_translate import CAPTCHA_Translater
import config
import utils
import cv2

filename = '000998_3.jpg'
img = cv2.imread(utils.get_img_path(filename))
translater = CAPTCHA_Translater()
print(translater.translate(img))