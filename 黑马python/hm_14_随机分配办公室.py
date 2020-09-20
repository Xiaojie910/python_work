"""
需求：将8位老师随机分配到3个办公室
"""
import random
teachers = ['A','B','C','D','E','F','G','H']
offices = [[],[],[]]

for name in teachers:
    #随机挑选办公室加入老师
    num = random.randint(0,2)
    offices[num].append(name)

#把各个办公室字列表添加一个办公室编号1,2,3
i = 1
for office in offices:
    print(f"办公室{i}的人数是{len(office)},老师分别是：")
    for name in office:
        print(name)
    i += 1