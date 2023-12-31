import streamlit as st
import cv2 as cv
import numpy as np
import math

class PSNRv2:
    def __init__(self,iii1,iii2):
        file_bytes_1 = np.asarray(bytearray(iii1.read()), dtype=np.uint8)
        self.img1 = cv.imdecode(file_bytes_1, 1)

        file_bytes_2 = np.asarray(bytearray(iii2.read()), dtype=np.uint8)
        self.img2 = cv.imdecode(file_bytes_2, 1)
        self.mse = np.mean((self.img1 / 255. - self.img2 / 255.) ** 2)
        if self.mse < 1.0e-10:
            self.psnr = 100
        else:
            self.psnr = 20 * math.log10(1 / math.sqrt(self.mse))



    # 定义计算均方误差（MSE）的函数
    def get_mse(self):
        img1 = self.img1
        img2 = self.img2
        return np.mean((img1 / 255. - img2 / 255.) ** 2)

    # 定义计算峰值信噪比（PSNR）的函数
    def get_psnr(self):
        img1 = self.img1
        img2 = self.img2
        mse = self.get_mse(img1, img2)
        if mse < 1.0e-10:
            return 100
        pixel_max = 1
        return 20 * math.log10(pixel_max / math.sqrt(mse))



