import streamlit as st
import cv2
import numpy as np
from PIL import Image
import io

class enhance:
    def __init__(self,uploadFile):
        self.__image = Image.open(uploadFile)
        # 将图片转换为OpenCV格式
        self.__image2 = np.array(self.__image)
        self.img = cv2.cvtColor(self.__image2, cv2.COLOR_RGB2BGR)
        self.result = self.unsharp_mask()

    def unsharp_mask(self, sigma=1.0, strength=1.5, bilateral_filter_diameter=9, sigma_color=75, sigma_space=75):
        # 使用双边滤波减少噪声
        image = self.img
        image = cv2.bilateralFilter(image, bilateral_filter_diameter, sigma_color, sigma_space)

        # 使用高斯模糊
        blurred = cv2.GaussianBlur(image, (0, 0), sigma)

        # 未锐化掩模: 增强边缘
        sharpened = cv2.addWeighted(image, 1 + strength, blurred, -strength, 0)
        return sharpened