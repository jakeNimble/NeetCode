class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        fin = defaultdict(list) # when I am checking for a key the defaultdict will auto add it if it's not there

        for s in strs: #looping through the list of words
            count = [0] * 26 #this creates a list of 0's accounting for a ... z

            for c in s: #c standing for character and s standing for string
                count[ord(c) - ord("a")] += 1 #this is essentially creating a key for us... the key will be the count of characters

            fin[tuple(count)].append(s) #using our new key we are appending the word to that list... this is new to me
            #I believe this means for a dictionary with list we can actually append straight to the list (value)

        return fin.values()
                