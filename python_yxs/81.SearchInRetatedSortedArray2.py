class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        length = len(nums)
        if length == 0:
            return False
        fir = 0
        end = length-1
        while fir <= end:
            point = 0 #设置判断点
            mid = (fir+end)//2
            for i in range(mid,end):  #确保后面是否有序
                    if nums[i] > nums[i+1]:
                        point = 1
            if nums[mid] == target:
                return True
            elif nums[mid] <= nums[end] and point == 0: #表示后面为有序(可能重复)
                if nums[mid] < target and target <= nums[end]:
                    fir = mid + 1
                else:
                    end = mid - 1
            else:
            # elif nums[mid] >= nums[fir]:
                if nums[mid] > target and target >= nums[fir]:
                    end = mid - 1
                else:
                    fir = mid + 1
        return False
#2018.11.29
#---------------main function----------------
if __name__ == '__main__':
    l = [2,5,6,0,0,1,2]
    # l = [3,1,1]
    # l = [1,1,1,2,3,1]
    # l = [1,1,3,1]
    target = 3
    s = Solution()
    print(s.search(l,target))