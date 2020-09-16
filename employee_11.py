class Employee():
	def __init__(self,xing,ming,xinshui):
		self.xing = xing
		self.ming = ming
		self.xinshui = int(xinshui)
	
	def give_raise(self,zengzhang=5000):
		self.xinshui += int(zengzhang)
		
		
A=Employee("zhang","jie","10000")
B=A.xinshui
print(B)
A.give_raise()
C=A.xinshui
print(C)
A.give_raise(10000)
D=A.xinshui
print(D)
