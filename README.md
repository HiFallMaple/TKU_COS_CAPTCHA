# 淡江選課系統驗證碼CNN模型
---
使用 pytorch 建立的 CNN 模型，並建立 `CAPTCHA_Translater()` 以供調用。

## 目錄
---
- [淡江選課系統驗證碼CNN模型](#-淡江選課系統驗證碼cnn模型)
- [目錄](#-目錄)
- [訓練集](#-訓練集)
- [調用](#-調用)

## 訓練集
---
透過漏洞爬取的訓練集資料，共有26萬種數字，每種數字各有10張 jpg 檔，可透過以下連結下載。
+ [google drive](https://drive.google.com/file/d/1gWEezXfMkhXcuvxYKLczQIQfeyOe8t6l/view?usp=sharing)


## 調用
---
將檔案透過 cv2 讀取後，調用 `CAPTCHA_Translater.translate()`，範例如下：
```python
from cnn_translate import CAPTCHA_Translater
import config
import cv2

filename = '000998_3.jpg'
img = cv2.imread(f'{config.CAPTCHA_DIR}/{filename[:6]}/{filename}')
translater = CAPTCHA_Translater()
print(translater.translate(img))

```