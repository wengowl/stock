stock_basics 股票列表

code,代码
name,名称
industry,所属行业
area,地区
pe,市盈率
outstanding,流通股本
totals,总股本(万)
totalAssets,总资产(万)
liquidAssets,流动资产
fixedAssets,固定资产
reserved,公积金
reservedPerShare,每股公积金
eps,每股收益
bvps,每股净资
pb,市净率
timeToMarket,上市日期


report_data 业绩报表（主表）

code,代码
name,名称
eps,每股收益
eps_yoy,每股收益同比(%)
bvps,每股净资产
roe,净资产收益率(%)
epcf,每股现金流量(元)
net_profits,净利润(万元)
profits_yoy,净利润同比(%)
distrib,分配方案
report_date,发布日期

profit_data 盈利报表
code,代码
name,名称
roe,净资产收益率(%)
net_profit_ratio,净利率(%)
gross_profit_rate,毛利率(%)
net_profits,净利润(万元)
eps,每股收益
business_income,营业收入(百万元)
bips,每股主营业务收入(元)

营运能力opetation_data

按年度、季度获取营运能力数据，结果返回的数据属性说明如下：

code,代码
name,名称
arturnover,应收账款周转率(次)
arturndays,应收账款周转天数(天)
inventory_turnover,存货周转率(次)
inventory_days,存货周转天数(天)
currentasset_turnover,流动资产周转率(次)
currentasset_days,流动资产周转天数(天)


成长能力growth_data

按年度、季度获取成长能力数据，结果返回的数据属性说明如下：

code,代码
name,名称
mbrg,主营业务收入增长率(%)
nprg,净利润增长率(%)
nav,净资产增长率
targ,总资产增长率
epsg,每股收益增长率
seg,股东权益增长率



偿债能力

按年度、季度获取偿债能力数据，结果返回的数据属性说明如下：

code,代码
name,名称
currentratio,流动比率
quickratio,速动比率
cashratio,现金比率
icratio,利息支付倍数
sheqratio,股东权益比率
adratio,股东权益增长率

调用方法：

#获取2014年第3季度的偿债能力数据
ts.get_debtpaying_data(2014,3)




现金流量

按年度、季度获取现金流量数据，结果返回的数据属性说明如下：

code,代码
name,名称
cf_sales,经营现金净流量对销售收入比率
rateofreturn,资产的经营现金流量回报率
cf_nm,经营现金净流量与净利润的比率
cf_liabilities,经营现金净流量对负债比率
cashflowratio,现金流量比率

调用方法：

#获取2014年第3季度的现金流量数据
ts.get_cashflow_data(2014,3)



业绩预告

按年度、季度获取业绩预告数据，接口提供从1998年以后每年的业绩预告数据，需指定年度、季度两个参数。数据在获取的过程中，会打印进度信息(下同)。

参数说明：

    year:int 年度 e.g:2014
    quarter:int 季度 :1、2、3、4，只能输入这4个季度

结果返回的数据属性说明如下：

code,代码
name,名称
type,业绩变动类型【预增、预亏等】
report_date,发布日期
pre_eps,上年同期每股收益
range,业绩变动范围

调用方法：

#获取2014年中报的业绩预告数据
ts.forecast_data(2014,2)



