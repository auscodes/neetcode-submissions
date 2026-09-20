class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for num in nums:
            for subset in list(res):
                res.append(subset + [num])

        return res