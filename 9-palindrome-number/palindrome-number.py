class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev_num = 0
        negative = False
        # if x<0:
        #     negative = True
        temp = abs(x)
        while temp:
            last_digit = temp%10
            temp = temp//10
            rev_num = rev_num*10+last_digit
        
        # print(rev_num, x)
        # if negative:
        #     rev_num = -1*rev_num
        # print(rev_num, x)
        if x == rev_num:
            return True
        else:
            return False