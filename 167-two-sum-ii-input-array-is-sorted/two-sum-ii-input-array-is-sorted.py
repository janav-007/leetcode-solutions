class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        for i in range(0,len(nums)):
            k = target - nums[i]
            if(k in nums and nums.index(k)!=i):
                idx1 = i + 1
                idx2 = nums.index(k) + 1
                ans.append(min(idx1, idx2))
                ans.append(max(idx1, idx2))
                break
        return ans