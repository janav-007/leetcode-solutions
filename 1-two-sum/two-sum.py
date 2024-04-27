class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        for i in range(0,len(nums)):
            k = target - nums[i]
            if(k in nums and nums.index(k)!=i):
                ans.append(nums.index(k))
                ans.append(i)
                break
        return ans