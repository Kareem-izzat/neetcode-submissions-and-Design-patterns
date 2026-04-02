class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1freq = {}
        comp = {}

        
        for c in s1:
            if c not in s1freq:
                s1freq[c] = 1
            else:
                s1freq[c] += 1

        p1 = 0
        same = 0

        for p2 in range(len(s2)):
            
            if s2[p2] in s1freq:
                if s2[p2] not in comp:
                    comp[s2[p2]] = 1
                else:
                    comp[s2[p2]] += 1

                if comp[s2[p2]] == s1freq[s2[p2]]:
                    same += 1
                elif comp[s2[p2]] == s1freq[s2[p2]] + 1:
                    same -= 1

            if p2 - p1 + 1 > len(s1):
                left = s2[p1]
                if left in s1freq:
                    if comp[left] == s1freq[left]:
                        same -= 1
                    elif comp[left] == s1freq[left] + 1:
                        same += 1

                    comp[left] -= 1
                p1 += 1

            if same == len(s1freq):
                return True

        return False