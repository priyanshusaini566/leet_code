class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        new=nums1+nums2
        new.sort()


        size=len(new)
        med=size//2
        if size%2!=0:
         return new[med]

        else:
          return (new[med]+new[med-1])/2
          
        