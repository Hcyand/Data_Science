# 第13章：朴素贝叶斯算法

# 13.1一个简单的垃圾邮件过滤器
# 50%的垃圾邮件里含有单词viagra，而只有1%的非垃圾邮件里含有这个单词
# 任何一封含有viagra的电子邮件是垃圾邮件的概率：0.5/（0.5+0.01）=98%

# 13.2一个复杂的垃圾邮件过滤器
# 伪计数：data这个单词在98封邮件中出现0次，k取值1，即p=0.01，这样data垃圾邮件的概率非0值了

# 13.3算法的实现
# 将邮件解析为不同的单词，文本转换为小写形式
# 使用re.findall()提取由字母，数字和撇号组成的“单词”，set()函数获得不同的单词
import re


def tokenize(message):
    message = message.lower()
    all_words = re.findall("[a-z0-9']+", message)
    return set(all_words)
