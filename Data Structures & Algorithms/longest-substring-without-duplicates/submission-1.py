class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = 0
        longest = 0
        
        for right in range(len(s)):
            # Shrink the window from the left until the duplicate character is removed
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
                
            # Add the current character and update the maximum window length
            char_set.add(s[right])
            longest = max(longest, right - left + 1)
            
        return longest
            