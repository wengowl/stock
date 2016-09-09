#coding: UTF-8
import tushare as ts
import pandas as pd
stock_basics=ts.get_stock_basics()#获取所有上市公司的股票基本信息
all_stock_code=stock_basics.index.values#所有股票代码的arrary

report2014=ts.get_report_data(2014,2).drop_duplicates()
report2015=ts.get_report_data(2015,2).drop_duplicates()
report2016=ts.get_report_data(2016,2).drop_duplicates()

# report2014=pd.read_csv('data/report/report2014_2.csv').drop_duplicates()
# report2015=pd.read_csv('data/report/report2015_2.csv').drop_duplicates()
# report2016=pd.read_csv('data/report/report2016_2.csv').drop_duplicates()
print report2014.columns
print report2015.columns
print report2016.columns

for i in all_stock_code:
    print "^^^ %s"%i
    try:
        roecomp(i)
        profitcomp(i)
    except Exception,e:
        #print str(e)
        continue 
    
def roecomp(i):
    if report2014.ix[report2014.code==i,:1].empty==False:
        if report2015.ix[report2015.code==i,:1].empty==False:
            if report2016.ix[report2016.code==i,:1].empty==False:                
                if report2014.ix[report2014.code==i,:1].roe <= report2015.ix[report2015.code==i,:1].roe:                    
                    if report2015.ix[report2015.code==i ,:1].roe <= report2016.ix[report2016.code==i,:1].roe:
                         print stock_basics.ix[i]

def profitcomp(i):
    if report2014.ix[report2014.code==i,:1].empty==False:
        if report2015.ix[report2015.code==i,:1].empty==False:
            if report2016.ix[report2016.code==i,:1].empty==False:
                # try:
                #     print report2014.ix[report2014.code==i,:1].net_profits
                #     print report2015.ix[report2015.code==i,:1].net_profitsroe 
                #     print report2016.ix[report2016.code==i,:1].net_profits
                # except Exception,e:
                #     #print str(e)
                #     continue 
                if report2014.ix[report2014.code==i,:1].net_profits <= report2015.ix[report2015.code==i,:1].net_profits:
                    
                    if report2015.ix[report2015.code==i ,:1].net_profits <= report2016.ix[report2016.code==i,:1].net_profits:
                         print stock_basics.ix[i]
    