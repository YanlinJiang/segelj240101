import streamlit as st
import cv2
import numpy as np
from PIL import Image
from pages.algorithm.fireRecog import fireDetec

#BJUT logo:
st.image('./exFile/BJUT.png', use_column_width=True)

# 标题
st.title("Flame Detecting Service")
st.caption("Upload an image and the flame in the image will be marked by a rectangular box...")
# 文件上传
image11 = st.file_uploader("upload an image...", type=["jpg", "jpeg", "png"])
# 操作按钮
ex = st.button("Execute")
if ex:
    if image11:
        detecting = fireDetec(image11)
        result = detecting.result
        # 将结果图像转换为PIL格式以显示在Streamlit上
        col1, padding, col2 = st.columns((10, 2, 10))
        with col1:
            image1 = Image.open(image11)
            st.image(image1, use_column_width=True)
        with col2:
            st.image(result, use_column_width=True)
        st.success("finished")
    else:
        st.error("Please input an image first!")