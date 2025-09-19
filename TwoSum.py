class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashe = {}
        for i in range(len(nums)):
            hashe[nums[i]] = i

        for j in range(len(nums)):
            if ((target - nums[j]) in hashe) == True and j != hashe.get(target-nums[j]):
                return [j, hashe.get(target-nums[j])]
