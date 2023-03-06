class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [s for s in s.lower() if s.isalnum()]
        return s == s[::-1]
    

a = "A man, a plan, a canal: Panama"
s = Solution()
print(s.isPalindrome(a))