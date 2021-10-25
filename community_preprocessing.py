# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 21:57:12 2021

@author: user
"""

import pandas as pd
import re

news = pd.read_csv('C:/Users/user/Desktop/뉴스/종목토론실_데이터/삼성전자_종목토론실.csv')


news= news.drop(['Unnamed: 0'],axis=1)

news = news.reset_index(drop=False)

news = news.drop(['index'],axis=1)

emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags=re.UNICODE)

#분석에 어긋나는 불용어구 제외 (특수문자, 의성어)
han = re.compile(r'[ㄱ-ㅎㅏ-ㅣ!?~,".\n\r#\ufeff\u200d]')

comment_list = []
for i in range(len(news)):
    comment_list.append(news['제목'].iloc[i])
    


comment_result = []

for i in comment_list:
    #tokens = re.sub(emoji_pattern,"",i)
    tokens = re.sub(han,"",tokens)
    comment_result.append(tokens)
    
for i in range(len(news)):
    news['제목'][i]= comment_result[i]
    
    
    
news['time']=None


for i in range(len(news)):
    news['time'][i] = news['날짜'][i][12:]
    news['날짜'][i] = news['날짜'][i][:11]
    
for i in range(len(news)):
    news['날짜'][i]= news['날짜'][i].replace('.','-')
    
news['날짜'].head()
    
news['timing']=None

for i in range(len(news)):
    if news['time'][i][1:2] == '9':
        pass
    elif news['time'][i][1:2] == '8':
        pass
    elif news['time'][i][0:2] == '10':
        pass
    elif news['time'][i][0:2] == '11':
        pass
    elif news['time'][i][0:2] == '12':
        pass
    elif news['time'][i][0:2] == '13':
        pass
    elif news['time'][i][0:2] == '14':
        pass
    else:
        news['timing'][i]='내일'
        
news['날짜'] = pd.to_datetime(news['날짜'])

from datetime import datetime, timedelta
news['new_date'] =None

for i in range(len(news)):
    if news['timing'][i] =='내일':
        news['new_date'][i] = news['날짜'][i] + timedelta(days=1)
    else:
        news['new_date'][i] = news['날짜'][i]



for i in range(len(news)):
    news['new_date'][i] = news['new_date'][i].strftime('%Y-%m-%d')
    
news= news.sort_values(by='new_date')

result_news=news[['new_date','제목']]

result_news.columns=['date','title']


import FinanceDataReader as fdr

stock_price=fdr.DataReader('005930','20180101','20201231')

stock_price['date']= None


for i in range(len(stock_price)):
    stock_price['date'][i] = stock_price.index[i]
    stock_price['date'][i] = stock_price['date'][i].strftime('%Y-%m-%d')


news_stock = pd.merge(result_news,stock_price,how='inner',on='date')


news_stock.to_csv('C:/Users/user/Desktop/뉴스/종목토론실_데이터/삼성전자_종목토론실_전처리완료.csv')


##################sk
news = pd.read_csv('C:/Users/user/Desktop/뉴스/종목토론실_데이터/sk_종목토론실.csv')


news= news.drop(['Unnamed: 0'],axis=1)

news = news.reset_index(drop=False)

news = news.drop(['index'],axis=1)

emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags=re.UNICODE)

#분석에 어긋나는 불용어구 제외 (특수문자, 의성어)
han = re.compile(r'[ㄱ-ㅎㅏ-ㅣ!?~,".\n\r#\ufeff\u200d]')

comment_list = []
for i in range(len(news)):
    comment_list.append(news['제목'].iloc[i])
    


comment_result = []

for i in comment_list:
    #tokens = re.sub(emoji_pattern,"",i)
    tokens = re.sub(han,"",tokens)
    comment_result.append(tokens)
    
for i in range(len(news)):
    news['제목'][i]= comment_result[i]
    
    
    
news['time']=None


for i in range(len(news)):
    news['time'][i] = news['날짜'][i][12:]
    news['날짜'][i] = news['날짜'][i][:11]
    
for i in range(len(news)):
    news['날짜'][i]= news['날짜'][i].replace('.','-')
    
news['날짜'].head()
    
news['timing']=None

for i in range(len(news)):
    if news['time'][i][1:2] == '9':
        pass
    elif news['time'][i][1:2] == '8':
        pass
    elif news['time'][i][0:2] == '10':
        pass
    elif news['time'][i][0:2] == '11':
        pass
    elif news['time'][i][0:2] == '12':
        pass
    elif news['time'][i][0:2] == '13':
        pass
    elif news['time'][i][0:2] == '14':
        pass
    else:
        news['timing'][i]='내일'
        
news['날짜'] = pd.to_datetime(news['날짜'])

from datetime import datetime, timedelta
news['new_date'] =None

for i in range(len(news)):
    if news['timing'][i] =='내일':
        news['new_date'][i] = news['날짜'][i] + timedelta(days=1)
    else:
        news['new_date'][i] = news['날짜'][i]



for i in range(len(news)):
    news['new_date'][i] = news['new_date'][i].strftime('%Y-%m-%d')
    
news= news.sort_values(by='new_date')

result_news=news[['new_date','제목']]

result_news.columns=['date','title']


import FinanceDataReader as fdr

stock_price=fdr.DataReader('000660','20180101','20201231')

stock_price['date']= None


for i in range(len(stock_price)):
    stock_price['date'][i] = stock_price.index[i]
    stock_price['date'][i] = stock_price['date'][i].strftime('%Y-%m-%d')


news_stock = pd.merge(result_news,stock_price,how='inner',on='date')


news_stock.to_csv('C:/Users/user/Desktop/뉴스/종목토론실_데이터/sk_종목토론실_전처리완료.csv')


##################셀트리온
news = pd.read_csv('C:/Users/user/Desktop/뉴스/종목토론실_데이터/셀트리온_종목토론실.csv')


news= news.drop(['Unnamed: 0'],axis=1)

news = news.reset_index(drop=False)

news = news.drop(['index'],axis=1)

emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags=re.UNICODE)

#분석에 어긋나는 불용어구 제외 (특수문자, 의성어)
han = re.compile(r'[ㄱ-ㅎㅏ-ㅣ!?~,".\n\r#\ufeff\u200d]')

comment_list = []
for i in range(len(news)):
    comment_list.append(news['제목'].iloc[i])
    


comment_result = []

for i in comment_list:
    #tokens = re.sub(emoji_pattern,"",i)
    tokens = re.sub(han,"",tokens)
    comment_result.append(tokens)
    
for i in range(len(news)):
    news['제목'][i]= comment_result[i]
    
    
    
news['time']=None


for i in range(len(news)):
    news['time'][i] = news['날짜'][i][12:]
    news['날짜'][i] = news['날짜'][i][:11]
    
for i in range(len(news)):
    news['날짜'][i]= news['날짜'][i].replace('.','-')
    
news['날짜'].head()
    
news['timing']=None

for i in range(len(news)):
    if news['time'][i][1:2] == '9':
        pass
    elif news['time'][i][1:2] == '8':
        pass
    elif news['time'][i][0:2] == '10':
        pass
    elif news['time'][i][0:2] == '11':
        pass
    elif news['time'][i][0:2] == '12':
        pass
    elif news['time'][i][0:2] == '13':
        pass
    elif news['time'][i][0:2] == '14':
        pass
    else:
        news['timing'][i]='내일'
        
news['날짜'] = pd.to_datetime(news['날짜'])

from datetime import datetime, timedelta
news['new_date'] =None

for i in range(len(news)):
    if news['timing'][i] =='내일':
        news['new_date'][i] = news['날짜'][i] + timedelta(days=1)
    else:
        news['new_date'][i] = news['날짜'][i]



for i in range(len(news)):
    news['new_date'][i] = news['new_date'][i].strftime('%Y-%m-%d')
    
news= news.sort_values(by='new_date')

result_news=news[['new_date','제목']]

result_news.columns=['date','title']


import FinanceDataReader as fdr

stock_price=fdr.DataReader('000660','20180101','20201231')

stock_price['date']= None


for i in range(len(stock_price)):
    stock_price['date'][i] = stock_price.index[i]
    stock_price['date'][i] = stock_price['date'][i].strftime('%Y-%m-%d')


news_stock = pd.merge(result_news,stock_price,how='inner',on='date')


news_stock.to_csv('C:/Users/user/Desktop/뉴스/종목토론실_데이터/셀트리온_종목토론실_전처리완료.csv')

##################현대차
news = pd.read_csv('C:/Users/user/Desktop/뉴스/종목토론실_데이터/현대차_종목토론실.csv')


news= news.drop(['Unnamed: 0'],axis=1)

news = news.reset_index(drop=False)

news = news.drop(['index'],axis=1)

emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags=re.UNICODE)

#분석에 어긋나는 불용어구 제외 (특수문자, 의성어)
han = re.compile(r'[ㄱ-ㅎㅏ-ㅣ!?~,".\n\r#\ufeff\u200d]')

comment_list = []
for i in range(len(news)):
    comment_list.append(news['제목'].iloc[i])
    


comment_result = []

for i in comment_list:
    #tokens = re.sub(emoji_pattern,"",i)
    tokens = re.sub(han,"",tokens)
    comment_result.append(tokens)
    
for i in range(len(news)):
    news['제목'][i]= comment_result[i]
    
    
    
news['time']=None


for i in range(len(news)):
    news['time'][i] = news['날짜'][i][12:]
    news['날짜'][i] = news['날짜'][i][:11]
    
for i in range(len(news)):
    news['날짜'][i]= news['날짜'][i].replace('.','-')
    
news['날짜'].head()
    
news['timing']=None

for i in range(len(news)):
    if news['time'][i][1:2] == '9':
        pass
    elif news['time'][i][1:2] == '8':
        pass
    elif news['time'][i][0:2] == '10':
        pass
    elif news['time'][i][0:2] == '11':
        pass
    elif news['time'][i][0:2] == '12':
        pass
    elif news['time'][i][0:2] == '13':
        pass
    elif news['time'][i][0:2] == '14':
        pass
    else:
        news['timing'][i]='내일'
        
news['날짜'] = pd.to_datetime(news['날짜'])

from datetime import datetime, timedelta
news['new_date'] =None

for i in range(len(news)):
    if news['timing'][i] =='내일':
        news['new_date'][i] = news['날짜'][i] + timedelta(days=1)
    else:
        news['new_date'][i] = news['날짜'][i]



for i in range(len(news)):
    news['new_date'][i] = news['new_date'][i].strftime('%Y-%m-%d')
    
news= news.sort_values(by='new_date')

result_news=news[['new_date','제목']]

result_news.columns=['date','title']


import FinanceDataReader as fdr

stock_price=fdr.DataReader('000660','20180101','20201231')

stock_price['date']= None


for i in range(len(stock_price)):
    stock_price['date'][i] = stock_price.index[i]
    stock_price['date'][i] = stock_price['date'][i].strftime('%Y-%m-%d')


news_stock = pd.merge(result_news,stock_price,how='inner',on='date')


news_stock.to_csv('C:/Users/user/Desktop/뉴스/종목토론실_데이터/현대차_종목토론실_전처리완료.csv')
