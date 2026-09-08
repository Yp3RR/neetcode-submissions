class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        p = {}
        for i,num in enumerate(nums):
            temp = target - num
            if temp in p:
                return [p[temp],i]
            else:
                p[num] = i