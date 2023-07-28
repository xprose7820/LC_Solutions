class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        hashMap = {}
        words1 = s1.split(' ')
        words2 = s2.split(' ')
        print(words1)
        print(words2)
        result = []
        for word in words1:
            if word not in hashMap:
                hashMap[word] = 0
            hashMap[word] += 1

        for word in words2:
            if word not in hashMap:
                hashMap[word] = 0
            hashMap[word] += 1

        for word,count in hashMap.items():
            if count == 1:
                result.append(word)

        return result