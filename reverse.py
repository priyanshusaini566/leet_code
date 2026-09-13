class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s1=""
        s = " ".join(s.split())
        s=s.split()

        s.reverse()

        for item in s:
            s1=s1+item
            s1=s1+" "
            
        return s1.strip()

obj=Solution()
print(obj.reverseWords("the sky is blue"))