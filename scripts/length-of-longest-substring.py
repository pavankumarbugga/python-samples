def lengthOfLongestSubstring(s):
        maxLen = 1
        finals = ''
        if s == '':
            return 0                      # Dealing with one edge case
        for i in range(len(s)):
            substring = s[i]              # Initialising the substring
            for j in range(i+1, len(s)):  # Starting to append characters to substring from i+1
                substring = s[i:j+1]
                #print(substring)
        print("----")
        print(finals)
        print(maxLen) 

# s = "arocrubiksapool"
lengthOfLongestSubstring(s)