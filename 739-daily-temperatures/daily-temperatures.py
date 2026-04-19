class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        # UPVOTE !
        for idx, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                i = stack.pop()
                res[i] = idx - i
            stack.append(idx)

        return res