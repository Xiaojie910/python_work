# ~ #10-1文件打开的三种方式
# ~ ##1
# ~ print(".read()方式打开：")
# ~ with open("taohuaange.txt",encoding="UTF-8") as file_object:
	# ~ contents = file_object.read()
	# ~ print(contents)

# ~ ##2
# ~ print("逐行打印，for循环遍历：")
# ~ filename="taohuaange.txt"
# ~ with open(filename,encoding="UTF-8") as file_object:
	# ~ for line in file_object:
		# ~ print(line)

# ~ ##3
# ~ print("逐行打印，采用.rstrip（）处理for循环遍历：")
# ~ filename="taohuaange.txt"
# ~ with open(filename,encoding="UTF-8") as file_object:
	# ~ for line in file_object:
		# ~ print(line.rstrip())

# ~ ##4
# ~ print("利用.readlines()处理")
# ~ filename="taohuaange.txt"
# ~ with open(filename,encoding="UTF-8") as file_object:
	# ~ lines = file_object.readlines()
# ~ #print(lines)	
# ~ for line in lines:
	# ~ print(line.rstrip())

# ~ #10-2replace()字符串替换
# ~ msg = "娘子 is real!"
# ~ print("\n"+msg)
# ~ msg=msg.replace("real","rio")
# ~ print("\n"+msg)

# ~ print("替换前")
# ~ with open("HTSC.txt",encoding="UTF-8") as file_object:
	# ~ contents = file_object.read()
	# ~ print(contents)

# ~ print("替换后")
# ~ with open("HTSC.txt",encoding="UTF-8") as file_object:
	# ~ contents = file_object.read()
	# ~ contents = contents.replace("女子香","男子香")#替换所有的“女子香”
	# ~ print(contents)

# ~ #10-3 写入文档
# ~ file_name = "10-3XIERU.txt"
# ~ with open("10-3XIERU.txt","w",encoding="UTF-8") as file_object:
	# ~ msg = input("请输入：")
	# ~ file_object.write(msg)#列入输入我爱张杰

# ~ #10-4连续输入，一条占一行
# ~ file_name = "10-4.txt"
# ~ with open(file_name,"w",encoding="UTF-8") as file_object:
	# ~ while True:
		# ~ msg = input("请输入：")
		# ~ if msg != "q":
			# ~ file_object.write(msg+"\n")
		# ~ else:
			# ~ break

# ~ #10-5对10-4做修改利用列表
# ~ words = ["我爱张杰","我爱打卡玲","我爱中华","我爱世界","我爱宇宙","我爱太阳系"]
# ~ file_name = "10-5.txt"
# ~ with open(file_name,"w",encoding="UTF-8") as file_object:
	# ~ for word in words:
		# ~ file_object.write(word+"\n")
# ~ print("写入完成")

# ~ #10-6,10-7一起做了
# ~ print("给我俩个数字，我会将它们相加。")
# ~ print("输入q退出")
# ~ while True:
	# ~ first_number = input("\n第一个数字： ")
	# ~ if first_number == "q":
		# ~ break
	# ~ second_number = input("\n第二个数字： ")
	# ~ if second_number == "q":
		# ~ break
	# ~ answer = int(first_number)+int(second_number)
	# ~ print(answer)

# ~ #利用try-except解决问题
# ~ print("给我俩个数字，我会将它们相加。")
# ~ print("输入q退出")
# ~ while True:
	# ~ first_number = input("\n第一个数字： ")
	# ~ if first_number == "q":
		# ~ break
	# ~ second_number = input("\n第二个数字： ")
	# ~ if second_number == "q":
		# ~ break
	# ~ try:
		# ~ answer = int(first_number)+int(second_number)
	# ~ except:
		# ~ print("非数字不能做此操作")
	# ~ else:
		# ~ print(answer)



# ~ #10-8猫和狗，列表开文件，except解决文件不存在问题
# ~ def read_txt(filename):
	# ~ for filename in filenames:
		# ~ try:
			# ~ with open(filename,encoding="UTF-8") as file_object:
				# ~ contents = file_object.read()
		# ~ except FileNotFoundError:
			# ~ print("不存在改文件")
		# ~ else:
			# ~ print(contents)

# ~ filenames = ["10-4.txt","10-5.txt","1000.txt"]
# ~ read_txt(filenames)

# ~ #10-9利用pass处理问题
# ~ def read_txt(filename):
	# ~ for filename in filenames:
		# ~ try:
			# ~ with open(filename,encoding="UTF-8") as file_object:
				# ~ contents = file_object.read()
		# ~ except FileNotFoundError:
			# ~ pass
		# ~ else:
			# ~ print(contents)

# ~ filenames = ["10-4.txt","10-5.txt","1000.txt"]
# ~ read_txt(filenames)

# ~ #10-10count()计算字符串或文章中单词（短语）出现了多少次，以空格、换行等为标准
# ~ with open("taohuaange.txt",encoding="UTF-8") as file_object:
	# ~ contents = file_object.read()
	# ~ print(contents)
# ~ print(contents.count("桃花"))

#10-11、10-12json.dump,利用书上的例子
import json
def get_stored_number(filename):
	"""如果储存了数字，就获取他"""
	filename = filename   #这里可以改成其他变量
	try:
		with open(filename,encoding="UTF-8") as file_object:
			number = json.load(file_object)
	except FileNotFoundError:
		return None  ###这里用于下面做逻辑的判断
	else:
		return number

def get_new_number():
	"""提示用户输入"""
	number = input("输入你最喜欢的数字： ")
	filename = "number.json"
	with open(filename,"w",encoding="UTF-8") as file_object:
		json.dump(number,file_object)
	return number
	
def greet_user(filename):
	number = get_stored_number(filename)
	if number:
		print("我知道你最喜欢的数字是："+number)
	else:
		username = get_new_number()
		print("我会记得你的，当你再次回来的时候！")

greet_user("number.json")
		
