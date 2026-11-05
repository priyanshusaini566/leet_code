class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        l1=s.split()
        siz=len(l1)

        return len(l1[siz-1])


obj=Solution()
print(obj.lengthOfLastWord("Hello World"))
