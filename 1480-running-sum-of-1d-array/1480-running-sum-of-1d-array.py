class Solution(object):
    def runningSum(self, nums):
        l=[]
        fois=0
        for i in nums:
            fois+=i
            l.append(fois)
        return l
