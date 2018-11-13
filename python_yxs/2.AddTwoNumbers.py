# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        #将两个单链表的数存进列表
        listnum1 = []
        listnum2 = []
        while l1 != None:
        	listnum1.append(l1.val)
        	l1 = l1.next
        while l2 != None:
        	listnum2.append(l2.val)
        	l2 = l2.next

        #将两个数同整型num1和num2表示出来
        num1 = 0
        num2 = 0
        for i in range(len(listnum1)):
        	num1 = num1 + listnum1[i] * (10 ** i)
        for j in range(len(listnum2)):
        	num2 = num2 + listnum2[j] * (10 ** j)

        #计算结果后，构造结果的单链表结构l3
        result = num1 + num2
        l3 = ListNode(0)  #初始化返回链表
        p = ListNode(0)   #初始化指针结点
        p = l3
        while result >= 10:
        	temp = ListNode(None)
        	p.val = result % 10
        	p.next = temp 
        	p = temp
        	result = result // 10
        #最后一轮留下最高位数
        p.val = result % 10

        return l3

#2018.11.05

#-------------------官方主函数------------------------

def stringToListNode(input):
    # Generate list from the input
    numbers = json.loads(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr

def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            line = lines.next()
            l1 = stringToListNode(line)
            line = lines.next()
            l2 = stringToListNode(line)
            
            ret = Solution().addTwoNumbers(l1, l2)

            out = listNodeToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()