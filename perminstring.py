class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        k=len(s1)

        if k>len(s2):
            return False

        for i in range(len(s2)-k+1):
            s3=s2[i:i+k]
            
            if sorted(s3)==sorted(s1):
                return True
                
            
        return False


        
obj=Solution()
print(obj.checkInclusion("acp","qwertabcuiop"))