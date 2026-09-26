class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        count=0
        n=x
        flag=False

        while x>0:
            r=x%10
            count=count*10+r
            x=x/10

        if count==n:
            flag=True

        else:
            flag=False

        return flag

        
obj=Solution()
print(obj.isPalindrome(121))     