import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from PIL import Image
import cv2
import io
from pages.algorithm.SSIM_2P import SSIM
from pages.algorithm.PSNR_2P import PSNR
from pages.algorithm.NRSS2 import NRSSzwei
from pages.algorithm.PSNR_V2 import PSNRv2
from skimage.metrics import structural_similarity as compare_ssim

#BJUT logo:
st.image('./exFile/BJUT.png', use_column_width=True)

def refreshButton():
    step4Button = st.button('re-start')
    if step4Button:
        st.experimental_rerun()

def outputImgDetail(uploadImg):
    imgOpen = Image.open(uploadImg)
    st.image(imgOpen, use_column_width=True)
    image_details = {"file_name": uploadImg.name,
                     "file_type": uploadImg.type,
                     "file_size": uploadImg.size}
    st.write(image_details)

st.header("""Multiple Modules Image Processing""")
st.caption("-You can choose what function you like and processing image here.")


#第一步，选择FR/RR/NR
step1Button = st.selectbox('Step-1, Choose an type for image processing:',
             ('Full Reference(FR)','Reduce Reference(RR)','None Reference(NR)','Click to select'),index=3)

if step1Button=='Full Reference(FR)':
    # 第二步，选择算法
    multiSelect = st.multiselect('Step-2, click to choose multiple algorithm here:',['SSIM', 'PSNR'])
    st.write("\n\n")
    image11 = st.file_uploader("-Upload the *Original image(jpg/jpeg/png)...", type=["png", "jpg", "jpeg"])
    image22 = st.file_uploader("-Upload the damaged image(jpg/jpeg/png)...", type=["png", "jpg", "jpeg"])
    step3Button = st.button("Execute")
    if step3Button:
        if image11 and image22:
            #选择SSIM处理方法：
            if 'SSIM' in multiSelect:
                tempSSIM = SSIM(image11, image22)
                st.write("SSIM score:", tempSSIM.score, ' /100')
                image11.seek(0); image22.seek(0);
            #选择PSNR处理方法:
            if 'PSNR' in multiSelect:
                tempPSNR = PSNRv2(image11, image22)
                st.write("MSE score:", tempPSNR.mse, "\n\nPSNR score:",tempPSNR.psnr,' /100')
                image11.seek(0);image22.seek(0);
            #输出两张图与两张图相关的具体信息:
            st.success("finished")
            col1, padding, col2 = st.columns((10, 2, 10))
            with col1:
                outputImgDetail(image11)
            with col2:
                outputImgDetail(image22)
            refreshButton()

        else:
            st.error("Please input two images first")

elif step1Button=='Reduce Reference(RR)':
    # 第二步，选择算法
    multiSelect = st.multiselect('Step-2, click to choose multiple algorithm here:', ['尚未开放'])

elif step1Button=='None Reference(NR)':
    # 第二步，选择算法
    multiSelect = st.multiselect('Step-2, click to choose multiple algorithm here:',['NRSS'])
    st.write("\n\n")
    image11 = st.file_uploader("-Upload an image(jpg/jpeg/png)...", type=["jpg", "png", "jpeg"])
    step3Button = st.button("Execute")
    if step3Button:
        if image11:
            if 'NRSS' in multiSelect:
                tempNRSS = NRSSzwei(image11)
                st.write('NRSS score:', tempNRSS.nrss, ' /100')
                image11.seek(0);

            st.success("finished")
            col1, col2 = st.columns((10, 12))
            with col1:
                outputImgDetail(image11)
            refreshButton()
        else:
            st.error("Please input an image first")