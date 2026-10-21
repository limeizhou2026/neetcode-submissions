class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #using sliding window logic to resolve this question:
        #set a hashmap to count the occurance of each char, the qualified substring is exactly when each char appearent 1 time; 
        #when to increase the window: when there is no duplicate
        #when to narrow the window: when the duplicate appears
        #when to update res: after narrowing the window w/o duplicate
        window = {}
        res = 0
        left = right = 0
        n =len(s)
        #do the while loop while right < n
        while right<n:
            char1 = s[right]
            window[char1] = window.get(char1, 0)+1
            right+=1

            while window[char1] > 1:
                char2 = s[left]
                window[char2] = window.get(char2, 0) -1
                left += 1

            res = max(res, right-left)

        return res