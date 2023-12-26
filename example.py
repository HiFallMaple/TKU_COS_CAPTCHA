from cnn_translate import CAPTCHA_Translater
import config
import utils
import cv2

filename = '000998_3.jpg'
img = cv2.imread()
translater = CAPTCHA_Translater(utils.get_img_path(filename))
print(translater.translate(img))