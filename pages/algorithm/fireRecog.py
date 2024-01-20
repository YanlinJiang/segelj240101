import cv2
import numpy as np
from PIL import Image


class fireDetec:
    def __init__(self,uploadFile):
        self.__file_bytes = np.asarray(bytearray(uploadFile.read()), dtype=np.uint8)
        self.img = cv2.imdecode(self.__file_bytes, 1)
        self.result = self.detect_flame()

    def get_dominant_color(self, image):
        pixels = np.float32(image.reshape(-1, 3))
        num_clusters = 1
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
        _, labels, centers = cv2.kmeans(pixels, num_clusters, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
        dominant_color = centers[0].astype(int)
        return dominant_color

    def detect_flame(self):
        # 转换到HSV色彩空间
        image = self.img
        #将图像从BGR颜色空间转换到HSV颜色空间。HSV更适合处理颜色相关的任务：
        #HSV空间更适合描述人类对颜色的感知，因此更适合颜色基础的图像处理任务
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        # 定义火焰颜色的HSV范围
        #lower_flame = np.array([18, 50, 50])
        #upper_flame = np.array([35, 255, 255])
        lower_flame = np.array([4, 140, 175])
        upper_flame = np.array([32, 190, 255])

        # 创建一个颜色掩码，只保留HSV图像中在指定火焰颜色范围内的部分。
        # 颜色掩码是一个图像处理中使用的技术，通常用于特定颜色范围内的像素的选择或过滤
        mask = cv2.inRange(hsv, lower_flame, upper_flame)

        # 在掩码图像中寻找轮廓
        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        # 如果找到了轮廓，则进入下一步处理
        # 对找到的轮廓按面积大小排序，选择最大的两个
        if contours:
            #对找到的轮廓按面积大小排序，并取最大的两个：
            sorted_contours = sorted(contours, key=cv2.contourArea, reverse=True)[:1]



            # 在原始图像上用矩形标记最大的两个火焰区域_(遍历这两个最大的轮廓)
            for contour in sorted_contours:
                # 对于每个轮廓，计算其外接矩形的位置和大小:
                x, y, w, h = cv2.boundingRect(contour)
                #在原始图像上，用红色矩形框标记出这些轮廓:
                cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 10)

        # 返回处理后的图像:
        result = Image.fromarray(image)
        # 首先将PIL图像转换回NumPy数组
        image_np = np.array(result)

        # 将图像从RGB转换回BGR颜色空间，因为OpenCV默认使用BGR
        image_bgr = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)

        # 返回处理后的图像
        return image_bgr

