#User function Template for python3
from collections import Counter

class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        # Your code here
        # i = 0
        # while len(b) > 0:
        #     if b[i] in a:
        #         a.remove(b[i])
        #         b.remove(b[i])
        #     else:
        #         return False
                
        # return True
        acount = Counter(a)
        bcount = Counter(b)
        for idx in range(len(b)):
            if bcount[b[idx]] <= acount[b[idx]]:
                continue
            else:
                return False
        return True
