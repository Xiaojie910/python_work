# ~ #9-1
# ~ class Restaurant():#注意大小写
	# ~ """模拟饭店调查"""
	
	# ~ def __init__(self,restaurant_name,cuisine_type):#init俩边分别是俩个下划线
		# ~ self.name=restaurant_name
		# ~ self.type=cuisine_type
		
	# ~ def describe_restaurant(self):##self不要忘记
		# ~ print(self.name + "的"+self.type + "很不错哦")
		
	# ~ def open_restaurant(self):
		# ~ print("而且他正在营业")

# ~ my_restaurant = Restaurant("张家饭店","徽菜")
# ~ my_restaurant.describe_restaurant()
# ~ my_restaurant.open_restaurant()

#9-2多次调用9-1的函数

# ~ #9-3
# ~ class User():
	# ~ """记录用户的信息"""
	# ~ def __init__(self,xing,ming,*qita):
		# ~ self.xing=xing
		# ~ self.ming=ming
		# ~ self.qita=qita
	
	# ~ def describe_user(self):
		# ~ print("姓："+self.xing)
		# ~ print("名："+self.ming)
		# ~ if self.qita:
			# ~ print("\n其他信息如下：\n")
			# ~ for info in self.qita:
				# ~ print("-"+info)
	
	# ~ def greet_user(self):
		# ~ print("\n"+"小"+self.ming + "，我们奶你！")
		# ~ print("小"+self.ming + "，你老霸道了！")
	
# ~ my_user=User("张","杰","帅啊","机智","成功")
# ~ my_user.describe_user()
# ~ my_user.greet_user()	

# ~ #9-4修改9-1的代码
# ~ class Restaurant():#注意大小写
	# ~ """模拟饭店调查"""
	
	# ~ def __init__(self,restaurant_name,cuisine_type):#init俩边分别是俩个下划线
		# ~ self.name=restaurant_name
		# ~ self.type=cuisine_type
		# ~ self.number_served=0
		
	# ~ def describe_restaurant(self):
		# ~ print(self.name + "的"+self.type + "很不错哦")
		
	# ~ def open_restaurant(self):
		# ~ print("而且他正在营业")
	
	# ~ def set_number_served(self,number):
		# ~ if number >= self.number_served:
			# ~ self.number_served=number
		# ~ print("共有"+str(self.number_served)+"人在此用餐")
		
	# ~ def increment_number_served(self,increment_number):
		# ~ self.number_served += increment_number
		# ~ print("共有"+str(self.number_served)+"人在此用餐")

# ~ my_restaurant = Restaurant("张家饭店","徽菜")
# ~ my_restaurant.set_number_served(100)
# ~ my_restaurant.increment_number_served(50)

# ~ #9-5修改9-3的代码
# ~ class User():
	# ~ """记录用户的信息"""
	# ~ def __init__(self,xing,ming,*qita):
		# ~ self.xing=xing
		# ~ self.ming=ming
		# ~ self.qita=qita
		# ~ self.login_attempts=0
	
	# ~ def describe_user(self):
		# ~ print("姓："+self.xing)
		# ~ print("名："+self.ming)
		# ~ if self.qita:
			# ~ print("\n其他信息如下：\n")
			# ~ for info in self.qita:
				# ~ print("-"+info)
	
	# ~ def greet_user(self):
		# ~ print("\n"+"小"+self.ming + "，我们奶你！")
		# ~ print("小"+self.ming + "，你老霸道了！")
		
	# ~ def increment_login_attempts(self):
		# ~ self.login_attempts += 1
		
	# ~ def reset_login_attempts(self):
		# ~ self.login_attempts=0
	
	# ~ def print_login_attempts(self):
		# ~ print("您登陆了"+str(self.login_attempts)+"次")
	
# ~ my_user=User("张","杰","帅啊","机智","成功")
# ~ my_user.describe_user()
# ~ my_user.greet_user()	
# ~ my_user.increment_login_attempts()
# ~ my_user.increment_login_attempts()
# ~ my_user.increment_login_attempts()
# ~ my_user.print_login_attempts()
# ~ my_user.reset_login_attempts()
# ~ my_user.print_login_attempts()

# ~ #9-6继承Restaurant()
# ~ class Restaurant():
	# ~ """模拟饭店调查"""
	# ~ def __init__(self,restaurant_name,cuisine_type):
		# ~ self.name=restaurant_name
		# ~ self.type=cuisine_type
		# ~ self.number_served=0
		
	# ~ def describe_restaurant(self):
		# ~ print(self.name + "的"+self.type + "很不错哦")
		
	# ~ def open_restaurant(self):
		# ~ print("而且他正在营业")
	
	# ~ def set_number_served(self,number):
		# ~ if number >= self.number_served:
			# ~ self.number_served=number
		# ~ print("共有"+str(self.number_served)+"人在此用餐")
		
	# ~ def increment_number_served(self,increment_number):
		# ~ self.number_served += increment_number
		# ~ print("共有"+str(self.number_served)+"人在此用餐")


# ~ class Icecreamstand(Restaurant):
	# ~ """继承9-4，冰淇淋特殊餐馆"""
	# ~ def __init__(self,restaurant_name,cuisine_type):
		# ~ #初始化父类参数
		# ~ super().__init__(restaurant_name,cuisine_type)
		# ~ #利用super（）函数建立与父类的关系
		# ~ self.flavors=['vanilla','chocolate','durian']
		
	# ~ def print_flavors(self):
		# ~ print("\n")
		# ~ for flavor in self.flavors:
			# ~ print(flavor)

# ~ your_restaurant=Icecreamstand('麦当劳甜品站','冰淇淋')
# ~ your_restaurant.print_flavors()

