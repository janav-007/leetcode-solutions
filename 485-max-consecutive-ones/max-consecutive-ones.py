class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        i = 0
        count = 0
        counter = []
        while i < len(nums):
            if nums[i] == 1:
                count += 1
            else:
                counter.append(count)
                count = 0
            i += 1
        counter.append(count)
        return max(counter)