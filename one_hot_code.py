# -*- coding: UTF-8 -*-
import numpy as np
import config

class LengthError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)


def encode(string: str) -> np.ndarray:
    if len(string) is not config.CAPTCHA_LEN:
        message = 'CAPTCHA length is not equal to config.CAPTCHA_LEN'
        raise LengthError(message)
    result = None
    for num in string:
        code = np.zeros(len(config.CHAR_LIST))
        code[config.CHAR_LIST.index(num)] = 1
        if result is None:
            result = code
        else:
            result = np.concatenate([result, code])
    return result

def decode(vector: np.ndarray) -> str:
    nums = np.array_split(vector, config.CAPTCHA_LEN)
    if len(nums) is not config.CAPTCHA_LEN:
        message = 'Length of one hot code is not equal to config.CAPTCHA_LEN'
        raise LengthError(message)
    result = str()
    for code in nums:
        index = np.where(code == 1)[0][0]
        result += config.CHAR_LIST[index]
    return result
