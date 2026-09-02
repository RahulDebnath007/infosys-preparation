class Solution:
    def longestOnes(self, nums, k):

        left = 0
        zero_count = 0
        max_length = 0

        for right in range(len(nums)):

            # Expand window
            if nums[right] == 0:
                zero_count += 1

            # Shrink if we have too many zeros
            while zero_count > k:

                if nums[left] == 0:
                    zero_count -= 1

                left += 1

            # Window is valid
            max_length = max(max_length, right - left + 1)

        return max_length