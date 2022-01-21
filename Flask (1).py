#!/usr/bin/env python
# coding: utf-8

# In[2]:


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


# In[12]:


from flask import Flask, request, render_template # render_template : HTML 연결용
import cv2
import io #파일 입출력용
import numpy as np
import matplotlib.pyplot as plt
import joblib
from tensorflow.keras.models import load_model # 저장된 모델 로딩용


# In[11]:


from flask import Flask 
app = Flask (__name__) #  app 인스턴스화

@app.route('/') # 실제 접속하는 url
def hello_world(): 
    loaded_model = joblib.load("./model_Park.pkl") # 모델로딩
    return 'Hello, World!' 
    

if __name__ == "__main__": 
    app.run(port='8000') # 서버가동 시작


# In[12]:


frames_tracked = [] # 얼굴 추적 프레임을 저장할 리스트

# enumerate : 반복문 사용 시 몇 번째 반복문인지 확인할 떄 사용, 인덱스 번호와 원소를 tuple형태로 반환합니다.
for i, frame in enumerate(frames): # frame : 튜플형태로 사진 데이터 저장 / i : 인덱스 번호
    print('\r프레임: {}'.format(i + 1)) # 각각의 프레임 출력
    
    # 얼굴 탐지
    boxes, _ = mtcnn.detect(frame) # mtcnn 모델을 활용하여 한 프레임씩 탐지 후 박스에 결과 저장 
    # boxes : 2차원의 배열 (21, 4) # 행 : 감지된 사람의 얼굴 수 / 열 : 해당 정보의 차원 및 좌표
    # _ :  프레임 한 장에 탐지된 사람들의 얼굴 확률 값
    
    # 얼굴 그리기
    frame_draw = frame.copy() # 프레임 한 장 카피
    draw = ImageDraw.Draw(frame_draw) 
        
    # 감지된 사람 수가 0이라면 모델에 오류가 발생함 이를 해결하기 위한 알고리즘
    # 그림 그려주기
    try:
        for box in boxes:
            if box is not None :
                # 네모 그리기
                draw.rectangle(box.tolist(), outline=(255, 0, 0), width=1) # tolist : list 형태로 대상의 차원에 맞춰서 반환, 얼굴 탐지가 된 좌표값
                #outline : 네모 색상 / width : 두께
                frames_tracked.append(frame_draw.resize((640, 360), Image.BILINEAR)) # 리스트에 추가
                # BILINEAR : 이미지 리사이즈 시 이진선형을 사용하여 리사이즈 하겠다.
    except:
         print("except!!") # 가독성을 위한 띄어쓰기

print('탐색 끝!')

