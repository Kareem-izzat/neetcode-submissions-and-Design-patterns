class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        freq1 = {}
        freq2 = {}
        for i in range(len(s)):
            if s[i] not in freq1:
                freq1[s[i]]=1
            else:
                freq1[s[i]]+=1
            if t[i] not in freq2:
                freq2[t[i]] = 1
            else:
                freq2[t[i]] += 1
        for key in freq2:
            if key not in freq1:
                return False
            if freq1[key] != freq2[key]:
                return False
        return True
                