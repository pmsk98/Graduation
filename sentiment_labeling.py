# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 06:59:46 2021

@author: user
"""

import codecs

positive = [] 
negative = [] 
posneg = [] 
pos = codecs.open("C:/Users/user/Desktop/뉴스/positive_words_self.txt", 'rb', encoding='UTF-8') 

while True: 
    line = pos.readline() 
    line = line.replace('\n', '')
    
    if not line: break
        
    positive.append(line) 
    posneg.append(line) 
    
     
        
pos.close() 

neg = codecs.open("C:/Users/user/Desktop/뉴스/negative_words_self.txt", 'rb', encoding='UTF-8') 
while True: 
    line = neg.readline() 
    line = line.replace('\n', '')
    if not line: break
    
    negative.append(line) 
    posneg.append(line) 
    
neg.close()


import pandas as pd
import numpy as np


j = 0
label = [0] * len(samsung_2018)

my_dic = {"text":[], "label":label}

texts = samsung_2018.text
texts = texts.str.replace('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…\"\“▲》◆▶◇■]','')
texts = texts.str.replace('[\n\r\t\\\]','')
texts = texts.reset_index().drop('index',1).text.str[:1000]

for df in range(len(samsung_2018)):    
    txt_data = texts[df]
    
    my_dic['text'].append(txt_data) 

    for i in range(len(posneg)): 
        posflag = False 
        negflag = False 

        if i < (len(positive)-1): 
            # print(title_data.find(posneg[i])) 
            if txt_data.find(posneg[i]) != -1: 
                posflag = True 

                print(i, "positive?","테스트 : ",txt_data.find(posneg[i]),"비교단어 : ", posneg[i], "인덱스 : ", i) 
                break 

        if i > (len(positive)-2): 
            if txt_data.find(posneg[i]) != -1: 
                negflag = True 
                print(i, "negative?","테스트 : ",txt_data.find(posneg[i]),"비교단어 : ", posneg[i], "인덱스 : ", i) 
                break 

    if posflag == True: 
        label[j] = 1 
        # print("positive", j) 

    elif negflag == True: 
        label[j] = -1 
        # print("negative", j) 

    elif negflag == False and posflag == False: 
        label[j] = -1 
        # print("objective", j) 

    j = j + 1 


samsung_2018['label'] = None


for i in range(len(samsung_2018)):
    samsung_2018['label'][i]=label[i]


label
samsung_2018
