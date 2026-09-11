class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        l=s.split()
        return len(l[-1])



obj=Solution()
print(obj.lengthOfLastWord("Hello World"))