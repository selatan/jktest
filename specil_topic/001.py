#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests,xlrd, xlwt,json,time
from xlutils.copy import  copy

host='170.16.15.79'
excel1=xlrd.open_workbook('TEST\salesAPP1.xlsx')#打开excel文件
sheet1=excel1.sheet_by_index(0)#打开第一个sheet
nrows=sheet1.nrows#第一个sheet总行数
file=xlwt.Workbook(encoding='utf-8')#新增一个文件夹
file=copy(excel1)#复制
sheetnew=file.get_sheet(0)#新文件的第一个sheet

for i in range(1,3):#按行循环
    url1=host+"?"+sheet1.cell(i,1).value
    params1=sheet1.cell(i,3).value.encode('utf-8')
    j=json.dumps(params1)
    if sheet1.cell(i,2).value=='get':
        r=requests.get(url=url1,params=j)
    elif sheet1.cell(i,2).value=='post':
        r=requests.post(url=url1,data=j)
    elif sheet1.cell(i,2).value=='put':
        r=requests.put(url=url1,data=j)
    elif sheet1.cell(i,2).value=='delete':
        r=requests.delete(url=url1)
    a=r.text
    b=json.loads(a)
    c=b['statusCode']
    sheetnew.write(i,5,a)
    print(i+1,a)
fileName = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
print(fileName)
file.save(fileName+'.xls')
