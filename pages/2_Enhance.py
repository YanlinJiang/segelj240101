import streamlit as st
import cv2
import numpy as np
from PIL import Image
import io
from pages.algorithm.EnhanceQuality import enhance


st.image('./exFile/BJUT.png', use_column_width=True)

# Streamlit 应用界面
st.title("Image Quality Enhancement")

# 文件上传器
image11 = st.file_uploader("Upload an image(jpg/jpeg/png)...", type=["jpg", "jpeg", "png"])

ex = st.button("Execute")
if ex:
    # 读取图片
    if image11 is not None:
        # 处理图片
        temp = enhance(image11)
        enhanced_image = temp.result
        image11.seek(0)

        st.success("finished")
        col1, padding, col2 = st.columns((10, 2, 10))
        with col1:
            #显示原图
            image1 = Image.open(image11)
            st.image(image1, caption='Original image', use_column_width=True)
            step4Button = st.button('re-start')
            if step4Button:
                st.experimental_rerun()
        with col2:
            # 显示处理后的图片
            st.image(enhanced_image, caption='Processed image', channels="BGR", use_column_width=True)
            # 创建下载按钮
            im_pil = Image.fromarray(cv2.cvtColor(enhanced_image, cv2.COLOR_BGR2RGB))
            buffered = io.BytesIO()
            im_pil.save(buffered, format="JPEG")
            st.download_button(
                label="Download",
                data=buffered,
                file_name="enhanced_image.jpg",
                mime="image/jpeg"
            )
    else:
        st.error("Please upload an image first!")
