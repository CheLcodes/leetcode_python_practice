class Solution:
    def addBoldTag(self, s: str, words) -> str:
        status = [False] * len(s) # whether it should be bolded
        final = ""
        for word in words:
            start = s.find(word)  # starting idx for word in s
            last = len(word)
            while start != -1:
                for i in range(start, start + last):
                    status[i] = True
                start = s.find(word,start+1) # (there can be several same words)search word in s[start+1:]
        i = 0
        while i < len(s):
            if status[i]:
                final += "<b>"
                while i < len(s) and status[i]:
                    final += s[i]
                    i += 1
                final += "</b>"
            else:
                final += s[i]
                i += 1
        return final

sol = Solution()
res = sol.addBoldTag("aaabbcc", ["aaa","aab","bc"])
print(res)