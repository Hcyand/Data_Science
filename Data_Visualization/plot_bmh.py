from numpy.random import beta
import matplotlib.pyplot as plt

plt.style.use('bmh')


# histtype表示表格样式
# deta函数
# bins表示取多少个值
# alpha表示可视程度（0~1）
def plot_beta_hist(ax, a, b):
    ax.hist(beta(a, b, size=10000), histtype="stepfilled", bins=500, alpha=0.8, normed=True)


fig, ax = plt.subplots()
plot_beta_hist(ax, 10, 10)
plot_beta_hist(ax, 4, 12)
plot_beta_hist(ax, 50, 12)
plot_beta_hist(ax, 6, 55)
ax.set_title("'bmh' style sheet")
plt.show()
