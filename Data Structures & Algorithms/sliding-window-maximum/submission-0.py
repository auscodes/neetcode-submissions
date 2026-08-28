class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        res = []
        max_so_far = max(nums[:k])
        max_index = nums[:k].index(max_so_far)
        res.append(max_so_far)

        l = 0

        for r in range(k, len(nums)):
            l += 1

            # current max out of window:
            if max_index < l:
                max_so_far = nums[l]
                max_index = l

                for i in range(l + 1, r + 1):
                    if nums[i] >= max_so_far:
                        max_so_far = nums[i]
                        max_index = i

            # current max is still inside
            elif nums[r] >= max_so_far:
                max_so_far = nums[r]
                max_index = r

            res.append(max_so_far)

        return res