# 第12章：K近邻法
# 12.1 模型
# （1）某种距离的概念（2）一种彼此接近的点具有相似性质的假设
from collections import Counter


def raw_majority_vote(labels):
    votes = Counter(labels)
    # 返回一个TopN列表。如果n没有被指定，则返回所有元素。当多个元素计数值相同时，排列是无确定顺序的
    winner, _ = votes.most_common(1)[0]
    return winner


# 当具有相同票数时，三种解决方案
# 1.随机选择一个 2.根据距离加权并选择加权的获胜者
# 3.减少k值知道找到唯一获胜者，我们运用第三种
def majority_vote(labels):
    vote_counts = Counter(labels)
    winner, winner_count = vote_counts.most_common(1)[0]
    num_winners = len([count for count in vote_counts.values()
                       if count == winner_count])
    if num_winners == 1:
        return winner
    else:
        return majority_vote(labels[:-1])  # 去掉最远元素
