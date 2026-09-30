class Solution:

  def lengthOfLongestSubstring(self, s: str) -> int:
    char_set = set()
    left = 0
    max_len = 0

    for right in range(len(s)):
      # If we hit a duplicate, shrink the window from the left until the duplicate is gone
      while s[right] in char_set:
        char_set.remove(s[left])
        left += 1

      # Add the new character to our set and update max length
      char_set.add(s[right])
      max_len = max(max_len, right - left + 1)

    return max_len