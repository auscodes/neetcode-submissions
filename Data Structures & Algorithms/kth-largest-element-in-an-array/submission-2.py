class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        k = len(nums) - k
        
        def dfs(l, r):
            pivot = nums[r]
            p = l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]

            if p > k:
                return dfs(l, p - 1)
            elif p < k:
                return dfs(p + 1, r)
            else:
                return nums[p]

        return dfs(0, len(nums) - 1)



    