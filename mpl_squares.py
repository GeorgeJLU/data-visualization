import matplotlib.pyplot as plt

#绘制图表时显示中文字体
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

# 使用 plt.style.available 指令查找可用样式
plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()

# 绘制散点图
ax.scatter(x_values, y_values, c='red', s=10)
#ax.scatter(x_values, y_values, c=(0, 0.8, 0), s=10)
# 使用颜色映射
#ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# 绘制折线图
#ax.plot(x_values, y_values, linewidth=3)

# 设置图表标题并为坐标轴加上标签
ax.set_title("平方数", fontsize=20)
ax.set_xlabel("值", fontsize=14)
ax.set_ylabel("值的平方", fontsize=14)

# 设置刻度标记的大小
ax.tick_params(axis='both', labelsize=14)

# 设置 x 坐标轴和 y 坐标轴的取值范围
ax.axis([0, 1100, 0, 1100000])

# 自动保存图表
plt.savefig('squares_plot.png', bbox_inches='tight')

plt.show()