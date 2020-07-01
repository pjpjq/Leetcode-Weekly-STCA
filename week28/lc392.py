class Solution:
    def isSubsequenceNormal(self, s: str, t: str) -> bool:
        if not s: return True
        cur_s_idx = 0
        n = len(s)
        for c in t:
            if c == s[cur_s_idx]:
                cur_s_idx += 1
                if cur_s_idx == n:
                    return True 
        return False

    def isSubsequence(self, s: str, t: str) -> bool: # follow up
        pos = defaultdict(list)
        for i, c in enumerate(t):
            pos[c].append(i)
        prev_pos = 0
        for c in s:
            pos_idx = bisect_left(pos[c], prev_pos)
            if pos_idx == len(pos[c]):
                return False 
            prev_pos = pos[c][pos_idx] + 1
        return True