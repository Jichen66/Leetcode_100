class Solution:
    def remove_duplicate_stars(self, p):
        if p == '':
            return p
        p1 = [p[0],]
        for x in p[1:]:
            if p1[-1] != '*' or p1[-1] == '*' and x != '*':
                p1.append(x)
        return ''.join(p1)

    def helper(self, s, p):
        dp = self.dp
        if (s, p) in dp:
            return dp[(s, p)]

        if p == s or p == '*':
            dp[(s, p)] = True
        elif p == '' or s == '':
            dp[(s, p)] = False
        elif p[0] == s[0] or p[0] == '?':
            dp[(s, p)] = self.helper(s[1:], p[1:])
        elif p[0] == '*':
            dp[(s, p)] = self.helper(s, p[1:]) or self.helper(s[1:], p)
        else:
            dp[(s, p)] = False

        return dp[(s, p)]

    def isMatch(self, s, p):
        p = self.remove_duplicate_stars(p)
        # memorization hashmap to be used during the recursion
        self.dp = {}
        return self.helper(s, p)
a = Solution()
s1 = "acdcb"
p1 = "a*c?b"
print(a.isMatch(s1,p1))