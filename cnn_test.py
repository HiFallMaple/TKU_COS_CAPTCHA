from cnn_model import *
from torch.utils.data import DataLoader
from cnn_dataset import CAPTCHADataset
import torch
from one_hot_code import *
import itertools
from torch.autograd import Variable
from tqdm import tqdm



test_dataset = CAPTCHADataset(config.TEST_CSV, config.CAPTCHA_DIR)
test_dataloader = DataLoader(test_dataset, batch_size=300)


dataiter = iter(test_dataloader)
images, labels = dataiter.next()

cnn = CNN()
cnn.load_state_dict(torch.load(config.TRAIN_RESULT_PATH))

total = 0
correct = 0
progress = tqdm()
for i, (images, labels) in enumerate(test_dataloader):
    vimage = Variable(images)
    outputs = cnn(vimage)

    for output, label in itertools.product(outputs, labels):
        nums = np.array_split(output.detach().numpy(), config.CAPTCHA_LEN)
        result = str()
        # print("CNN: ", end='')
        for num in nums:
            result += str(np.argmax(num))
        # print(result)
        ans = decode(label.numpy())
        # print(f'ANS: {ans}')
        if result == ans:
            # print(True)
            correct += 1
        # else:
            # print(False)
        progress.update(1)
    
    total += labels.size(0)
    if(total%200==0):
        print('Test Accuracy of the model on the %d test images: %f %%' % (total, 100 * correct / total))
print('Test Accuracy of the model on the %d test images: %f %%' % (total, 100 * correct / total))
