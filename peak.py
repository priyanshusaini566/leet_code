class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max=0
        for i in range(len(nums)):
            if nums[i]>nums[max]:
              max=i

        return max


obj=Solution()
print(obj.findPeakElement([1,5,3,7,9]))