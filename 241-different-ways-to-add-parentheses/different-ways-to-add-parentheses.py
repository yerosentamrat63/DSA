class Solution:
    def diffWaysToCompute(self, expres: str):
        if expres.isdigit():
            return [int(expres)]
        
        result = []
        
        for s in range(len(expres)):
            if expres[s].isdigit():
                continue
            
            left = self.diffWaysToCompute(expres[:s])
            right = self.diffWaysToCompute(expres[s+1:])
            
            for idx in left:
                for jdx in right:
                    if expres[s] == "+":
                        result.append(idx + jdx)
                    elif expres[s] == "*":
                        result.append(idx * jdx)
                    elif expres[s] == "-":
                        result.append(idx - jdx)
        
        return result