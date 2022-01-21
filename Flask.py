#!/usr/bin/env python
# coding: utf-8



get_ipython().system('pip3 install matplotlib')
get_ipython().system('pip3 install opencv-python')
get_ipython().system('pip3 install flask')
get_ipython().system('pip3 install facenet')
get_ipython().system('pip3 install MTCNN')
get_ipython().system('pip3 install facenet_pytorch')
get_ipython().system('pip3 install opencv-python')
get_ipython().system('pip3 install MMCV')
get_ipython().system('pip3 install IPython')
get_ipython().system('pip3 install Ipython display')




from flask import Flask, request, render_template # render_template : HTML 연결용
import cv2
import io #파일 입출력용
import numpy as np
import matplotlib.pyplot as plt
import joblib
from tensorflow.keras.models import load_model # 저장된 모델 로딩용




from flask import Flask 
app = Flask (__name__) #  app 인스턴스화

@app.route('/fileUpload', methods=['POST']) # 실제 접속하는 url // 사용자의 요청을 처리하기 위한 라우터
def hello_world(): 
   
    loaded_model = joblib.load("./model_Park.pkl") # 모델로딩
    return 'Hello, World!' 
    

if __name__ == "__main__": 
    app.run(port='8000') # 서버가동 시작



