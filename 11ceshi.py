# ~ #11-1
# ~ import unittest
# ~ from chengshi_guojia_11 import city_function

# ~ class CityFunctionTest(unittest.TestCase):
	# ~ """测试11.py"""
	# ~ def test_city_function(self):
		# ~ """能够正确的处理吉林 中国这样的"""
		# ~ jieguo = city_function("吉林",'中国')
		# ~ self.assertEqual(jieguo,"吉林-中国")

# ~ unittest.main()

	
# ~ #11-2
# ~ import unittest
# ~ from chengshi_guojia_11 import city_function

# ~ class CityFunctionTest(unittest.TestCase):
	# ~ """测试11.py"""
	# ~ def test_city_function(self):
		# ~ """能够正确的处理吉林 中国这样的"""
		# ~ jieguo = city_function("吉林",'中国',"2717w")
		# ~ self.assertEqual(jieguo,"吉林-中国-2717w")

# ~ unittest.main()


#11-3
import unittest
from employee_11 import Employee

def setUp(self):
	"""创建一组数据，提供测试使用"""
	xing="zhang"
	ming="jie"
	xinshui="10000"
	self.employee=Employee(xing.ming,xinshui)
	self.zengzhang=[10000]
	self.yuce=[15000,25000]

def test_morezengzhang(self):
	self.employee.give_riase()
	self.assertEqual(self.employee.xinshui,self.yuce[0])
	
def test_zhidingzengzhang(self):
	self.employee.give_raise(self.zengzhang[0])
	self.assertEqual(self.employee.xinshui,self.yuce[1])
	
unittest.main()
	
	

	
