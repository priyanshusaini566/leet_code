class Solution(object):
    def maxFreqSum(self, s):
        """
        :type s: str
        :rtype: int
        """
        max1=0
        max2=0
        for item in s:
            if item in "aeiou":
                count=s.count(item)
                if count>=max1:
                    max1=count

            else:
                c2=s.count(item)
                if c2>=max2:
                    max2=c2

        return max1+max2

obj=Solution()
str=input("Enter the string : ")
print(obj.maxFreqSum(str))