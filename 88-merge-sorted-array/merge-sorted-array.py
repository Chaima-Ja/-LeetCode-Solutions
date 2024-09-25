class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None
        """
        # Start from the end of nums1 and nums2
        p1 = m - 1  # Pointer for the last element in nums1's valid part
        p2 = n - 1  # Pointer for the last element in nums2
        p = m + n - 1  # Pointer for the last position in nums1

        # Merge in reverse order
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        # If there are still elements left in nums2, copy them
        # (nums1 doesn't need copying since it's already in place)
        nums1[:p2 + 1] = nums2[:p2 + 1]
