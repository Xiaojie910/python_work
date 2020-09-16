class Restaurant():#注意大小写
	"""模拟饭店调查"""
	
	def __init__(self,restaurant_name,cuisine_type):#init俩边分别是俩个下划线
		self.name=restaurant_name
		self.type=cuisine_type
		
	def describe_restaurant(self):##self不要忘记
		print(self.name + "的"+self.type + "很不错哦")
		
	def open_restaurant(self):
		print("而且他正在营业")
