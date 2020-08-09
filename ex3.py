"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

class Solution:
    def lengthOfLongestSubstring(self, s):
        str_list = []
        max_length = 0
    
        for x in s:
            if x in str_list:
                str_list = str_list[str_list.index(x)+1:]
            
            str_list.append(x)    
            max_length = max(max_length, len(str_list))
        
        return max_length
    
ex3=Solution()
print(ex3.lengthOfLongestSubstring("abcaabcbb"))
