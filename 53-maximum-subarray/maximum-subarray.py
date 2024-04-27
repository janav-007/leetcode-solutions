class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sub = nums[0]
        current_sub = 0
        for i in nums:
            if(current_sub < 0):
                current_sub = 0
            current_sub += i
            max_sub = max(max_sub, current_sub)
        return max_sub