# ~ #9-7继承User，管理员
# ~ class User():
	# ~ """记录用户的信息"""
	# ~ def __init__(self,xing,ming,*qita):
		# ~ self.xing=xing
		# ~ self.ming=ming
		# ~ self.qita=qita
	
	# ~ def describe_user(self):
		# ~ print("姓："+self.xing)
		# ~ print("名："+self.ming)
		# ~ if self.qita:
			# ~ print("\n其他信息如下：\n")
			# ~ for info in self.qita:
				# ~ print("-"+info)
	
	# ~ def greet_user(self):
		# ~ print("\n"+"小"+self.ming + "，我们奶你！")
		# ~ print("小"+self.ming + "，你老霸道了！")


# ~ class Admin(User):
	# ~ """特殊用户，管理员"""
	# ~ def __init__(self,xing,ming,*qita):
		# ~ #初始化父类参数
		# ~ super().__init__(xing,ming,*qita)
		# ~ #利用super建立联系
		# ~ self.privileges="和稀泥"
	
	# ~ def show_privileges(self):
		# ~ print("\n管理员能"+self.privileges)

# ~ dalao=Admin('张','杰','帅啊','机智','成功')
# ~ dalao.show_privileges()

# ~ #9-8
# ~ class User():
	# ~ """记录用户的信息"""
	# ~ def __init__(self,xing,ming,*qita):
		# ~ self.xing=xing
		# ~ self.ming=ming
		# ~ self.qita=qita
	
	# ~ def describe_user(self):
		# ~ print("姓："+self.xing)
		# ~ print("名："+self.ming)
		# ~ if self.qita:
			# ~ print("\n其他信息如下：\n")
			# ~ for info in self.qita:
				# ~ print("-"+info)
	
	# ~ def greet_user(self):
		# ~ print("\n"+"小"+self.ming + "，我们奶你！")
		# ~ print("小"+self.ming + "，你老霸道了！")


# ~ class Admin(User):
	# ~ """特殊用户，管理员"""
	# ~ def __init__(self,xing,ming,*qita):
		# ~ #初始化父类参数
		# ~ super().__init__(xing,ming,*qita)
		# ~ #利用super建立联系
	
	# ~ def show_privileges(self):
		# ~ Privileges()


# ~ class Privileges():
	# ~ """管理人员特权"""
	# ~ def __init__(self):
		# ~ self.privileges="和稀泥"
		# ~ print("\n管理员能"+self.privileges)

# ~ dalao=Admin('张','杰','帅啊','机智','成功')
# ~ dalao.show_privileges()

#9-9电瓶升级

# ~ #9-10导入Restaurant
# ~ import restaurant
# ~ r=restaurant.Restaurant("张家饭店","徽菜")
# ~ r.describe_restaurant()
# ~ r.open_restaurant()

# ~ #9-11导入Admin，调用9-8的练习
# ~ import admin
# ~ my=admin.Admin('张','杰','帅啊','机智','成功')
# ~ my.show_privileges()

# ~ #9-12导入多个模块
# ~ import admin
# ~ my=admin.Admin('张','杰','帅啊','机智','成功')
# ~ my.show_privileges()

# ~ #9-13OrderDict,重写6-4
# ~ ##6-3/6-4复制过来
# ~ python_words = {'Code lay out':'代码布局',
				# ~ 'Whitespaces in Expressions':'表达式中的空格',
				# ~ 'Comments':'注释',
				# ~ 'Naming Conventions':'命名规范',
				# ~ 'Programing recommendations':'操作失误删除了',
				# ~ 'Global Variable Names':'全局变量名',
				# ~ 'Function Annotation':'功能注释',
				# ~ 'Indentation':'缩进',
				# ~ 'Binary Operatoe':'运算符',
				# ~ 'string quotes':'字符串引号'}
				
# ~ #.item()不要忘记，调用字典中的键值对
# ~ for word,explanation in python_words.items():
	# ~ print("\n"+word+":")
	# ~ print(explanation)

# ~ ##改写
# ~ from collections import OrderedDict
# ~ python_words = OrderedDict()
# ~ python_words['Code lay out']='代码布局'
# ~ python_words['Whitespaces in Expressions']='表达式中的空格'
# ~ python_words['Comments']='注释'
# ~ python_words['Naming Conventions']='命名规范'
# ~ python_words['Programing recommendations']='操作失误删除了'
# ~ python_words['Global Variable Names']='全局变量名'
# ~ python_words['Function Annotation']='功能注释'
# ~ python_words['Indentation']='缩进'
# ~ python_words['Binary Operatoe']='运算符'
# ~ python_words['string quotes']='字符串引号'

# ~ n=0
# ~ for word,explanation in python_words.items():
	# ~ print("\n"+word+":")
	# ~ print(explanation)
	# ~ n+=1

# ~ #9-14随机模拟骰子
# ~ from random import randint
# ~ ##测试一下这个函数的功能,必须多次调用函数不能直接多次使用print
# ~ x = randint(1,6)#闭区间
# ~ print(x)
# ~ x = randint(1,6)
# ~ print(x)
# ~ x = randint(1,6)
# ~ print(x)

##定义一个类，x面的骰子掷n次
# ~ from random import randint
# ~ class Die():
	# ~ def __init__(self,sides):
		# ~ self.sides=sides
		
	# ~ def roll_die(self):
		# ~ self.side=randint(1,self.sides)
		# ~ print(self.side)
		
	# ~ def roll_die_times(self,times):
		# ~ self.n=0
		# ~ self.times=times
		# ~ while self.n<self.times:
			# ~ self.roll_die()
			# ~ self.n+=1

# ~ x=Die(6) 
# ~ x.roll_die_times(10)
			
		
