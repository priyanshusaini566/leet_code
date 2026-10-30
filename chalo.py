class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l1=[]
        size=len(nums)
        c=nums[size-2]
        nums[size-2]=nums[size-1]
        nums[size-1]=c

        return nums
        