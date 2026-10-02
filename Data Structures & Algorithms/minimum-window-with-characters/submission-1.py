class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        length_t = len(t)
        length_s = len(s)
        count_t = {}
        
        for i in range(length_t):
            count_t[t[i]] = count_t.get(t[i], 0) + 1

        required = len(count_t)
        formed = 0
        count_s = {}

        # Tracking our minimum window: (length, left_index, right_index)
        min_len = float("inf")
        ans_left, ans_right = 0, 0

        i = 0 # Left Pointer

        for j in range(length_s):
            char = s[j]
            count_s[char] = count_s.get(char, 0) + 1

            if char in count_t and count_s[char] == count_t[char]:
                formed += 1

            while formed == required:
                if j - i + 1 < min_len:
                    min_len = (j - i + 1)
                    ans_left, ans_right = i, j

                left_char = s[i]    
                count_s[left_char] -= 1
                if left_char in count_t and count_s[left_char] < count_t[left_char]:
                    formed -= 1  # We broke a requirement, so formed drops!
                i += 1

        return "" if min_len == float("inf") else s[ans_left : ans_right + 1]