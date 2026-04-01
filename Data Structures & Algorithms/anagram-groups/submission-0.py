class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for letter in s:
                count[ord(letter) - ord("a")] +=1
            map[tuple(count)].append(s)
        return list(map.values())