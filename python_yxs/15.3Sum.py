class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #返回列表
        rlist = []
        #实参列表排序
        nums.sort()

        for i in range(len(nums)):
        	#判断每一轮首元素是否大于0,是则无需继续查找
        	if nums[i] > 0:
        		break
        	#判断相邻两个元素是否相同,是则只查找一个
        	#值得注意的是：这里使用前一个查找忽略后一个，就是为了防止漏找
        	if i > 0 and nums[i] == nums[i-1]:
        		continue  #直接进入下一次循环
            #j指针表示从前往后
        	j = i + 1
        	#k指针表示从后往前
        	k = len(nums)-1
        	while j < k:
        		#恰好三个数之和等于0
        		if nums[i] + nums[j] + nums[k] == 0:
        			#将结果添加进返回数组
        			rlist.append([nums[i],nums[j],nums[k]])
        			#相等时去除重复
        			while j < k and nums[j] == nums[j+1]:
        				j = j + 1
        			while j < k and nums[k] == nums[k-1]:
        				k = k - 1
        			#最后一轮需要继续跳到下一个数
        			j = j + 1
        			k = k - 1
        		#三数之和大于0
        		elif nums[i] + nums[j] + nums[k] > 0:
        			k = k - 1  #尾指针前移
        		elif nums[i] + nums[j] + nums[k] < 0:
        			j = j + 1  #首指针后移

        return rlist

#2018.11.07
#------------------主函数-----------------------

if __name__ == '__main__':
	sl = Solution()
	l = sl.threeSum([1,1,2,-1,0,-1,-4,-2,3,1,4])
	print(l)
