class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        if len(t) > len(s):
            return ""

        need = {}

        for ch in t:
            need[ch] = need.get(ch, 0) + 1

        left = 0
        have = 0
        required = len(need)

        window = {}
        min_length = float('inf')
        start = 0

        for right in range(len(s)):
            ch = s[right]
            window[ch] = window.get(ch, 0) + 1

            if ch in need and window[ch] == need[ch]:
                have += 1

            while have == required:
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    start = left

                left_ch = s[left]
                window[left_ch] -= 1

                if left_ch in need and window[left_ch] < need[left_ch]:
                    have -= 1

                left += 1

        if min_length == float('inf'):
            return ""

        return s[start:start + min_length]

obj=Solution()
print(obj.minWindow('ADOBEGANBPC','ABC'))