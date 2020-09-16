from die import Die
import pygal
#创建2个骰子
die_1 = Die()
die_2 = Die()
#整几次骰子，并将结果储存在一个列表中
results = []
for roll_num in range(1000):
	result = die_1.roll()+die_2.roll()
	results.append(result)
	
#分析结果
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2,max_result+1):
	frequence = results.count(value)
	frequencies.append(frequence)
	
#对结果进行可视化
hist = pygal.Bar()

hist.title = "100次2个六面骰子的结果直方图"
hist.x_labels = ['2','3','4','5','6','7','8','9','10','11','12']
hist.x_title = "点数"
hist.y_title = '对应点出现的次数'

hist.add('2个六面骰子',frequencies)
hist.render_to_file('dice_visual.svg')
