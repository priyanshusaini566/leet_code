class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        balance=0
        count=0

        l=list(s)
        for i in range(len(l)):
            if l[i]=='R':
                balance+=1
            else:
                balance-=1

            if balance==0:
                count+=1

        return count


obj=Solution()
print(obj.balancedStringSplit("RLRRLLRLRL"))