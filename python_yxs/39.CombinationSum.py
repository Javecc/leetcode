class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
    #     candidates.sort()
    #     answer = []
    #     result = []
    #     self.compute(candidates,target,0,answer,result)
    #     return result
    
    # def compute(self,candidates,target,start,answer,result):
    #     for i in range(start,len(candidates)):
    #         if target>0:
    #             answer.append(candidates[i])
    #             self.compute(candidates,target-candidates[i],i,answer,result)
    #             answer.pop()
    #         elif target<0:
    #             return
    #         else:
    #             temp = answer[:]
    #             result.append(temp)
    #             return
        candidates.sort()
        def findSum(cans, tar):
            result_list = []
            for i, can in enumerate(cans):
                # print(cans, tar)
                can = cans[i]
                if tar == can:
                    result_list.append([can])
                elif tar > can:
                    found = findSum(cans[i:], tar - can)
                    if found:
                        for sum_list in found:
                            sum_list.append(can)
                            result_list.append(sum_list)
                else:
                    return result_list
            return result_list
        return findSum(candidates, target)

#2018.11.15
if __name__ == '__main__':
	l = [1,2,3,4,5,6,7,8,9,10]
	target = 10
	s = Solution()
	print(s.combinationSum(l,target))

       