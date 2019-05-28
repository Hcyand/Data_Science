"""
评论提取
"""
import pandas as pd

inputfile = 'huizong.csv'
outputfile = 'meidi_jd.txt'
data = pd.read_csv(inputfile, encoding='utf-8')
data = data[['评论']][data['品牌'] == '美的']
data.to_csv(outputfile, index=False, header=False)
