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
#삼성전자
samsung_2018 = pd.read_csv('C:/Users/user/Desktop/뉴스/2018_maeil_samsung.csv')
samsung_2019 = pd.read_csv('C:/Users/user/Desktop/뉴스/2019_maeil_samsung.csv')
samsung_2020 = pd.read_csv('C:/Users/user/Desktop/뉴스/2020_maeil_samsung.csv')
#sk하이닉스
sk_2018 = pd.read_csv('C:/Users/user/Desktop/뉴스/2018_maeil_sk.csv')
sk_2019 = pd.read_csv('C:/Users/user/Desktop/뉴스/2019_maeil_sk.csv')
sk_2020 = pd.read_csv('C:/Users/user/Desktop/뉴스/2020_maeil_sk.csv')

#셀트리온
cell_2018 = pd.read_csv('C:/Users/user/Desktop/뉴스/2018_maeil_celltrion.csv')
cell_2019 = pd.read_csv('C:/Users/user/Desktop/뉴스/2019_maeil_celltrion.csv')
cell_2020 = pd.read_csv('C:/Users/user/Desktop/뉴스/2020_maeil_celltrion.csv')

#현대차
hyundai_2018 = pd.read_csv('C:/Users/user/Desktop/뉴스/2018_maeil_hyundai.csv')
hyundai_2019 = pd.read_csv('C:/Users/user/Desktop/뉴스/2019_maeil_hyundai.csv')
hyundai_2020 = pd.read_csv('C:/Users/user/Desktop/뉴스/2020_maeil_hyundai.csv')

#lg 화학
lg_2018 = pd.read_csv('C:/Users/user/Desktop/뉴스/2018_maeil_hyundai.csv')
lg_2019 = pd.read_csv('C:/Users/user/Desktop/뉴스/2019_maeil_hyundai.csv')
lg_2020 = pd.read_csv('C:/Users/user/Desktop/뉴스/2020_maeil_hyundai.csv')


#삼성전자
samsung_news = pd.concat([samsung_2018,samsung_2019,samsung_2020])
samsung_news=samsung_news.reset_index(drop=True)

#sk하이닉스
sk_news = pd.concat([sk_2018,sk_2019,sk_2020])
sk_news=sk_news.reset_index(drop=True)


#셀트리온
celltrion_news = pd.concat([cell_2018,cell_2019,cell_2020])
celltrion_news=celltrion_news.reset_index(drop=True)
#현대차
hyundai_news = pd.concat([hyundai_2018,hyundai_2019,hyundai_2020])
hyundai_news=hyundai_news.reset_index(drop=True)
#lg화학
lg_news = pd.concat([lg_2018,lg_2019,lg_2020])
lg_news=lg_news.reset_index(drop=True)


##############삼성####################
j = 0
label = [0] * len(samsung_news)

my_dic = {"text":[], "label":label}

texts = samsung_news.text
texts = texts.str.replace('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…\"\“▲》◆▶◇■]','')
texts = texts.str.replace('[\n\r\t\\\]','')
texts = texts.reset_index().drop('index',1).text.str[:1000]

samsung_news['text'] = texts

for df in range(len(samsung_news)):    
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
        label[j] = 1 
        # print("objective", j) 

    j = j + 1 




samsung_news['label'] = None


for i in range(len(samsung_news)):
    samsung_news['label'][i]=label[i]

###################sk하이닉스################
j = 0
label = [0] * len(sk_news)

my_dic = {"text":[], "label":label}


texts = sk_news.text
texts = texts.str.replace('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…\"\“▲》◆▶◇■]','')
texts = texts.str.replace('[\n\r\t\\\]','')
texts = texts.reset_index().drop('index',1).text.str[:1000]


sk_news['text'] =texts

for df in range(len(sk_news)):    
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
        label[j] = 1 
        # print("objective", j) 

    j = j + 1 




sk_news['label'] = None


for i in range(len(sk_news)):
    sk_news['label'][i]=label[i]




##############셀트리온###########

j = 0
label = [0] * len(celltrion_news)

my_dic = {"text":[], "label":label}


texts = celltrion_news.text
texts = texts.str.replace('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…\"\“▲》◆▶◇■]','')
texts = texts.str.replace('[\n\r\t\\\]','')
texts = texts.reset_index().drop('index',1).text.str[:1000]


celltrion_news['text'] =texts

for df in range(len(celltrion_news)):    
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
        label[j] = 1 
        # print("objective", j) 

    j = j + 1 




celltrion_news['label'] = None


for i in range(len(celltrion_news)):
    celltrion_news['label'][i]=label[i]




##############현대차###########

j = 0
label = [0] * len(hyundai_news)

my_dic = {"text":[], "label":label}


texts = hyundai_news.text
texts = texts.str.replace('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…\"\“▲》◆▶◇■]','')
texts = texts.str.replace('[\n\r\t\\\]','')
texts = texts.reset_index().drop('index',1).text.str[:1000]


hyundai_news['text'] =texts

for df in range(len(hyundai_news)):    
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
        label[j] = 1 
        # print("objective", j) 

    j = j + 1 




hyundai_news['label'] = None


for i in range(len(hyundai_news)):
    hyundai_news['label'][i]=label[i]



##############LG화학###########

j = 0
label = [0] * len(lg_news)

my_dic = {"text":[], "label":label}


texts = lg_news.text
texts = texts.str.replace('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…\"\“▲》◆▶◇■]','')
texts = texts.str.replace('[\n\r\t\\\]','')
texts = texts.reset_index().drop('index',1).text.str[:1000]


lg_news['text'] =texts

for df in range(len(lg_news)):    
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
        label[j] = 1 
        # print("objective", j) 

    j = j + 1 




lg_news['label'] = None


for i in range(len(lg_news)):
    lg_news['label'][i]=label[i]


