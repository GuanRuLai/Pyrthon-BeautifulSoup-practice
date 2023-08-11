# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 16:04:32 2022

@author: HP
"""

import requests
from bs4 import BeautifulSoup
url="https://www.taiwanlottery.com.tw"
html=requests.get(url)
sp=BeautifulSoup(html.text,"lxml")
# 找到威力彩的區域
datas=sp.find("div",class_="contents_box02")
# 開獎期數
title=datas.find("span","font_black15").text
print("威力採期數:",title)
# 開獎號碼
nums=datas.find_all("div",class_="ball_tx ball_green")
# 開出順序
print("開出順序:",end=" ") #註：end=" "：末尾不換行+字與字間空格
for i in range(0,6):
    print(nums[i].text,end=" ")
# 大小順序
print("\n大小順序:",end=" ") #註：\n：換行
for i in range(6,12):
    print(nums[i].text,end=" ")
# 第二區
nums1=datas.find("div",class_="ball_red").text
print("\n第二區:",nums1)
