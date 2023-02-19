class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, k):
        
        dictionary={}
        for num in arr:
            if num not in dictionary:
                dictionary[num]=1
            else:
                dictionary[num]+=1
        count=len(dictionary)
        for frequency in sorted(dictionary.values()):
            k-=frequency
            if(k<0):
                return count
            else:
                count-=1
        return count