class Solution:
    def decodeString(self, s: str) -> str:
        self.idx = 0
        def decode():
            res = ""
            currNum = 0
            while self.idx < len(s):
                char = s[self.idx]
                
                if char.isdigit():
                    currNum = currNum * 10 + int(char)

                elif char == '[':
                    self.idx += 1
                    decoded = decode()
                    res += decoded * currNum
                    currNum = 0
    
                elif char == ']':
                    return res
                
                else:
                    res += char
                self.idx += 1

            return res
        return decode()