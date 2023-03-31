"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """

        # approach: use recursion on each child

        if not root:
            return []

        result = []
        if root.children:
            for node in root.children:
                result.extend(self.preorder(node))

        return [root.val] + result