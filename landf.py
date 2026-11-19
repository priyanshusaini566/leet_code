class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        low=0
        high=len(nums)-1
        first=-1

        while(low<=high):
            mid=(low+high)//2
            if nums[mid]==target:
                first=mid
                high=mid-1

            elif nums[mid]<target:
                low=mid+1

            else:
                high=mid-1

        low=0
        high=len(nums)-1
        last=-1

        while(low<=high):
            mid=(low+high)//2

            if nums[mid]==target:
                last=mid
                low=mid+1

            elif nums[mid]<target:
                low=mid+1
            else:
                high=mid-1

        return [first,last]


obj=Solution()
print(obj.searchRange(8,[1,2,3,5,8,6,5,8,44]))