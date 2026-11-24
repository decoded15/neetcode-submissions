class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        frq = {}
        for i in nums :
            frq[i] = frq.get(i,0) + 1
        
        index = 0

        for i in range(3):
            while frq.get(i, 0) > 0:
                nums[index] = i
                frq[i] -= 1
                index += 1
        