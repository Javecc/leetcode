# coding:utf-8
from timeit import timer
# li1 = [1,2]
# li2 = [23,5]
# li = li1 + li2
# li = [i for i in range(10000)] 
def test1():
	li = []
	for i in range(10000):
		li.append(i)

def test2():
	li = []
	for i in range(10000):
		li += [i]

def test3():
	li = [i for i in range(10000)]

def test4():
	li = list(range(10000))
#timer class
timer1 = timer("test1()","from __name__ import test1")
print("+:",timer1.timeit(1000))