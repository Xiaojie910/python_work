#习题6-1使用一个字典，将存的信息打印出来
durian_mille_crepe_cake = {'durian':'炒了',
							'mille crepe':'煎了',
							'cake':'抹上',
							}
print(durian_mille_crepe_cake)

#习题6-2
favorite_number = {'a':'1','b':'2','c':'3','d':'4','e':'5'}
print(favorite_number)

#习题6-3、6-4
python_words = {'Code lay out':'代码布局',
				'Whitespaces in Expressions':'表达式中的空格',
				'Comments':'注释',
				'Naming Conventions':'命名规范',
				'Programing recommendations':'编程建议',
				'Global Variable Names':'全局变量名',
				'Function Annotation':'功能注释',
				'Indentation':'缩进',
				'Binary Operatoe':'运算符',
				'string quotes':'字符串引号'}

#.item()不要忘记，调用字典中的键值对
for word,explanation in python_words.items():
	print("\n"+word+":")
	print(explanation)

#6-5河流 国家
rivers = {'La Seine':'France','yellow river':'China','Nile':'Egypt'}
for river,country in rivers.items():
	print("\nThe "+river.title()+" runs through "+country+"!!")
for river,country in rivers.items():
	print(river)
for river,country in rivers.items():
	print(country)  

#名单列表，字典，在列表中和不在列表中区别打印
king_seven_armed_sea = ['鹰眼','老沙','九蛇','明哥','甚平','月光莫利亚','大熊','罗','巴基']
the_defeated = {'老沙':'歇菜','月光莫利亚':'完蛋','大熊':'打不过就跑','甚平':'收编'}
for name in king_seven_armed_sea:
	if name in the_defeated.keys():
		print(name+',嘿兄弟老熟人了啊')
	else:
		print(name,',你等着!')
		

#6-7三个字典合成一个字典
durian_mille_crepe_cake = {'durian':'炒了',
							'mille crepe':'煎了',
							'cake':'抹上',
							}

tomato_egg = {'tomato':'切了','egg':'炒了','suger':'适量','salt':'少量'}
palace_exploded_chicken_man = {'peanut':'爆炒','chicken':'腌制好','carrot':'切成丁'}
cook_books = [durian_mille_crepe_cake,tomato_egg,palace_exploded_chicken_man]
for dish in cook_books:
	for ingredient,method in dish.items():
		print("\n材料:"+ingredient)
		print("方法:"+method)

#6-8宠物
tom = {'type':'cat','host':'一个只有脚出境的女子'}
jerry = {'type':'hourse','host':'观众'}
speike = {'type':'dog','host':'一个只有脚出境的女子'}
pets = [tom,jerry,speike]
for pet in pets:
	for key,value in pet.items():
		print('\n'+key+":"+value)

#6-9喜欢的地方，字典套列表
favorite_places = {'依萍':['大上海','可云家','火车站'],
					'如萍':['书桓家','公园','上海大桥'],
					'陆飞':['如萍学校','报社','战场'],
					}
					
for name,places in favorite_places.items():
	print("\n"+name+'喜欢的地方:')
	for place in places:
		print(place)

#6-10喜欢的数字
favorite_number = {'a':[1,2,3],'b':[4,5,6],'c':[7,8,9],'d':[10,11,12]}
for name,numbers in favorite_number.items():
	print("\n"+name+"喜欢的数字是:")
	for number in numbers:
		print(number)

#6-11城市 字典套字典
places = {'bordeux':{'country':'france',
			'population':'23456',
			'fact':'水晶广场',
			},
'larochelle':{'country':'france',
				'population':'456789',
				'fact':'港口水族馆和世界的尽头',
				},
'barcelona':{'country':'spain',
				'population':'789123',
				'fact':'建筑教堂和弗朗明哥圆圈舞',
				},
				}
for city,info in places.items():
	print("\n\n"+city+"介绍:")
	for key,value in info.items():
		print("\n"+key+':'+value)
