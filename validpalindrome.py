class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s=s.lower()
        s1=""

        for item in s:
            if item.isalnum():
                s1=s1+item
            else:
                continue

        rev=s1[::-1]
        if rev==s1:
            return True
        else:
            return False

obj=Solution()
print(obj.isPalindrome("A man, a plan, a canal: Panama"))          