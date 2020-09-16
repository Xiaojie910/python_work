from die import Die
import pygal
#创建一个D6
die = Die()
#整几次骰子，并将结果储存在一个列表中
results = []
for roll_num in range(100):
	result = die.roll()
	results.append(result)
	
#分析结果
frequencies = []
for value in range(1,die.num_sides+1):
	frequence = results.count(value)
	frequencies.append(frequence)
	
#对结果进行可视化
hist = pygal.Bar()

hist.title = "100次六面骰子的结果直方图"
hist.x_labels = ['1','2','3','4','5','6']
hist.x_title = "点数"
hist.y_title = '对应点出现的次数'

hist.add('六面骰子',frequencies)
hist.render_to_file('die_visual.svg')

