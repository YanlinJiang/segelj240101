import streamlit as st
from PIL import Image
import numpy as np
from skimage.metrics import mean_squared_error

class PSNR:
    def __init__(self,image1, image2):
        self.img1 = image1
        self.img2 = image2
    def calculate_psnr(self):
        mse = mean_squared_error(self.img1, self.img2)
        if mse == 0:
            return float('inf')
        max_pixel = 255.0
        psnr = 20 * np.log10(max_pixel / np.sqrt(mse))
        return psnr