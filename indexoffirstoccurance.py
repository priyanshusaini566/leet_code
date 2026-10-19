class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        size=len(needle)
        l1=list(needle)
        p=-1
        for i in range(len(haystack)):
            if haystack[i]==l1[0]:
                s2=haystack[i:(i+size)]
                if s2==needle:
                    p=i
                    break

        return p
        
obj=Solution()
print(obj.strStr("sadbutsad","sad"))
