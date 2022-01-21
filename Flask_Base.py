#!/usr/bin/env python
# coding: utf-8

('pip3 install flask')


from flask import Flask, request, render_template # render_template : HTML 연결용
import cv2
import io #파일 입출력용
import numpy as np
import matplotlib.pyplot as plt
import joblib
from tensorflow.keras.models import load_model # 저장된 모델 로딩용




from flask import Flask 
app = Flask (__name__) #  app 인스턴스화

@app.route('/fileUpload', methods=['POST']) # 트리거 할 함수 이름 / 사용자의 요청을 처리하기 위한 라우터 / .../fileUpload url
def hello_world(): 
   
    loaded_model = joblib.load("./model_Park.pkl") # 모델로딩
    return 'Hello, World!' 
    

if __name__ == "__main__": 
    app.run(port='8000') # 서버가동 시작



