# coding:utf-8

class Node:
    """结点"""
    def __init__(self, elem):
        self.elem = elem
        self.next = None

class SingleLinkList:
    """单链表"""
    def __init__(self, head=None):
        """创建头结点"""
        self.__head = head

    def is_empty(self):
        """链表判断是否为空"""
        return self.__head is None

    def length(self):
        """链表长度"""
        length = 0
        point = self.__head   #遍历游标
        while point is not None:
            length += 1
            point = point.next
        return length

    def travel(self):
        """遍历元素"""
        point = self.__head
        while point is not None:
            print(point.elem,end=" ")
            point = point.next
        print("\n")

    def append(self, item):  #添加具体数据
        """追加元素，尾插法"""
        # 为何不行？
        # node = Node(item)
        # point = self._head
        # while point is not None:
        #     point = point.next
        # point = node
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            point = self.__head
            while point.next is not None:
                point = point.next
            point.next = node

    def add(self, item):
        """插入元素，头插法"""
        node = Node(item)
        point = self.__head
        self.__head = node
        node.next = point
    
    def insert(self, pos, item):
        """指定位置插入元素
        :param pos从0开始
        """ 
        if pos <= 0:  #小于等于0头插法
            self.add(item)
        elif pos > self.length(): #大于长度尾插法
            self.append(item)
        elif pos > 0 and pos < self.length():
            node = Node(item)
            point = self.__head
            for i in range(pos-1):
                point = point.next
            temp = point.next
            point.next = node
            node.next = temp
            # nothing
            # for i in range(pos):
            #     point = point.next
            # temp = point
            # point = node
            # node.next = temp

    def search(self, item):
        """查找结点是是否存在
           存在打印True+坐标，否则打印False
        """
        point = self.__head
        pos = 0
        while pos < self.length():
            if point.elem == item:
                print("True {}".format(pos))
                return 
            else:
                point = point.next
            pos += 1
        print("False")

    def remove(self, item):
        


if __name__ == '__main__':
    # head = Node(100)
    # head = None
    ssl = SingleLinkList(Node(10))
    print(ssl.is_empty())  #判空
    print(ssl.length())    #求长度
    ssl.travel()
    ssl.append(1)       #追加元素
    ssl.append(2)
    ssl.append(3)
    ssl.append(4)
    ssl.append(5)
    ssl.travel()
    ssl.add(7)
    ssl.add(8)
    ssl.travel()
    ssl.insert(6,11)
    ssl.travel()
    ssl.search(12)