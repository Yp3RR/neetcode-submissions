class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        p = {}
        for num in nums:
            p[num] = p.get(num, 0) + 1

        freq_bucket = [[] for _ in range(len(nums)+1)]

        for num,count in p.items():
            freq_bucket[count].append(num)
        
        for i in range(len(freq_bucket)-1,0,-1):
            for num in freq_bucket[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans
                