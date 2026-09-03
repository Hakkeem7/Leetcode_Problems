class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""

        need = {}

        for ch in t:
            need[ch] = need.get(ch, 0) + 1

        window = {}

        left = 0
        have = 0
        need_count = len(need)

        best_len = float("inf")
        best_start = 0

        for right in range(len(s)):
            ch = s[right]

            window[ch] = window.get(ch, 0) + 1

            if ch in need and window[ch] == need[ch]:
                have += 1

            while have == need_count:

                if right - left + 1 < best_len:
                    best_len = right - left + 1
                    best_start = left

                left_ch = s[left]
                window[left_ch] -= 1

                if left_ch in need and window[left_ch] < need[left_ch]:
                    have -= 1

                left += 1

        if best_len == float("inf"):
            return ""

        return s[best_start:best_start + best_len]