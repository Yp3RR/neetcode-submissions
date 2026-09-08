class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        p = {}
        for word in strs:
            key = "".join(sorted(word))

            if key not in p:
                p[key] = []
            p[key].append(word)
        
        return list(p.values())