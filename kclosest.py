class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        arr.sort(key=lambda a:(abs(a-x),a))

        ans=arr[:k]

        ans.sort()

        return ans


obj=Solution()
print(obj.findClosestElements([1,2,3,4,5],4,3))