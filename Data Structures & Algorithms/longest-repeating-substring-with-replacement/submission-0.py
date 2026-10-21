class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = {}
        l = r = 0
        res = 0
        maxf = 0
        n =len(s)

        while r<n:
            char1 = s[r]
            window[char1] = window.get(char1, 0)+1
            r+=1
            maxf = max(window.values())
            while (r-l -maxf) >k:
                    char2 = s[l]
                    window[char2] = window.get(char2, 0) -1
                    l +=1

            res = max(res, r-l)

        return res
