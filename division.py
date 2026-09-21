class Solution(object):
    def divide(self, dividend, divisor):
        negative = (dividend < 0) != (divisor < 0)

        dividend = abs(dividend)
        divisor = abs(divisor)

        quotient = 0

        while dividend >= divisor:
            temp = divisor
            multiple = 1

            while dividend >= temp + temp:
                temp = temp + temp
                multiple = multiple + multiple

            dividend = dividend - temp
            quotient = quotient + multiple

        if negative:
            quotient = -quotient

        # 32-bit integer limits
        if quotient > 2147483647:
            quotient = 2147483647

        if quotient < -2147483648:
            quotient = -2147483648

        return quotient
