"""
验证输入用户名和QQ号是否有效
拆分长字符串
"""
import re


def main():
    poem = '床前明月光，疑是地上霜。举头望明月，低头思故乡。'
    sentence_list = re.split(r'[，。,.]', poem)
    while '' in sentence_list:
        sentence_list.remove('')
    print(sentence_list)


if __name__ == '__main__':
    main()
