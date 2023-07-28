class Solution:
    def removeAnagrams(self, words):
        i = 0
        while i < len(words) - 1:
            if "".join(sorted(words[i])) == "".join(sorted(words[i + 1])):
                del words[i + 1]
            else:
                i += 1
        return words