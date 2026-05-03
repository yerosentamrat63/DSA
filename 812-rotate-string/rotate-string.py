class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        manual_loop = s + s
        return True if goal in manual_loop else False