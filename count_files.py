import os
import shutil
from config import CAPTCHA_DIR

# 計算有多少圖片檔，並刪除於錯誤位置之.jpg檔案

num_of_imgs = 0
REMOVE = True

verification_list = os.listdir(CAPTCHA_DIR)
verification_len = len(os.listdir(CAPTCHA_DIR))
print(f'Number of CAPTCHA: {verification_len}')
for verify_code in verification_list:
    if '.jpg' in verify_code:
        os.remove(f'{CAPTCHA_DIR}/{verify_code}')
        print(f'remove {verify_code}')
        continue
    num_per_code = len(os.listdir(f'{CAPTCHA_DIR}/{verify_code}'))
    if num_per_code != 10:
        print(f'{verify_code}: {num_per_code}')
        if REMOVE:
            shutil.rmtree(f'{CAPTCHA_DIR}/{verify_code}')
            print(f'remove {verify_code}!')
    else:
        num_of_imgs += num_per_code
print(f'Number of imgs: {num_of_imgs}')
