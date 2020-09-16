class Stack(object):
    """栈"""
    def __init__(self):
        self.__list = []

    def push(self,item):
        """添加一个新的元素item到栈顶"""
        self.__list.append(item)

    def pop(self):
        """弹出元素"""
        return self.__list.pop()

    def peek(self):
        """返回栈顶元素"""
        if self.__list:
            return self.__list[-1]
        else:
            return None
    def is_empty(self):
        """判断栈是否为空"""
        return self.__list == []
        #先计算self.__list中的值，在判断是否与[]相等，如果相等返回true，否则返回false

    def size(self):
        """返回栈的元素个数"""
        return len(self.__list)

if __name__ == "__main__":
    s = Stack()