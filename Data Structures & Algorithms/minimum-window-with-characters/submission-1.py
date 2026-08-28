class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        count_t, window = {}, {}

        # store count of each char in t
        for c in t:
            count_t[c] = 1 + count_t.get(c, 0)

        have = 0
        need = len(count_t)
        res = [-1, -1]
        res_len = float('inf')

        l = 0
        for r in range(len(s)):
            # store in window
            window[s[r]] = 1 + window.get(s[r], 0)
            # increment have if matches
            if s[r] in count_t and window[s[r]] == count_t[s[r]]:
                have += 1

            while have == need: # means we found valid window
                # store our results
                if r - l + 1 < res_len:
                    res_len = r - l + 1
                    res = [l, r]

                # start shrinking left window
                window[s[l]] -= 1
                if s[l] in count_t and window[s[l]] < count_t[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        if res_len == float('inf'):
            return ""
        else:
            return s[l : r + 1]