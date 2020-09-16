def bubble_sort(alist):
    """冒泡排序"""
    n = len(alist)
    for j in range(n-1):
        count = 0
        for i in range(0,n-1-j):
            #从头到尾
            if alist[i] > alist[i+1]:
                alist[i],alist[i+1] = alist[i+1],alist[i]
                count += 1
        if count == 0:
            return


# i 0~n-2  range(0,n-1)  j = 0
# i 0~n-3  range(0,n-1-1)  j = 1
# i 0~n-4  range(0,n-1-2)  j = 2
# ...
# j = n i range(0,n-1-j)
if __name__ == "__main__":
    li = [52,12,84,56,89,13,15,64,75]
    print(li)
    bubble_sort(li)
    print(li)