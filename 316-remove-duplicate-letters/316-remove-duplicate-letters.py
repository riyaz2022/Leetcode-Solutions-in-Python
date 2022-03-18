class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        count = Counter(s)
        vis = set()
        stack = []

        for c in s:
            if c not in vis:
                while stack and stack[-1] > c and count[stack[-1]] > 0:
                    vis.remove(stack.pop())
                stack.append(c)
                vis.add(c)
            count[c] -= 1
        return "".join(stack)