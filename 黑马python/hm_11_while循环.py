"""
while 条件：
条件成立执行代码
"""
# #需求：重复打印5次
# i = 0
# while i < 5:
#     print("老婆,我错了！")
#     i += 1 #i = i+1
# print("任务结束")

# #需求：1到100累加，并计算结果
#
# #准备数据
# i = 1
#
# #储存结果
# result = 0
# #循环
# while i <= 100:
#     result += i
#     i += 1
# print(result)

# #1-100偶数累加
# i = 1
# result = 0
# while i <= 100:
#     if i % 2 ==0:
#         result += i
#     i += 1
# print(result)

# #break 退出循环的的方式，终止全部循环
# i = 1
# while i <= 5:
#     if i == 4:
#         print(f'吃饱了不吃第{i+1}个了')
#         break
#     print(f"吃了第{i}个苹果")
#     i += 1

# #continue退出循环，退出当前循环
# i = 1
# while i <= 5:
#     if i == 3:
#         print(f'吃到了一个虫子，这个苹果不吃了，开始吃第{i+1}个苹果')
#         #continue之前要修改计数器
#         i += 1
#         continue
#     print(f'吃了第{i}个苹果')
#     i += 1


#while循环嵌套应用打印99乘法表
j = 1
while j <= 9:
    #一行的表达式开始
    i = 1
    while i <= j:
        print(f'{i} * {j} = {i*j}',end='\t')
        i += 1
    #一行的表达式结束
    print()
    j += 1
