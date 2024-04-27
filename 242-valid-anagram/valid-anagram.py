class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False
        else:
            s_freq = {}
            for i in s:
                if(i in s_freq):
                    s_freq[i] += 1
                else:
                    s_freq[i] = 1
            for i in t:
                if(i in s_freq):
                    s_freq[i] -= 1
            for i in s_freq:
                if(s_freq[i]!=0):
                    return False
            return True