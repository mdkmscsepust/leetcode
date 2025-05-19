class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        list = {}
        for i,item in enumerate(nums):
            result = target - item 
            if result in list:
                return [list[result],i]
            list[item]=i
        return []