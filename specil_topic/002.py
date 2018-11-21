# -*- coding:utf-8 -*-

import requests
import json
import urllib.request
import urllib3


url1 = "http://172.16.15.79:8085/action/topic/detail?topicId=560916260859183104&isCache=false"

url2 = "http://172.16.15.79:8085/action/topic/list"

header = {
    "Content-Type":'application/json',
    'Cookie':'CASTGC=TGT-2043-uRhfc399qt1vDFEsuVbwpzUBdDbeXZ9CtPBTagcdrd7HxFqVp0-dev-sso.tcjk.com; JSESSIONID=395B02EC28BBD25BCEC184A224625F58'
}
#获取专题详情-get
response1 = requests.get(url1,headers = header)
print(response1.text)

content = {'start': '1542729600000', 'end': "1542816000000", 'topicName': "", 'page': 1, 'size': 10}
#搜索专题-post
response2 = requests.post(url2,data=json.dumps(content),headers = header)
print(response2.text)
