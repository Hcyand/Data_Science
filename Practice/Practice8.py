# 第9章：获取数据
# 利用sys.stdin和sys.stdout以管道的方式进行传递数据
# # errep.py
# import sys, re
#
# # sys.argv是m命令行参数的列表
# sys.sargv[0]是程序自己的名字
# sys.argv[1]会是在命令行上指定的正则表达式
# regex = sys.argv[1]
# 对传递到这个脚本中的每一行
# for line in sys.stdin:
# 如果它匹配正则表达式，则写入stdout
#     if re.search(regex, line):
#         sys.stdout.write(line)

# # line_count.py
# import sys
# count = 0
# for line in sys.stdin:
#     count += 1
# print(count)

# 这种方法计算文件中有多少行包含数字
# type SomeFile.py.txt | python egrep.py "[0-9]" | python line_count.py

# 计算单词的数量并且给出常用的单词
import sys, re
from collections import Counter

# # 传递单词个数作为第一个参数
# try:
#     num_words = int(sys.argv[1])
# except:
#     print("usage: Practice8.py num_words")
#     sys.exit(1)  # 非零的exit代码表明有错误
# counter = Counter(word.lower()
#                   for line in sys.stdin
#                   for word in line.strip().split()
#                   if word)
# for word, count in counter.most_common(num_words):
#     sys.stdout.write(str(count))
#     sys.stdout.write("\t")
#     sys.stdout.write(word)
#     sys.stdout.write("\n")

# 读取文件
# 'r'表示只读   'w'表示写入（会破坏已经存在的文件） 'a'为添加，添加至文件的末尾   .close()为关闭文件
# file_for_reading = open('test.txt', 'r')
# file_for_reading.close()


# 读取一个完整的文件，使用for语句对文件进行迭代
starts_with_hash = 0
with open('test.txt', 'r') as f:
    # 查找文件的每一行
    for line in f:
        # 用正则表达式判断是否是以'#'开头
        if re.match("^#", line):
            # 如果是，计数加一
            starts_with_hash += 1


# 网络爬取
# HTML和解析方法
# 使用API：Application Programming Interface（应用程序接口），允许明确的请求结构化格式的数据
# JSON/使用无验证的API/寻找API
