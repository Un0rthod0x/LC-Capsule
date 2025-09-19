class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        hashe = {}
        for i in range(len(s)):
            if s[i] not in hashe:
                hashe[s[i]] = 0
            else:
                hashe[s[i]] += 1

        hash2 = {}
        for i in range(len(t)):
            if t[i] not in hash2:
                hash2[t[i]] = 0
            else:
                hash2[t[i]] += 1

        if (hash2 == hashe): 
            return True;

        else:
            return False

#not space efficient, hash2 not necessary.         
