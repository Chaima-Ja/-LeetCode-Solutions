class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        filtered_chars = ''.join(c.lower() for c in s if c.isalnum())
        return filtered_chars == filtered_chars[::-1]
