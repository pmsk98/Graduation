# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 04:05:47 2021

@author: user
"""

import pandas as pd
from konlpy.tag import Okt
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import re
## FastText
import fasttext
import fasttext.util
from gensim import models

import datetime
from collections import Counter
import sys
import warnings

samsung_2018 = pd.read_csv('C:/Users/user/Desktop/뉴스/2018_maeil_samsung.csv')
samsung_2019 = pd.read_csv('C:/Users/user/Desktop/뉴스/2019_maeil_samsung.csv')
samsung_2020 = pd.read_csv('C:/Users/user/Desktop/뉴스/2020_maeil_samsung.csv')



samsung_news = pd.concat([samsung_2018,samsung_2019,samsung_2020])

samsung_news=samsung_news.reset_index(drop=True)





with open('C:/Users/user/Desktop/뉴스/감성사전/KOSELF_pos.txt', encoding='utf-8') as pos:
    positive = pos.readlines()
positive = [pos.replace('\n', '') for pos in positive]
with open('C:/Users/user/Desktop/뉴스/감성사전/KOSELF_neg.txt', encoding='utf-8') as neg:
    negative = neg.readlines()
negative = [neg.replace('\n', '') for neg in negative]


#cosine 유사도 측정
ko_model = models.fasttext.load_facebook_model('C:/Users/user/Desktop/뉴스/cc.ko.300.bin')



limit_number = 15000
sys.setrecursionlimit(limit_number)


#####긍정####
pos_samsung = pd.DataFrame(columns=['date', 'news_num', 'KOSELF_pos_word', 'news_word', 'cosine_similarity', 'frequency'])   

# KOSELF_pos와의 Cosine Similarity 계산
for x in range(len(samsung_news['Tokenization'])):
    news_num = x+1
    for y in range(len(positive)):
        for z in range(len(list(set(samsung_news['Tokenization'][x].split())))):
            if (ko_model.wv.similarity(positive[y], list(set(samsung_news['Tokenization'][x].split()))[z]) >= 0.5) and (ko_model.wv.similarity(positive[y], list(set(samsung_news['Tokenization'][x].split()))[z]) != 1.0):
                freq = 0
                for w in range(len(samsung_news['Tokenization'][x].split())):
                    if samsung_news['Tokenization'][x].split()[w] == list(set(samsung_news['Tokenization'][x].split()))[z]:
                        freq += 1
                data = {
                    'date': samsung_news['date'][x],
                    'news_num': news_num,
                    'KOSELF_pos_word': positive[y],
                    'news_word': list(set(samsung_news['Tokenization'][x].split()))[z],
                    'cosine_similarity': ko_model.wv.similarity(positive[y], list(set(samsung_news['Tokenization'][x].split()))[z]),
                    'frequency': freq
                    }
                pos_samsung = pos_samsung.append(data, ignore_index=True)
                print("***{0} Cosine Similarity between <{1}> & <{2}> : {3}".format(samsung_news['date'][x], positive[y], list(set(samsung_news['Tokenization'][x].split()))[z], ko_model.wv.similarity(positive[y], list(set(samsung_news['Tokenization'][x].split()))[z])))

###부정###
neg_samsung = pd.DataFrame(columns=['date', 'news_num', 'KOSELF_neg_word', 'news_word', 'cosine_similarity', 'frequency'])   

# KOSELF_neg와의 Cosine Similarity 계산
for x in range(len(samsung_news['Tokenization'])):
    news_num = x+1
    for y in range(len(negative)):
        for z in range(len(list(set(samsung_news['Tokenization'][x].split())))):
            if (ko_model.wv.similarity(negative[y], list(set(samsung_news['Tokenization'][x].split()))[z]) >= 0.5) and (ko_model.wv.similarity(negative[y], list(set(samsung_news['Tokenization'][x].split()))[z]) != 1.0):
                freq = 0
                for w in range(len(samsung_news['Tokenization'][x].split())):
                    if samsung_news['Tokenization'][x].split()[w] == list(set(samsung_news['Tokenization'][x].split()))[z]:
                        freq += 1
                data = {
                    'date': samsung_news['date'][x],
                    'news_num': news_num,
                    'KOSELF_neg_word': negative[y],
                    'news_word': list(set(samsung_news['Tokenization'][x].split()))[z],
                    'cosine_similarity': ko_model.wv.similarity(negative[y], list(set(samsung_news['Tokenization'][x].split()))[z]),
                    'frequency': freq
                    }
                neg_samsung = neg_samsung.append(data, ignore_index=True)
                print("***{0} Cosine Similarity between <{1}> & <{2}> : {3}".format(samsung_2018['date'][x], negative[y], list(set(samsung_news['Tokenization'][x].split()))[z], ko_model.wv.similarity(negative[y], list(set(samsung_news['Tokenization'][x].split()))[z])))


pos_samsung_2018['news_word'][3]

a = list(set(list(pos_samsung_2018['news_word'])))

b = list(set(list(pos_samsung_2018[pos_samsung_2018['cosine_similarity']>=0.8]['news_word'])))

b


##감성지수###

for i in range(len(corp_list)):
    globals()[corp_list[i]]['Positive_Score'] = 0
    globals()[corp_list[i]]['Negative_Score'] = 0
    globals()[corp_list[i]]['Ratio'] = 0.1
    globals()[corp_list[i]]['NSI'] = 0.1
    
    for j in range(len(globals()[corp_list[i]])):
        pos_score = 0 ; neg_score = 0
        
        for k in range(len(globals()[corp_list[i]]['Tokenization'][j].split())):
            if globals()[corp_list[i]]['Tokenization'][j].split()[k] in positive:
                pos_score += 1
            elif globals()[corp_list[i]]['Tokenization'][j].split()[k] in negative:
                neg_score += 1
            else:
                pass
        
        globals()[corp_list[i]]['Positive_Score'][j] = pos_score
        globals()[corp_list[i]]['Negative_Score'][j] = neg_score
        
        # 긍정과 부정의 비율
        if (pos_score==0) and (neg_score==0):
            globals()[corp_list[i]]['Ratio'][j] = 0.5   # 둘 다 0일 경우에는 긍정으로 가정
        else:
            globals()[corp_list[i]]['Ratio'][j] = pos_score / (pos_score + neg_score)
        

        
        # 뉴스심리지수(NSI) 계산
        if (pos_score==0) and (neg_score==0):
            globals()[corp_list[i]]['NSI'][j] = 101
        else:
            globals()[corp_list[i]]['NSI'][j] = (pos_score - neg_score) / (pos_score + neg_score) * 100 + 100




samsung_2018.columns


samsung_2018[['date','title']].head()
samsung_2018['text'].head()
