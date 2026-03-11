from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        window = {}

        need_count = len(t)
        have = 0

        left = 0
        best_len = float(inf)
        best_start = 0

        for right in range(len(s)):
            # expand window
            c = s[right]
            window[c] = window.get(c, 0) + 1

            if c in need and window[c] <= need[c]:
                have +=1

            while have == need_count:
                # update best window
                if right-left+1 < best_len:
                    best_len = right-left+1
                    best_start = left

                left_c = s[left]
                window[left_c] -= 1

                if left_c in need and window[left_c] < need[left_c]:
                    have -= 1

                #shrink window
                left += 1        

        if best_len == float('inf'): return ""

        return s[best_start : best_start + best_len]
