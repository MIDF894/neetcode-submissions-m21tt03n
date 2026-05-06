class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lst = list()
        for i in range(len(nums)):
            for n in range(len(nums)):
                if i == n:
                    continue
                elif (nums[i] + nums[n]) == target:
                    lst = [i, n]
                    return lst