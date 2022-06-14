'''
Given a string s, find the length of the longest substring without repeating characters.

'''

'''class Solution:

    Correct solution, but TimeLimitExceeded

    complexity = O(n^2)

    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 1: return 1

        prev = cur = [1] + [0] * (n - 1)

        m = 0
        for i in range(1, n):
            for j in range(1, i + 1):
                if s[i - j] != s[i]:
                    cur[j] += 1 + prev[j - 1]
                else:
                    cur[j] = cur[j - 1]
                    break

            if max(cur) > m: m = max(cur)

            prev = cur
            cur = [1] + [0] * (n - 1)
            
        return m'''

class Solution:
    # O(n)
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        maxlength = 0
        used = {}
        for i in range(len(s)):
            if s[i] in used and start <= used[s[i]]:
                start = used[s[i]] + 1
            else:
                maxlength = max(maxlength, i - start + 1)
            used[s[i]] = i
        return maxlength

a = Solution()

#print(a.lengthOfLongestSubstring('abcabcbb'))
#print(a.lengthOfLongestSubstring('bbbb'))
#print(a.lengthOfLongestSubstring('pwwkew'))
#print(a.lengthOfLongestSubstring('a'))
#print(a.lengthOfLongestSubstring('abcdefghtoqwe'))
print(a.lengthOfLongestSubstring('abccdag'))