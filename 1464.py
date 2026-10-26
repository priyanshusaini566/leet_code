class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l1=[]
        i=max(nums)
        l1.append(i-1)

        nums.remove(i)
        a=max(nums)

        l1.append(a-1)

        return l1[0]*l1[1]
        
obj=Solution()
print(obj.maxProduct([1,2,3,3]))