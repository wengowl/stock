#coding: UTF-8
import tushare as ts
stock_basics=ts.get_stock_basics()#获取所有上市公司的股票基本信息
all_stock_code=stock_basics.index.values#所有股票代码的arrary
