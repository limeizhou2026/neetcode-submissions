class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {}
        l = r = 0
        n = len(s)
        res = 0

        while r<n:
                char1 = s[r]
                hashmap[char1] = hashmap.get(char1, 0) +1
                r+=1

                while hashmap[char1]>1:
                    char2 = s[l]
                    hashmap[char2] = hashmap.get(char2, 0)-1
                    l +=1

                res = max(res, r-l)

        return res










































        
        #using sliding window logic to resolve this question:
        #set a hashmap to count the occurance of each char, the qualified substring is exactly when each char appearent 1 time; 
        #when to increase the window: when there is no duplicate
        #when to narrow the window: when the duplicate appears
        #when to update res: after narrowing the window w/o duplicate
        window = {}
        res = 0
        #window是左闭右开
        left = right = 0
        n =len(s)
        #do the while loop while right < n
        while right<n:
            #let 右边开始scan string
            char1 = s[right]
            #count在这个区间之内的char的occurance
            window[char1] = window.get(char1, 0)+1
            #right pointer+1
            right+=1


            #当duplicate出现即是有不符合题规的char加入
            while window[char1] > 1:
                #开始从左边缩紧window
                char2 = s[left]
                window[char2] = window.get(char2, 0) -1
                left += 1

            res = max(res, right-left)

        return res