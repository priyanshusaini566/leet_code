class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """
        if int(num)%2!=0:
            return num
        else:
            l1=list(num)
            maximum=0
            for i in range(len(l1)):

                if int(l1[i])%2!=0:
                    maximum=i

            if maximum==0 and int(l1[0])%2==0:
                return ""
            else:
                return num[:maximum +1]



obj=Solution()
print(obj.largestOddNumber("52"))