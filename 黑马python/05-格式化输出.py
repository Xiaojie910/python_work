"""
1.准备数据
2.格式化符号输出数据
"""
age = 18
name = 'Tom'
weight = 75.5
stu_id = 1
#1.今年我的年纪是x岁--整数 %d
print('今年我的年纪是%d岁' % age)

#2.我的名字是x--字符串 %s(也可用来输出其他整数和浮点数形式例如2.1)
print('我的名字是%s' % name)
#2.1.我的名字是x，今年x岁了，体重x公斤
print('我的名字是%s，今年%s岁了，体重%s公斤' %(name,age+1,weight))

#3.我的体重是x公斤--浮点型 %f（%号后.xf表示保留几位小数）
print('我的体重是%.2f公斤' % weight)

#4.我的学号是x--%d
print('我的学号是%d' % stu_id)
#4.1我的学号是001--%03d（表示输出是三位数，不足的以0补全，超出的原样输出
print('我的学号是%03d' %stu_id)

#5.我的名字是x，今年x岁了
print('我的名字是%s,今年%d岁了' %(name,age))
#5.1.我的名字是x，明年我就x岁了
print('我的名字是%s，明年我就%d岁了' %(name,age+1) )

#6.我的名字是x，今年x岁了，体重x公斤，学号是x
print('我的名字是%s，今年%d岁了，体重%.2f公斤，学号是%03d' %(name,age,weight,stu_id))

#7.语法 f'{表达式}'
print(f'我的名字是{name}，今年{age+1}岁了，体重{weight}公斤，学号是{stu_id}')
