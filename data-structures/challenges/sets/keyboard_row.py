from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = [set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")]
        res = []

        for word in words:
            sword = set(word.lower())

            for row in rows:
                if sword & row == sword:
                    res.append(str(word))

        return res



sol = Solution()
print(sol.findWords(["Hello","Alaska","Dad","Peace"]))
