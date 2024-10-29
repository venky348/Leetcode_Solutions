class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        alpha_s = ""
        for i in range(n):
            if s[i].isalnum():
                alpha_s += s[i].lower()
        
        alpha_s = list(alpha_s)
        # if len(alpha_s) == 1:
        #     return False
        for i in range(len(alpha_s)//2):
            if alpha_s[i] != alpha_s[len(alpha_s)-i-1]:
                return False
        return True
        
        