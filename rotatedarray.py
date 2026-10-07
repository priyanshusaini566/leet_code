class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        flag=False
        for i in range(len(nums)):
            if nums[i]==target:
                flag=True
                value=i
            else:
                continue

        if flag==True:
            return value
        else:
            return -1


obj=Solution()
print(obj.search([1,2,3,0,5,6],0))