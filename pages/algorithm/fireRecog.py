import cv2
import numpy as np
from PIL import Image


class fireDetec:
    def __init__(self,uploadFile):
        self.__file_bytes = np.asarray(bytearray(uploadFile.read()), dtype=np.uint8)
        self.img = cv2.imdecode(self.__file_bytes, 1)
        self.result = self.detect_flame()

    def detect_flame(self):
        # 转换到HSV色彩空间
        image = self.img
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        # 定义火焰颜色的HSV范围
        lower_flame = np.array([18, 50, 50])
        upper_flame = np.array([35, 255, 255])

        # 创建一个颜色掩码
        mask = cv2.inRange(hsv, lower_flame, upper_flame)

        # 寻找火焰区域
        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        # 对找到的轮廓按面积大小排序，选择最大的两个
        if contours:
            sorted_contours = sorted(contours, key=cv2.contourArea, reverse=True)[:2]

            # 在原始图像上用矩形标记最大的两个火焰区域
            for contour in sorted_contours:
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
        result = Image.fromarray(image)

        return result
