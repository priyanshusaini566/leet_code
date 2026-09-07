class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        maxcount=0
        for i in range(len(nums)):
            if nums[i]==1:
                count+=1
                maxcount=max(maxcount,count)

            elif nums[i]==0:
                count=0

        return maxcount
        
obj=Solution()
print(obj.findMaxConsecutiveOnes([1,0,1,1,1,0,1]))