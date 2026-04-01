class Solution:
    def isPalindrome(self, s: str) -> bool:
        str2=s.upper()
        start=0
        end=len(s)-1
        palindrome=True

        while start<end:
            if not str2[start].isalpha() and not str2[start].isdigit():
                start+=1
                continue
            if not str2[end].isalpha() and not str2[end].isdigit():
                end-=1
                continue
            if str2[start]!=str2[end]:
                palindrome=False
                break
            start+=1
            end-=1

        return palindrome
        