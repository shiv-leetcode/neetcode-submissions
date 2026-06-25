class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsMap = {}

        for i, n in enumerate(nums):
            complement = target - n

            if complement in numsMap:
                return [numsMap[complement], i]
            
            numsMap[n] = i
        
        return []