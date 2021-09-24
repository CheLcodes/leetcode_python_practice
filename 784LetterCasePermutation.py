from typing import List
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        res = []
        self.backtrack(S, "", 0, res)
        return res

    def backtrack(self, S, path, i, res):
        if i == len(S):
            res.append(path)
            return
        if S[i].isalpha():
            for c in [S[i].upper(), S[i].lower()]:
                self.backtrack(S, path + c, i + 1, res)
        else:
            self.backtrack(S, path + S[i], i + 1, res)
            