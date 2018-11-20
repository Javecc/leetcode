class Solution:
    def generateMatrix(self, n):

        def listAppend(column,x,y,case):
            num = 1
            if case == 0:
                for i in range(column):
                    rlist[0][i] = num
                    print(rlist[1])
                    num += 1

        #初始化ReturnList
        rlist = []
        ls = []
        for i in range(n):
            ls.append(0)
        for i in range(n):
            rlist.append(ls)
        for i in range(n):
            print(rlist[i])
        listAppend(n,0,0,0) 
        return rlist
if __name__ == '__main__':
    n = 4
    s = Solution()
    rlist = s.generateMatrix(n)
    print(rlist)
    #--------test----------
    # num = 1
    # ls = [[0,0,0],[0,0,0]]
    # for i in range(3):
    #     ls[1][i] = num
    #     num += 1
    # print(ls)