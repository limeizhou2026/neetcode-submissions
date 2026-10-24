class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #using sort and hashmap:
        #sort the string in strs, since if the str is a anagram. It will be the same once sort the letters
        #then using hashmap to record the same anagrams that the value of each key will append the anagrams into a list

        hashmapA = {}
        for str in strs:
            #字符串不能用.sort() 必须用sorted返回一个list 否则返回None。
            #EX：sorted("eat")  # 返回 ["a", "e", "t"]
            #如果你还希望继续返回一个 字符串 那么就用 ‘’.join 表示字符中间不能有任何间隔符
            key = ''.join(sorted(str))
            if key in hashmapA:
                hashmapA[key].append(str)
            else:
                hashmapA[key] = [str]

        #这步至关重要 因为 hashmap.values（）不会自动生成一个list 必须手动转换
        return list(hashmapA.values())























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