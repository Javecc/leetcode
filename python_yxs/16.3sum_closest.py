class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        rsum = sum(nums[:3])
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                temp = nums[i] + nums[j] + nums[k]
                if abs(rsum - target) > abs(temp - target):
                    rsum = temp
                elif temp > target:
                    k = k - 1
                else:
                    j = j + 1
        return rsum
#2018.11.08

#-----------------官方主函数-------------------

def stringToIntegerList(input):
    return json.loads(input)

def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            nums = stringToIntegerList(line);
            line = next(lines)
            target = int(line);
            
            ret = Solution().threeSumClosest(nums, target)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()