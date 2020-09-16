class User():
	"""记录用户的信息"""
	def __init__(self,xing,ming,*qita):
		self.xing=xing
		self.ming=ming
		self.qita=qita
	
	def describe_user(self):
		print("姓："+self.xing)
		print("名："+self.ming)
		if self.qita:
			print("\n其他信息如下：\n")
			for info in self.qita:
				print("-"+info)
	
	def greet_user(self):
		print("\n"+"小"+self.ming + "，我们奶你！")
		print("小"+self.ming + "，你老霸道了！")
