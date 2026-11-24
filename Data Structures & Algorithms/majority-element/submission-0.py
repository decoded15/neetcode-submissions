class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = dict()
        m = len(nums) // 2
        for i in nums :
            freq[i] = freq.get(i,0) + 1
        for i in freq :
            if freq[i] >= m :
                return i
        return nums[0]
