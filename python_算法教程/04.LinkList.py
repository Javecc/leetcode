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
            print(point.elem)
            point = point.next

    def append(self, item):  #添加具体数据
        """追加元素"""
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
            

if __name__ == '__main__':
    # head = Node(100)
    # head = None
    ssl = SingleLinkList()
    print(ssl.is_empty())  #判空
    print(ssl.length())    #求长度
    ssl.travel()
    ssl.append(1)       #追加元素
    ssl.append(2)
    ssl.append(3)
    ssl.append(4)
    ssl.append(5)
    print(ssl.travel())