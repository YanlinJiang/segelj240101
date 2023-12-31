#encoding=utf-8
import cv2
import numpy as np
from skimage.metrics import structural_similarity as compare_ssim
from PIL import Image



class NRSSzwei:
    def __init__(self, uploaded_file):
        self.__image1 = Image.open(uploaded_file)
        # 将图像转换为灰度
        self.__image1_gray = self.__image1.convert('L')
        # 将 PIL 图像转换为 NumPy 数组
        self.__image1_np = np.array(self.__image1_gray)
        self.iii = self.__image1_np
        self.nrss = self.NRSS()

    def gauseBlur(self, img):
        img_Guassian = cv2.GaussianBlur(img, (7, 7), 0)
        return img_Guassian

    def loadImage(self, filepath):
        img = cv2.imread(filepath, 0)  # Load in grayscale
        return img

    def showImage(self, img):
        cv2.imshow('image', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def saveImage(self, path, img):
        cv2.imwrite(path, img)

    def sobel(self, img):
        x = cv2.Sobel(img, cv2.CV_16S, 1, 0)
        y = cv2.Sobel(img, cv2.CV_16S, 0, 1)
        absX = cv2.convertScaleAbs(x)  # Convert back to uint8
        absY = cv2.convertScaleAbs(y)
        dst = cv2.addWeighted(absX, 0.5, absY, 0.5, 0)
        return dst

    def getBlock(self, G, Gr):
        (h, w) = G.shape
        G_blk_list = []
        Gr_blk_list = []
        sp = 6
        for i in range(sp):
            for j in range(sp):
                G_blk = G[int((i / sp) * h):int(((i + 1) / sp) * h), int((j / sp) * w):int(((j + 1) / sp) * w)]
                Gr_blk = Gr[int((i / sp) * h):int(((i + 1) / sp) * h), int((j / sp) * w):int(((j + 1) / sp) * w)]
                G_blk_list.append(G_blk)
                Gr_blk_list.append(Gr_blk)
        sum = 0
        for i in range(sp * sp):
            mssim = compare_ssim(G_blk_list[i], Gr_blk_list[i])
            sum += mssim
        nrss = 1 - sum / (sp * sp * 1.0)
        return nrss

    def NRSS(self):
        image = self.iii
        # Gaussian Blurring
        Ir = self.gauseBlur(image)
        G = self.sobel(image)
        Gr = self.sobel(Ir)
        # Get block information
        result = self.getBlock(G, Gr)
        result = result*100
        return result

# if __name__ == "__main__":
#     filepath = "perfect.jpg"
#     pro = NRSS_Processor()
#     pro.NRSS(filepath)