"""
删除前缀评分
"""
import pandas as pd

inputfile1 = 'meidi_jd_process_end_负面情感结果.txt'
inputfile2 = 'meidi_jd_process_end_正面情感结果.txt'
outputfile1 = 'meidi_jd_neg.txt'
outputfile2 = 'meidi_jd_pos.txt'

data1 = pd.read_csv(inputfile1, encoding='utf-8', header=None)
data2 = pd.read_csv(inputfile2, encoding='utf-8', header=None)

data1 = pd.DataFrame(data1[0].str.replace('.*?\d+?\\t', ''))
data2 = pd.DataFrame(data2[0].str.replace('.*?\d+?\\t', ''))

data1.to_csv(outputfile1, index=False, header=False, encoding='utf-8')
data2.to_csv(outputfile2, index=False, header=False, encoding='utf-8')
