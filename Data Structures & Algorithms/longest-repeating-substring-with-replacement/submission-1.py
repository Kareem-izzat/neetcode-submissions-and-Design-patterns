class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq={}

        start , end = 0 ,0
        longest=0
        while start < len(s) or end < len(s)-1:
            if s[end] not in freq:
                freq[s[end]] =1
            else:
                freq[s[end]] += 1
            maxChar = max(freq.values())
            if end - start +1  - maxChar <= k:
                if end - start +1 > longest:
                    longest = end - start +1
                if end<len(s)-1:
                    end+=1
                else:
                    start+=1
            else:
                freq[s[start]] -=1
                start+=1
                if end<len(s)-1:
                    end+=1
        return longest
        