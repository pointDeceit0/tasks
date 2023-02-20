import collections

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        Also O(n), but MORE efficient
        '''
        return collections.Counter(s) == collections.Counter(t)
        '''
        My solution
        time  --- O(n)
        space --- O(n)

        if len(s) != len(t): return False
        letters = {}
        
        for i in range(len(s)):
            if s[i] not in letters:
                letters[s[i]] = 1
            else:
                letters[s[i]] += 1
            
            if t[i] not in letters:
                letters[t[i]] = -1
            else:
                letters[t[i]] -= 1

        return all(let == 0 for let in letters.values())'''
            

def test():
    s = Solution()

    assert s.isAnagram("anagram", "nagaram") == True
    assert s.isAnagram("rat", "car") == False
    #assert s.isAnagram() ==


def main():
    test()
    return 0

if __name__ == "__main__":
    main()