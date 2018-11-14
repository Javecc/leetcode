class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)
        for i in range(length):
        	for j in range(i+1,length):
        		matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        for i in range(length):
        	matrix[i] = matrix[i][::-1]
#2018.11.14

if __name__ == '__main__':
	s = Solution()
	l = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
	for i in range(len(l)):
		print(l[i])
	print("--------------------")
	s.rotate(l)
	for i in range(len(l)):
		print(l[i])
