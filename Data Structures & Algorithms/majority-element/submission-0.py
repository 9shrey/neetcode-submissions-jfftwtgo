class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)
        res = maxC = 0
        for num in nums:
            count[num]+=1
            if maxC < count[num]:
                res = num
                maxC = count[num]
        return res
