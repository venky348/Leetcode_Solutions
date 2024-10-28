class Solution:
    def reverse(self, x: int) -> int:
        rev_num = 0
        negative = False
        if x<0:
            negative = True
            x = abs(x)
        while x:
            last_digit = x%10
            x = x//10
            rev_num = rev_num*10 + last_digit
        if negative:
            rev_num = -1*rev_num
        if rev_num >= -1*(2**31) and rev_num <= 2**31-1:
            return rev_num
        else:
            return 0