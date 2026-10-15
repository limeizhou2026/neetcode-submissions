class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap_strs = {}

        for word in strs:
            #join the sorted word without any spaces; sorted(word) returns a list
            key = ''.join(sorted(word))
            if key in hashmap_strs:
                hashmap_strs[key].append(word)
            else:
                #word here has to be a list since the result is a double list whose sublist contains all grouped anagram
                hashmap_strs[key] = [word]

        return list(hashmap_strs.values())