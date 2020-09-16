from user import User
class Admin(User):
	"""特殊用户，管理员"""
	def __init__(self,xing,ming,*qita):
		#初始化父类参数
		super().__init__(xing,ming,*qita)
		#利用super建立联系
	
	def show_privileges(self):
		Privileges()


class Privileges():
	"""管理人员特权"""
	def __init__(self):
		self.privileges="和稀泥"
		print("\n管理员能"+self.privileges)

dalao=Admin('张','杰','帅啊','机智','成功')
dalao.show_privileges()
