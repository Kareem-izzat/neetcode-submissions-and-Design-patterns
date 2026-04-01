class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq=set()
        if len(s) == 0:
            return 0
        start,end=0,0
        max=1
        dub=-1
        existDub=False
        while end<len(s):
            if existDub:
                if dub==s[start]:
                    freq.remove(s[start])
                    start+=1
                    dub=-1
                    existDub=False
                else:
                    freq.remove(s[start])
                    start+=1
            if s[end] not in freq:
                freq.add(s[end])
                end+=1
                if len(freq)> max:
                    max=len(freq)
            else:
                
                dub=s[end]
                existDub=True
        return max
                