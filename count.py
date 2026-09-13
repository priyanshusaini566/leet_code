class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        count=0
        for item in stones:
            if item in jewels:
                count+=jewels.count(item)

        return count

obj=Solution()
print(obj.numJewelsInStones("aA","aabAAAcc"))