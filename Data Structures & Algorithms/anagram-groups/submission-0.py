class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap_strs = {}

        for word in strs:
            key = ''.join(sorted(word))
            if key in hashmap_strs:
                hashmap_strs[key].append(word)
            else:
                hashmap_strs[key] = [word]

        return list(hashmap_strs.values())