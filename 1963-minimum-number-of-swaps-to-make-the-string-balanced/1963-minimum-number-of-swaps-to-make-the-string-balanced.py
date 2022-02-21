class Solution:
    def minSwaps(self, s: str) -> int:
        stack = []
        for c in s:
            if stack and c == "]":
                stack.pop()
            elif c == "[":
                stack.append(c)
        return (len(stack)+1)//2