#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install matplotlib')


# In[2]:


get_ipython().system('pip install flask')


# In[3]:


get_ipython().system('pip install opencv-python')


# In[ ]:





# In[1]:


from flask import Flask, request # flask 서버구축용
import cv2 #영상처리용 opencv
import io #파일 입출력용
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model # 저장된 모델 로딩용


# In[ ]:


app=Flask(__name__) # 플라스크 서버 객체 생성

model=load_model("keras_model.h5") # 모델 로딩

# 사용자 요청을 처리하기 위한 라우터 설정
@app.route('/fileUpload', methods=['POST'])


def fileUpload() :
    if request.method == 'POST':
        f=request.files['image'] # 요청된 객체안의 파일 데이터 꺼내기
        bytes_file=io.BytesIO() # byte단위로 저장할 객체 생성
        f.save(bytes_file) #byte단위로 데이터 저장
        data=np.fromstring(bytes_file.getvalue(),dtype=np.uint8) # numpy로 변경
        print(data.shape)
        
        img=cv2.imdecode(data,1) # 1-> 컬러사진 옵션
        img_rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB) #BGR -> RGB
        display(plt.imshow(img_rgb)) # matplotlib을 이용해서 사진을 그린다
        plt.show() # 그려진 그림을 보여준다
        
        # 티쳐블머신에서 진행한 스케일링 작업 전처리
        img_scaled=(np.array(img_rgb,dtype=np.float32)/127.0)-1
        
    
       
        # 모델예측
        pre = model.predict(img_scaled.reshape(1,224,244,3))
        i = np.argmax(pre) # 3개의 확률정보중 가장 큰 인덱스 찾기
        
        if i == 0:
            result="마이크"
        elif i == 1:
            result="과자"
        elif i == 2:
            result="리모콘"
            
        
    return "당신이 업로드한 사진은{}입니다".format(result)

app.run(host='59.0.236.2',port=8888) # 서버구동


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




