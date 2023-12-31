
import numpy as np
import cv2
import matplotlib.pyplot as plt


# 加噪声
def noise(img):
    out = img
    rows, cols, chn = img.shape
    for i in range(5000):
        x = np.random.randint(0, rows)
        y = np.random.randint(0, cols)
        out[x, y, :] = 255
    return out


if __name__ == "__main__":
    image = cv2.imread('perfect.jpg')
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # 格式转换，

    plt.subplot(1, 2, 1)
    noise_img = noise(image)
    plt.imshow(noise_img)
    plt.axis('off')
    plt.title('noise')

    # 中值滤波
    result4 = cv2.medianBlur(noise_img, 3)

    plt.subplot(1, 2, 2)
    plt.imshow(result4)
    plt.axis('off')
    plt.title('median')

    plt.show()