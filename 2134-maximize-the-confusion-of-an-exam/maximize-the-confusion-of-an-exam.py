class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        #FOR THE LONGEST TRUE
        n = len(answerKey)
        l= 0
        change_F = 0
        max_true= 0
        for r in range(n):
            if answerKey[r] == "F":
                change_F += 1
            while change_F > k:
                if answerKey[l] == "F":
                    change_F -= 1
                l += 1
            w = r - l + 1
            max_true = max(w, max_true)
        #FOR THE LONGEST FALSE
        left = 0
        change_T = 0
        max_false = 0
        for right in range(n):
            if answerKey[right] == "T":
                change_T += 1
            while change_T > k:
                if answerKey[left] == "T":
                    change_T -= 1
                left += 1
            w2 = right - left + 1
            max_false = max(w2, max_false)
        return max(max_false, max_true)