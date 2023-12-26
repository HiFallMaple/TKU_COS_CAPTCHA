from torch.utils.data import Dataset
import csv
import cv2
import one_hot_code
import config
import utils

class CAPTCHADataset(Dataset):
    """Face Landmarks dataset."""

    def __init__(self, csv_name, img_dir):
        self.img_name_list = self.__load_csv(csv_name)
        self.img_dir = img_dir
        
    def __getitem__(self, index):
        filename = self.img_name_list[index]
        img = cv2.imread(utils.get_img_path(filename))
        img = config.transform(img)
        label = one_hot_code.encode(filename[:6])
        return (img, label)

    def __len__(self):
        return len(self.img_name_list)

    def __load_csv(self, csv_name: str) -> list():
        data_list = list()
        with open(csv_name, 'r') as csvfile:
            reader = csv.reader(csvfile)
            for line in reader:
                data_list.append(line.pop())
        return data_list


