# ~ #8-1
# ~ def display_message():
	# ~ print("颤抖吧函数，我要来学你咯!")
# ~ display_message()

# ~ #8-2 喜欢的图书
# ~ def favorite_book(book):
	# ~ print(book+"这本书老好了，我最喜欢这本书了！")
# ~ favorite_book("老人与海")

#8-3 打印衬衫
# ~ def make_shirt(size,word):
	# ~ if size =='X':
		# ~ print(word)
		# ~ print("一起啃书！")
	# ~ if size =="M":
		# ~ print(word)
		# ~ print("加油我的小宝贝！")
	# ~ if size =="L":
		# ~ print(word)
		# ~ print("勇往直前，决不放弃！")
# ~ make_shirt("奋发图强","X")
# ~ make_shirt(size="M",word="革命尚未成功，同志们仍需努力！")

#8-4 8-3的变形
# ~ def make_shirt(size,word="我爱学习"):
	# ~ if size =='X':
		# ~ print(word)
		# ~ print("一起啃书！")
	# ~ if size =="M":
		# ~ print(word)
		# ~ print("加油我的小宝贝！")
	# ~ if size =="L":
		# ~ print(word)
		# ~ print("勇往直前，决不放弃！")
# ~ make_shirt("X")
# ~ make_shirt("M",word="革命尚未成功，同志们仍需努力！")

# ~ #8-5
# ~ def describe_city(city,country="China"):
	# ~ print(city+"在"+country+"！")
# ~ describe_city("hangzhou")
# ~ describe_city("shanghai")
# ~ describe_city("wangchuan","广莫之野无何有之乡")

# ~ #8-6 renturn返回值的用法 
# ~ def describe_city(city,country="China"):
	# ~ city_country = city+","+country
	# ~ return city_country
# ~ city_country_liaoning = describe_city("liaoning")
# ~ print(city_country_liaoning)

# ~ #8-7 返回字典
# ~ def make_album(singer,special_edition):
	# ~ music = {}
	# ~ music['singer']=singer
	# ~ music['special_edition']=special_edition
	# ~ print(music)
# ~ make_album("周杰伦",'依然范特西')
# ~ make_album('周杰伦','摩羯座')
# ~ make_album('周杰伦','青花瓷')

#8-8运用while循环
# ~ def make_album(singer,special_edition):
	# ~ music = {}
	# ~ music['singer']=singer
	# ~ music['special_edition']=special_edition
	# ~ print(music)

# ~ print("输入你喜欢的歌手，输入'q'退出 ")
# ~ while True:
	# ~ singer = input('你喜欢的歌手是: ')
	# ~ if singer == 'q':
		# ~ break
	# ~ else:
		# ~ special_edition = input('他的一个专辑是: ')
		# ~ if special_edition =="q":
			# ~ break
		# ~ else:
			# ~ make_album(singer,special_edition)

# ~ #8-9打印列表
# ~ def print_book_list(book_list):
	# ~ for book in book_list:
		# ~ print(book)
# ~ python_book_list=['python从入门到实践','python基础教程','python强化学习']
# ~ print_book_list(python_book_list)

# ~ #8-10利用函数对列表进行修改
# ~ def print_book_list(book_list):
	# ~ """打印列表"""
	# ~ for book in book_list:
		# ~ print(book)
# ~ def change_book_list(book_list): 
	# ~ """修改列表"""
	# ~ n = 0
	# ~ while n<len(book_list):
		# ~ book_list[n] = '推荐'+book_list[n]
		# ~ n+=1
	# ~ print_book_list(book_list)
# ~ python_book_list=['python从入门到实践','python基础教程','python强化学习']
# ~ change_book_list(python_book_list)

# ~ #8-11 8-10变形
# ~ def print_book_list(book_list):
	# ~ """打印列表"""
	# ~ for book in book_list:
		# ~ print(book)
# ~ def change_book_list(book_list): 
	# ~ """修改列表"""
	# ~ n = 0
	# ~ while n<len(book_list):
		# ~ book_list[n] = '推荐'+book_list[n]
		# ~ n+=1
	# ~ print_book_list(book_list)
# ~ python_book_list=['python从入门到实践','python基础教程','python强化学习']
# ~ change_book_list(python_book_list[:])
# ~ print_book_list(python_book_list)

# ~ #8-12 输入任意数量实参，三明治里面加什么
# ~ def sandwich(*foods):
	# ~ print('您要的三明治加的材料：')
	# ~ for food in foods:
		# ~ print('-'+food)
		
# ~ sandwich('guojiang','naiyou','huotui')

# ~ #8-13
# ~ def build_profile(first,last,**user_info):
	# ~ profile={}
	# ~ profile['first_name']=first
	# ~ profile['last_name']=last
	# ~ for key,value in user_info.items():
		# ~ profile[key]=value
	# ~ return profile
# ~ wo=build_profile('zhijing','dashen',tezheng="mei",aihao="piaoliang")
# ~ print(wo)

# ~ #8-14 8-13修改即可
# ~ def cars(brand,types,**car_info):
	# ~ vehicle={}
	# ~ vehicle['牌子']=brand
	# ~ vehicle['型号']=types
	# ~ for key,value in car_info.items():
		# ~ vehicle[key]=value
	# ~ return vehicle
# ~ che=cars('aima','diandongche',daiyan="zhoujielun",yanse="wucaibanlan")
# ~ print(che)

#8-15实现的功能是导入8.4.1的函数

#8-16
#导入模块
import pizza
pizza.make_pizza(16,'naiyou')

#模块中导入函数
from pizza import make_pizza
make_pizza(16,'naiyou')

#模块中导入函数并修改函数名
from pizza import make_pizza as mp
mp(16,'naiyou')

#导入模块并修改模块名
import pizza as p
p.make_pizza(16,'naiyou')

#导入模块中所有函数
from pizza import *
make_pizza(16,'naiyou')
