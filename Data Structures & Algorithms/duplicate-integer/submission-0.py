class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in nums:
            counter = 0
            for n in nums:
                if i == n:
                    counter += 1
            if counter > 1:
                return True
        return False