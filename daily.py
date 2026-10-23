class Solution(object):
    def sumCounts(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l1=[]
        for i in range(len(nums-1)):
            for j in range(len(nums)):
                if nums[i]==nums[j]:
                    l1.append(nums[i])
                    l1.append(nums[j])

obj=Solution()
obj.sumCounts()