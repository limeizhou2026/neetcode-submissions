class Solution:
    def isPalindrome(self, s: str) -> bool:
        res=''
        for str in s:
            if str.isalnum():
                res += str.lower()

        return res == res[::-1]
