# #15-1立方并指定颜色
# import matplotlib.pyplot as plt
#
# x_values = list(range(1,5001))
# y_values = [x**3 for x in x_values]
# plt.scatter(x_values,y_values,edgecolor="none",s=40,c=x_values,cmap=plt.cm.Reds)
#
# #设置图表的标题和坐标轴的标签
# plt.title("Square numbers",fontsize=24)
# plt.xlabel("Value",fontsize=14)
# plt.ylabel("Square of Value",fontsize=14)
#
# #设置刻度标记的大小
# plt.tick_params(axis="both",which='major',labelsize=15)
# plt.axis([0,5100,0,130000000000])
# plt.show()

# ##15-3/15-4
# from random import choice
# import matplotlib.pyplot as plt
#
#
# class RandomWalk():
#     """一个生成随机漫步数据的类"""
#
#     def __init__(self, num_points=5000):
#         """初始化随机漫步的属性"""
#         self.num_points = num_points
#
#         # 所有的随机漫步都始于（0,0）
#         self.x_values = [0]
#         self.y_values = [0]
#
#     def fill_walk(self):
#         """计算随机漫步包含的所有的点"""
#
#         # 不断漫步，直到列表达到指定的长度
#         while len(self.x_values) < self.num_points:
#             # 决定前进的方向以及沿着这个方向前进的距离
#             x_direction = choice([1, -1])
#             x_distance = choice([0, 1, 2, 3, 4])
#             x_step = x_direction * x_distance
#
#             y_direction = choice([1, -1])
#             y_distance = choice([0, 1, 2, 3, 4])
#             y_step = y_direction * y_distance
#
#             # 拒绝原地踏步
#             if x_step == 0 and y_step == 0:
#                 continue
#
#             # 计算下一个点的x，y值
#             next_x = self.x_values[-1] + x_step
#             next_y = self.y_values[-1] + y_step
#
#             self.x_values.append(next_x)
#             self.y_values.append(next_y)
# while True:
#     rw = RandomWalk()
#     rw.fill_walk()
#
#     plt.figure(figsize=(10,6))
#     point_numbers = list(range(rw.num_points))
#     plt.plot(rw.x_values,rw.y_values,c='green')
#     plt.plot(0,0,c='green')
#     plt.plot(rw.x_values[-1],rw.y_values[-1],c='blue')
#     plt.axes().get_xaxis().set_visible(False)
#     plt.axes().get_yaxis().set_visible(False)
#     plt.show()
#     keep_running = input('make another walk?:')
#     if keep_running =='n':
#         break

##15-5重构
# from random import choice
# import matplotlib.pyplot as plt
#
#
# class RandomWalk():
#     """一个生成随机漫步数据的类"""
#
#     def __init__(self, num_points=5000):
#         """初始化随机漫步的属性"""
#         self.num_points = num_points
#
#         # 所有的随机漫步都始于（0,0）
#         self.x_values = [0]
#         self.y_values = [0]
#
#     def fill_walk(self):
#         """计算随机漫步包含的所有的点"""
#
#         # 不断漫步，直到列表达到指定的长度
#         while len(self.x_values) < self.num_points:
#             # 决定前进的方向以及沿着这个方向前进的距离
#             x_step = self.get_step()
#             y_step = self.get_step()
#
#             # 拒绝原地踏步
#             if x_step == 0 and y_step == 0:
#                 continue
#
#             # 计算下一个点的x，y值
#             next_x = self.x_values[-1] + x_step
#             next_y = self.y_values[-1] + y_step
#
#             self.x_values.append(next_x)
#             self.y_values.append(next_y)
#
#     def get_step(self):
#         direction = choice([1,-1])
#         distance = choice([0,1,2,3,4])
#         step = direction * distance
#         return step
# while True:
#     rw = RandomWalk()
#     rw.fill_walk()
#
#     plt.figure(figsize=(10,6))
#     point_numbers = list(range(rw.num_points))
#     plt.plot(rw.x_values,rw.y_values,c='green')
#     plt.plot(0,0,c='green')
#     plt.plot(rw.x_values[-1],rw.y_values[-1],c='blue')
#     plt.axes().get_xaxis().set_visible(False)
#     plt.axes().get_yaxis().set_visible(False)
#     plt.show()
#     keep_running = input('make another walk?:')
#     if keep_running =='n':
#         break

