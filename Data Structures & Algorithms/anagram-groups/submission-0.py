class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = []
        freq = {}
        for str in strs:
            ssort = "".join(sorted(str))
            if ssort in freq:
                res = freq.get(ssort)
                res.append(str)
                freq[ssort] = res
            else:
                res = []
                res.append(str)
                freq[ssort] = res

        for key in freq:
            answer.append(freq.get(key))

        return answer               