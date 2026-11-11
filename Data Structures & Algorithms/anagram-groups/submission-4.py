class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #1.sort每一个单独的str，因为虽然组成不同的words 但是排序后都会是一样的
        #2.然后用一个hashmap记录 不是里面的key 就新建一个 把相对应的word包括它自己放进去
        #3.最后返回list【hashmap的values】

        hashmap_s = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word not in hashmap_s:
                hashmap_s[sorted_word] = []
            hashmap_s[sorted_word].append(word)

        return list(hashmap_s.values())
































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