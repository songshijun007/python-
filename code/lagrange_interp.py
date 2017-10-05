#coding:utf-8
#python中用拉格朗日插值法补充缺失值
import pandas as pd
from scipy.interpolate import lagrange#通过scipy引入拉格朗日插值法

inputfile = 'D:\学习\Python_data analysis\chapter4\demo\data\catering_sale.xls'
outputfile = 'D:\学习\Python_data analysis\chapter4\demo\data\sale.xls'

data = pd.read_excel(inputfile)
data[u'销量'][(data[u'销量'] < 400)|(data[u'销量']>5000)] = None#通过四分位、观察法等判断极端值值和缺失值，并且令他为空值再用拉格朗日插值法填补数据

def ployinterp_column(s,n,k=5):
    y = s[list(range(n-k,n))+list(range(n+1,n+1+k))]
    y = y[y.notnull()]
    return lagrange(y.index, list(y))(n)

print(data)

for i in data.columns:
    for j in range(len(data)):
        if (data[i].isnull())[j]:
            data[i][j] = ployinterp_column(data[i],j)

data.to_excel(outputfile)#输出数据以Excel方式保存
