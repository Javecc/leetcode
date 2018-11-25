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
        self._head = head

    def is_empty(self):
        """链表判断是否为空"""
        if self._head is None:
            return True
        else:
            return False

    def length(self):
        """链表长度"""

    def append(self, elem):
        """追加元素"""
        if self._head is None:
            self._head = elem
        else:
            


if __name__ == '__main__':
    # head = Node()
    head = None
    ssl = SingleLinkList(head)
    print(ssl.is_empty())