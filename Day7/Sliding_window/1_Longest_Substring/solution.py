class Solution(object):
    def lengthOfLongestSubstring(self, s):

        seen = {}
        start = 0
        max_len = 0

        for end, char in enumerate(s):

            if char in seen and seen[char] >= start:
                start = seen[char] + 1

            seen[char] = end

            current_len = end - start + 1

            if current_len > max_len:
                max_len = current_len

        return max_len