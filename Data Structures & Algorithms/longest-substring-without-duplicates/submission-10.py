class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        string_length = len(s)
        right = 0
        left = 0
        length = 0
        characters = {}

        for right in range(string_length):
            current_char = s[right]

            # If the character is already in our window, jump 'left' past its last seen index
            if current_char in characters and characters[current_char] >= left:
                left = characters[current_char] + 1
                
            # Update the character's latest position
            characters[current_char] = right

            length = max(length, right - left + 1)

        return length


        