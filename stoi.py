class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s1=[]
        s=list(s.strip())
        for item in s:
            if type(item)==int:
                s1.append(item)

        return s1

        