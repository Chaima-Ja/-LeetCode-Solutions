class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_index = {}  # Stores the most recent index of each character
        max_length = 0
        start = 0  # Left pointer of the sliding window

        for end, char in enumerate(s):
            if char in char_index and char_index[char] >= start:
                # If the character is repeated, move the left pointer
                start = char_index[char] + 1
            char_index[char] = end
            max_length = max(max_length, end - start + 1)

        return max_length
