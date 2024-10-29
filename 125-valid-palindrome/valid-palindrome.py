class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        i = 0
        j = n-1
        list_s = list(s)
        while i<=j:
            if list_s[i].isalnum() and list_s[j].isalnum():
                if list_s[i].lower() != list_s[j].lower():
                    return False
                else:
                    i += 1
                    j -= 1
            else:
                if not list_s[i].isalnum():
                    i += 1
                if not list_s[j].isalnum():
                    j -= 1
        return True