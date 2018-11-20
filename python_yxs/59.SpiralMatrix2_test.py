class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        def listAppend(row,column,x,y,case,num):
        	if row == 0 or column == 0:
        		return
        	#从左向右移动
        	if case == 0:
        		endy = y + column
        		for i in range(y,endy):
        			rlist[x][i] = num
        			num += 1
        		row -= 1
        		x += 1
        		y = endy - 1
                #listAppend(row,column,x,y,1,num)
        	#从上向下移动
        	# elif case == 1:
        	# 	endx = x + row
        	# 	for i in range(x,endx):
        	# 		rlist[i][y] = num
        	# 		num += 1
        	# 	column -= 1
        	# 	x = endx - 1
        	# 	y -= 1
        	# 	listAppend(row,column,x,y,2,num)
        	# #从右往左移动
        	# elif case == 2:
        	# 	endy = y - column
        	# 	for i in range(y,endy,-1):
        	# 		rlist[x][i] = num
        	# 		num += 1
        	# 	row -= 1
        	# 	x -= 1
        	# 	y = endy + 1
        	# 	listAppend(row,column,x,y,3,num)
        	# #从下往上移动
        	# elif case == 3:
        	# 	endx = x - row
        	# 	for i in range(x,endx,-1):
        	# 		rlist[i][y] = num
        	# 		num += 1
        	# 	column -= 1
        	# 	x = endx + 1
        	# 	y += 1
        	# 	listAppend(row,column,x,y,0,num)

        #初始化ReturnList
        rlist = []
        ls = []
        for i in range(n):
        	ls.append(0)
        for i in range(n):
        	rlist.append(ls)
        row,column = n,n
        listAppend(row,column,0,0,0,1)
        return rlist 
#2018.11.20

#-------------------main function----------------------
if __name__ == '__main__':
	n = 4
	s = Solution()
	rlist = s.generateMatrix(n)
	#print(rlist)
	for i in range(n):
		print(rlist[i])