##15-6自动生成标签，x值改为循环，for循环替换列表解析
##列表解析，直接上
# squares = [value**2 for value in range(1,11)]
# print(squares)

# import pygal
# from random import randint
#
#
# class Die():
#     """表示一个骰子的类"""
#
#     def __init__(self, num_sides=6):
#         """默认是6个面"""
#         self.num_sides = num_sides
#
#     def roll(self):
#         """返回一个位于1和骰子面数的随机值"""
#         return randint(1, self.num_sides)
#
# die_1 = Die()
# die_2 = Die()
#
# results = [die_1.roll() + die_2.roll() for roll_num in range(1000)]
#
# #分析结果
# frequencies = []
#
# max_result = die_1.num_sides + die_2.num_sides
# frequencies = [results.count(value) for value in range(2,max_result+1)]
#
# #对结果进行可视化
# hist = pygal.Bar()
#
# hist.title = "100次2个六面骰子的结果直方图"
# hist.x_labels = ['2','3','4','5','6','7','8','9','10','11','12']
# hist.x_title = "点数"
# hist.y_title = '对应点出现的次数'
#
# hist.add('2个六面骰子',frequencies)
# hist.render_to_file('dice_visual_4.svg')

#15-7
# import pygal
# from random import randint
#
#
# class Die():
#     """表示一个骰子的类"""
#
#     def __init__(self, num_sides=6):
#         """默认是6个面"""
#         self.num_sides = num_sides
#
#     def roll(self):
#         """返回一个位于1和骰子面数的随机值"""
#         return randint(1, self.num_sides)
#
# die_1 = Die(8)
# die_2 = Die(8)
#
# results = [die_1.roll() + die_2.roll() for roll_num in range(1000)]
#
# #分析结果
# frequencies = []
#
# max_result = die_1.num_sides + die_2.num_sides
# frequencies = [results.count(value) for value in range(2,max_result+1)]
#
# #对结果进行可视化
# hist = pygal.Bar()
#
# hist.title = "100次2个8面骰子的结果直方图"
# hist.x_labels = [x for x in range(2,max_result+1)]
# hist.x_title = "点数"
# hist.y_title = '对应点出现的次数'
#
# hist.add('2个8面骰子',frequencies)
# hist.render_to_file('dice_visual_5.svg')

#15-8三个骰子
import pygal
from random import randint


class Die():
    """表示一个骰子的类"""

    def __init__(self, num_sides=6):
        """默认是6个面"""
        self.num_sides = num_sides

    def roll(self):
        """返回一个位于1和骰子面数的随机值"""
        return randint(1, self.num_sides)

die_1 = Die()
die_2 = Die()
die_3 = Die()

results = [die_1.roll() + die_2.roll() + die_3.roll() for roll_num in range(10000)]

#分析结果
frequencies = []

max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
frequencies = [results.count(value) for value in range(3,max_result+1)]

#对结果进行可视化
hist = pygal.Bar()

hist.title = "10000次3个6面骰子的结果直方图"
hist.x_labels = [x for x in range(3,max_result+1)]
hist.x_title = "点数"
hist.y_title = '对应点出现的次数'

hist.add('3个6面骰子',frequencies)
hist.render_to_file('dice_visual_6.svg')

##15-9点数相乘
利用俩次循环添加结果
results = [die_1.roll()*die_2.roll() for roll_num in range(10000)]
result_possible = []
for n in range(1,die_1.num_sides+1):
    for m in range(1,die_2.num_sides+1):
        if n*m not in result_possible:
            result_possible.append(n*m)
result_possible.sort()

##15-10
#使用matploylib来模拟投掷骰子
#直接调用plt.bar(range(2,max_rasult+1),frequencies)

#使用pygal模拟随机漫步
#直接调用
# rw.fill_walk()
# 以下改成
# sandiantu = pygal.xy(stroke=False)
# sandiantu.title ='随机漫步结果'
# sandiantu.add('A',rw.values)
# sandiantu.render_to_file('randon_walk_2.svg')

