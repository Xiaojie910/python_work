# ~ #习题7-1
# ~ vehicle = input("what kind of vehicle would you like to try?")
# ~ print("Ok,i will show you the series of "+vehicle+",this way please!")

# ~ #习题7-2
# ~ number = input("how many people here?")
# ~ number = int(number)
# ~ if number >= 8:
	# ~ print("there's no empty table!")
# ~ else:
	# ~ print("there's an empty table for you!")

# ~ #习题7-3
# ~ question = "tell me a number: "
# ~ question += "\ni will tell if it is multiple of ten."
# ~ number = input(question)
# ~ number = int(number)#这个转换必须有
# ~ if number % 10 ==0:
	# ~ peint("yes,it is!")
# ~ else:
	# ~ print("no,it is not!")

# ~ #习题7-4
# ~ print("输入你想要添加的配料，输入quit结束")
# ~ topping = ""
# ~ while topping != "quit":
	# ~ topping = input("what would you like to add on your pizza?")
	# ~ if topping != "quit":
		# ~ print("add some "+topping)
		
# ~ #习题7-5
# ~ print("输入年龄，得到票价，输入quit退出")
# ~ age = ""
# ~ while age != "quit":
	# ~ age = input("how old are you? ")
	# ~ if age != "quit":
		# ~ age = int(age)
		# ~ if age < 0:
			# ~ print("别闹，重新输入")
			# ~ continue
		# ~ elif age >= 0 and age < 3:
			# ~ price = 0
		# ~ elif age >= 3 and age <=12:
			# ~ price = 10
		# ~ elif age > 12:
			# ~ price = 15
		# ~ print("your admission cost is "+str(price)+"$!")

# ~ #习题7-6
# ~ #active用法
# ~ active = True
# ~ while active:
	# ~ age = input("how old are you? ")
	# ~ if age != "quit":
		# ~ age = int(age)
		# ~ if age < 0:
			# ~ print("别闹，重新输入")
			# ~ continue
		# ~ elif age >= 0 and age < 3:
			# ~ price = 0
		# ~ elif age >= 3 and age <=12:
			# ~ price = 10
		# ~ elif age > 12:
			# ~ price = 15
		# ~ print("your admission cost is "+str(price)+"$!")
	# ~ else:
		# ~ active = False
		
# ~ #break用法
# ~ while True:
	# ~ age = input("how old are you? ")
	# ~ if age != "quit":
		# ~ age = int(age)
		# ~ if age < 0:
			# ~ print("别闹，重新输入")
			# ~ continue
		# ~ elif age >= 0 and age < 3:
			# ~ price = 0
		# ~ elif age >= 3 and age <=12:
			# ~ price = 10
		# ~ elif age > 12:
			# ~ price = 15
		# ~ print("your admission cost is "+str(price)+"$!")
	# ~ else:
		# ~ break

#习题7-7
#无限循环

# ~ #7-8
# ~ sandwich_orders = ["蛋黄三明治","奶酪火腿三明治","三文鱼三明治"]
# ~ finished_sandwichs = []
# ~ while sandwich_orders:
	# ~ sandwich = sandwich_orders.pop()
	# ~ print(sandwich+":i made your sandwich!")
	# ~ finished_sandwichs.append(sandwich)
# ~ print("finished sandwichs:")
# ~ for sandwich in finished_sandwichs:
	# ~ print(sandwich)

#7-9
sandwich_orders = ["蛋黄三明治","奶酪火腿三明治","三文鱼三明治","蛋黄三明治","牛肉三明治","蛋黄三明治"]
while "蛋黄三明治" in sandwich_orders:
	sandwich_orders.remove("蛋黄三明治")
for sandwich in sandwich_orders:
	print(sandwich)

# ~ #7-10
# ~ name_places = {}
# ~ print("问卷调查，任何时候，输入quit退出")
# ~ while True:
	# ~ name = input("输入您的名字 ")
	# ~ if name == "quit":
		# ~ break
	# ~ else:
		# ~ place = input("您最想去的地方 ")
		# ~ if place == "quit":
			# ~ break
		# ~ else:
			# ~ name_places[name] = place
# ~ print("调查结束，结果如下：")
# ~ for name,place in name_places.items():
	# ~ print(name+"最想去的地方："+place+"!")
			



