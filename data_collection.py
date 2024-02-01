# -*- coding:utf-8 -*-
import requests
import json
import pandas as pd 
from dotenv import load_dotenv
import os

load_dotenv() # .env 파일 활성화
SEIVICE_KEY = os.getenv('SEIVICE_KEY')
print(SEIVICE_KEY)
# 네이버 주식 차트 pd.concat()
for i in range(1, 3):
    URL = f'http://openapi.seoul.go.kr:8088/{SEIVICE_KEY}/json/tbLnOpendataRtmsV/{1 + (i-1) * 1000}/{i * 1000}/'
    print(URL)
    data = None
for j in range(1,5):
    url = f'http://openapi.seoul.go.kr:8088/{SEIVICE_KEY}/json/tbLnOpendataRtmsV/{1+((j-1)*1000)}/{j*1000}'
    # url = f'http://openapi.seoul.go.kr:8088/{service_key}/json/tbLnOpendataRentV/1/1000/2023/11560'
    print(url)
    req = requests.get(url)
    content = req.json()
    con = content['tbLnOpendataRtmsV']['row']
    result = pd.DataFrame(con)
    data = pd.concat([data, result])
data = data.reset_index(drop=True)
data.head()
