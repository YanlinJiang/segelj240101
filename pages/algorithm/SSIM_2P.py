
import numpy as np
import cv2
from PIL import Image
from skimage.metrics import structural_similarity as compare_ssim


class SSIM:
    def __init__(self,img1,img2):
        self.img1 = Image.open(img1)
        self.img2 = Image.open(img2)
        self.__gray1 = cv2.cvtColor(np.array(self.img1), cv2.COLOR_RGB2GRAY)
        self.__gray2 = cv2.cvtColor(np.array(self.img2), cv2.COLOR_RGB2GRAY)
        self.__s, _ = compare_ssim(self.__gray1, self.__gray2, full=True)
        self.score = 100*self.__s
    def calculate_ssim(self):
        # 转换图像为灰度
        gray1 = cv2.cvtColor(np.array(self.img1), cv2.COLOR_RGB2GRAY)
        gray2 = cv2.cvtColor(np.array(self.img2), cv2.COLOR_RGB2GRAY)
        # 计算 SSIM
        score, _ = compare_ssim(gray1, gray2, full=True)
        return score