# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 18:34:21 2021

@author: user
"""
import glob
import os
import pandas as pd
import  talib
import numpy as np


path ='C:/Users/user/Desktop/뉴스/5stock_updown_kobert'


file_list =os.listdir(path)

df= []

len(df)

for file in file_list:
    path = 'C:/Users/user/Desktop/뉴스/5stock_updown_kobert'
    
    df.append(pd.read_csv(path+"/"+file))
    


for i in range(len(df)):
    df[i]=df[i].drop(['Unnamed: 0'],axis=1)



#새로운 라벨 추가(e -> 인덱스 번호)
for i in range(0,5):
    df[i]['position']=None
    
                   
#randomforest
for i in range(0,5):
    for e in df[i].index:
        try:
            if df[i]['predict'][e]+df[i]['predict'][e+1]==0:
                df[i]['position'][e+1]='no action'
            elif df[i]['predict'][e]+df[i]['predict'][e+1]==2:
                df[i]['position'][e+1]='holding'
            elif df[i]['predict'][e] > df[i]['predict'][e+1]:
                df[i]['position'][e+1]='sell'
            else:
                df[i]['position'][e+1]='buy'
        except:
            pass

#첫날 position이 holding일 경우 buy로 변경
for i in range(0,5):
    if df[i]['position'][df[i].index[0]]=='holding':
        df[i]['position'][df[i].index[0]]='buy'
    elif df[i]['position'][df[i].index[0]]=='sell':
        df[i]['position'][df[i].index[0]]='buy'
    else:
        print(i)


#강제 청산
for i in range(0,5):
    for e in df[i].index[-1:]:
        if df[i]['position'][e]=='holding':
            df[i]['position'][e]='sell'
        elif df[i]['position'][e]=='buy':
            df[i]['position'][e]='sell'
        elif df[i]['position'][e]=='no action':
            df[i]['position'][e]='sell'
        else:
            print(i)



for i in range(0,5):
    df[i]['profit']=None
    
#다음날 시가를 가져오게 생성
for i in range(0,5):
    for e in df[i].index:
        try:
            if df[i]['position'][e]=='buy':
                df[i]['profit'][e]=df[i]['Open'][e+1]
            elif df[i]['position'][e]=='sell':
                df[i]['profit'][e]=df[i]['Open'][e+1]
            else:
                print(i)
        except:
            pass



for i in range(0,5):
    for e in df[i].index[-1:]:
        if df[i]['position'][e]=='sell':
            df[i]['profit'][e]=df[i]['Open'][e]
        
####

buy_label=[]
for i in range(0,5):
    buy_position=df[i]['position']=='buy'
    buy_label.append(df[i][buy_position])
    
sell_label=[]
for i in range(0,5):
    sell_position=df[i]['position']=='sell'
    sell_label.append(df[i][sell_position])    


buy=[]
sell=[]
for i in range(0,5):
    buy.append(buy_label[i]['Open'].reset_index(drop=True))
    sell.append(sell_label[i]['Open'].reset_index(drop=True))
    
  
profit_2=[]    
for i in range(0,5):
    profit_2.append((sell[i]-(0.0015*sell[i]))-buy[i])
  

for i in range(0,5):
    df[i]['profit_2']=None
    

#profit 결측치 처리
for i in range(0,5):
    profit_2[i]=profit_2[i].dropna()
    
    
#profit_2 sell에 해당하는 행에 값 넣기
for tb, pf in zip(df, profit_2):
    total_idx = tb[tb['position'] == 'sell'].index
    total_pf_idx = pf.index
    for idx, pf_idx in zip(total_idx, total_pf_idx):
        tb.loc[idx, 'profit_2'] = pf[pf_idx]




for i in range(0,5):
    df[i]['profit_cumsum']=None
    
    
    

#profit 누적 합 
for i in range(0,5):
    for e in df[i].index:
        try:
            if df[i]['position'][e]=='holding':
                df[i]['profit_2'][e]=0
            elif df[i]['position'][e]=='no action':
                df[i]['profit_2'][e]=0
            elif df[i]['position'][e]=='buy':
                df[i]['profit_2'][e]=0
            else:
                print(i)
        except:
            pass


#새로운 청산 기준 누적합

for i in range(0,5):
    df[i]['profit_cumsum2']=None    
    
    
for i in range(0,5):
    df[i]['profit_cumsum']=df[i]['profit_2'].cumsum()

profit_2[1]

################# ratio 작성

#ratio 작성
for i in range(0,5):
    profit_2[i]=pd.DataFrame(profit_2[i])

#거래횟수
trade= []

for i in range(0,5):
    trade.append(len(profit_2[i]))
    
#승률


for i in range(0,5):
    profit_2[i]['average']=None

   
for i in range(0,5):
    for e in range(len(profit_2[i])):      
        if profit_2[i]['Open'][e] > 0:
            profit_2[i]['average'][e]='gain'
        else:
            profit_2[i]['average'][e]='loss'
            
for i in range(0,5):
    for e in range(len(profit_2[i])):
        if profit_2[i]['Open'][e] < 0:
            profit_2[i]['Open'][e]=profit_2[i]['Open'][e] * -1
        else:
            print(i)

win=[]
for i in range(0,5):
    try:
        win.append(profit_2[i].groupby('average').size()[0]/len(profit_2[i]))
    except:
        win.append('0')
    
#평균 수익

gain=[]

for i in range(0,5):
    gain.append(profit_2[i].groupby('average').mean())
    

real_gain=[]

for i in range(0,5):
    try:
        real_gain.append(gain[i]['Open'][0])
    except:
        real_gain.append('0')



#평균 손실
loss=[]

for i in range(0,5):
    try:
        loss.append(gain[i]['Open'][1])
    except:
        loss.append('0')

    
loss
#payoff ratio
payoff=[]

for i in range(0,5):
    try:
        payoff.append(gain[i]['Open'][0]/gain[i]['Open'][1])
    except:
        payoff.append('inf')
    
#profit factor

factor_sum=[]

len(factor_sum)
for i in range(0,5):
    factor_sum.append(profit_2[i].groupby('average').sum())

factor=[]

for i in range(0,5):
    try:
        factor.append(factor_sum[i]['Open'][0]/factor_sum[i]['Open'][1])
    except:
        factor.append('0')

#year
year=[]

for i in range(0,5):
    year.append('2020')

#최종 결과물 파일 작성
stock_name=pd.DataFrame({'stock_name':file_list})

stock_name=stock_name.replace('.csv','',regex=True)

year=pd.DataFrame({'year':year})

trade=pd.DataFrame({'No.trades':trade})

win=pd.DataFrame({'Win%':win})

real_gain=pd.DataFrame({'Average gain($)':real_gain})

loss=pd.DataFrame({'Average loss($)':loss})

payoff=pd.DataFrame({'Payoff ratio':payoff})

factor=pd.DataFrame({'Profit factor':factor})

#2020
result =pd.concat([year,stock_name,trade,win,real_gain,loss,payoff,factor],axis=1)

result.to_csv('C:/Users/user/Desktop/뉴스/5stock_updown_kobert/5stock_result_updown_kobert.csv')


result_mean=result.groupby('year').mean()


result_mean.to_csv('C:/Users/user/Desktop/뉴스/5stock_updown_kobert/5stock_result_updown_kobert_평균.csv')

