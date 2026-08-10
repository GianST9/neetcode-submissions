class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_len = len(s)
        t_len = len(t)

        if s_len != t_len:
            return False 

        s_map = {}
        t_map = {}
        for i in range(s_len):
            if s[i] in s_map:
                s_map[s[i]] += 1
            else:
                s_map[s[i]] = 1

            if t[i] in t_map:
                t_map[t[i]] += 1
            else:
                t_map[t[i]] = 1
        return (s_map == t_map)