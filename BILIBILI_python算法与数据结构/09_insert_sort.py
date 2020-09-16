def insert_sort(alist):
    """插入排序"""
    n = len(alist)
    #外循环是从右边的无序序列中取出多个元素执行下列操作
    for j in range(1,n):
        #i代表内存循环的起始值
        i = j
        #执行从右边的无序序列中，即i位置的元素，然后将其插入到正确的位置中
        while i > 0:
            if alist[i] < alist[i-1]:
                alist[i],alist[i-1] = alist[i-1],alist[i]
                i -=1
            else:
                break

if __name__ == "__main__":
    li = [52,12,84,56,89,13,15,64,75]
    print(li)
    insert_sort(li)
    print(li)