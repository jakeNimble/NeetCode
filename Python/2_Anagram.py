class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charMap_s = {}
        charMap_t = {}
        for letter in s:
            if letter not in charMap_s:
                charMap_s[letter] = 1
            else:
                charMap_s[letter] += 1
        for letter in t:
            if letter not in charMap_t:
                charMap_t[letter] = 1
            else:
                charMap_t[letter] += 1
        #Comparing Dictionaries
        if len(charMap_s) != len(charMap_t):
            return False
        else:
            for key in charMap_s:
                if key in charMap_t:
                    if charMap_s[key] != charMap_t[key]:
                        return False
                else:
                    return False
            return True