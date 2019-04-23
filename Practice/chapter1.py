# 第1章：导论
# 激励假设：DataSciencester
# 1.3.1 寻找关键联系人
from collections import Counter
from collections import defaultdict
from matplotlib import pyplot as plt

users = [
    {"id": 0, "name": "Hero"},
    {"id": 1, "name": "Dumn"},
    {"id": 2, "name": "Sue"},
    {"id": 3, "name": "Chi"},
    {"id": 4, "name": "Thor"},
    {"id": 5, "name": "Clive"},
    {"id": 6, "name": "Hicks"},
    {"id": 7, "name": "Devin"},
    {"id": 8, "name": "Kate"},
    {"id": 9, "name": "Klein"}
]
friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

# 每个用户增加一个朋友列表
for user in users:
    user["friends"] = []

# 再用friendships数据填充
for i, j in friendships:
    users[i]["friends"].append(users[j])
    users[j]["friends"].append(users[i])


# 深入研究朋友网络关系：平均联系数是多少
# 先计算所有用户朋友的长度和
def number_of_friends(user):
    return len(user["friends"])


total_connections = sum(number_of_friends(user) for user in users)
# 然后除以用户个数
num_users = len(users)
avg_connections = total_connections / num_users

# 按照朋友数进行排序
# 创建一个列表（user_id,number_of_friends)
num_friends_by_id = [(user["id"], number_of_friends(user)) for user in users]
sorted(num_friends_by_id, key=lambda num_friends: num_friends, reverse=True)


# 1.3.2你可能知道的数据科学家
# 针对某个用户，用户朋友的朋友可能认识
def friends_of_friend_ids_bad(user):
    # foaf是朋友的朋友缩写
    return [foaf["id"] for friend in user["friends"]
            for foaf in friend["friends"]]


# 寻找共同朋友
def not_the_same(user, other_user):
    return user["id"] != other_user["id"]


def not_friends(user, other_user):
    return all(not_the_same(friend, other_user) for friend in user["friends"])


def friends_of_friend_ids(user):
    return Counter(foaf["id"]
                   for friend in user["friends"]
                   for foaf in friend["friends"]
                   if not_the_same(user, foaf)
                   and not_friends(user, foaf))


# print(friends_of_friend_ids(users[3]))

# 根据兴趣来寻找共同兴趣的用户
interests = [

    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),

    (0, "Spark"), (0, "Storm"), (0, "Cassandra"),

    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),

    (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),

    (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),

    (3, "statistics"), (3, "regression"), (3, "probability"),

    (4, "machine learning"), (4, "regression"), (4, "decision trees"),

    (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),

    (5, "Haskell"), (5, "programming languages"), (6, "statistics"),

    (6, "probability"), (6, "mathematics"), (6, "theory"),

    (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),

    (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),

    (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),

    (9, "Java"), (9, "MapReduce"), (9, "Big Data")

]


# 寻找对某事物有共同兴趣的用户
def data_scientists_who_like(target_interest):
    return [user_id
            for user_id, user_interest in interests
            if user_interest == target_interest]


# 建立一个从兴趣到用户的索引之间搜索
# 键是interest，值是带有这个interest的user_id的列表
user_ids_by_interest = defaultdict(list)
for user_id, interest in interests:
    user_ids_by_interest[interest].append(user_id)
# 以及另一个从用户到兴趣的索引
interests_by_user_id = defaultdict(list)
for user_id, interest in interests:
    interests_by_user_id[user_id].append(interest)


# 给定用户，寻找相同爱好的用户
# 1.迭代这个用户的兴趣2.针对这个用户的每个兴趣，寻找该兴趣的用户，并迭代3.记录每个用户出现的次数
def most_common_interest_with(user):
    return Counter(interested_user_id
                   for interest in interests_by_user_id[user["id"]]
                   for interested_user_id in user_ids_by_interest[interest]
                   if interested_user_id != user["id"])


salaries_and_tenures = [(83000, 8.7), (88000, 8.1),

                        (48000, 0.7), (76000, 6),

                        (69000, 6.5), (76000, 7.5),

                        (60000, 2.5), (83000, 10),

                        (48000, 1.9), (63000, 4.2)]
tenures = [tenure for salary, tenure in salaries_and_tenures]

salaries = [salary for salary, tenure in salaries_and_tenures]

plt.scatter(tenures, salaries)

plt.xlabel("Years Experience")

plt.ylabel("Salary")

plt.show()
