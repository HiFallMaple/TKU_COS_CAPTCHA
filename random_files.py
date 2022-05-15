from pathlib import Path
from tqdm import tqdm
import numpy
import os
import logging
import csv
from config import CAPTCHA_DIR, TRAIN_CSV, TEST_CSV, TRAIN_DATA_RATE, TEST_DATA_RATE


captcha_list = os.listdir(CAPTCHA_DIR)
captcha_len = len(os.listdir(CAPTCHA_DIR))
train_data_quantity = int(captcha_len * TRAIN_DATA_RATE * 10)
test_data_quantity = int(captcha_len * TEST_DATA_RATE * 10)
imgs_list = list()

logging.info(f'Number of captcha: {captcha_len}')

for captcha in captcha_list:
    imgs_list += [f'{captcha}_{i}.jpg' for i in range(10)]
train_data_list = numpy.random.choice(imgs_list, size=train_data_quantity, replace=False)
remaining_list  = list(set(imgs_list) - set(train_data_list))
test_data_list = numpy.random.choice(remaining_list, size=test_data_quantity, replace=False)

logging.info(f'train: {len(train_data_list)}')
logging.info(f'test: {len(test_data_list)}')
logging.info(f'total: {len(train_data_list) + len(test_data_list)}')

with open(TRAIN_CSV, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for row in tqdm(train_data_list):
        writer.writerow([row])

with open(TEST_CSV, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for row in tqdm(test_data_list):
        writer.writerow([row])