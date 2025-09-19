class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        tempdict = {}
        for i in range(len(nums)):
            if nums[i] not in tempdict:
                tempdict[nums[i]] = 0

            else:
                return True

        return False

      



        
