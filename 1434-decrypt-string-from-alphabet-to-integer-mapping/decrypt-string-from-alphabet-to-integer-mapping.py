class Solution:
    def freqAlphabets(self, s: str) -> str:
        hashmap ={        
                "1": "a",
                "2": "b",
                "3": "c",
                "4": "d",
                "5": "e",
                "6": "f",
                "7": "g",
                "8": "h",
                "9": "i",
                "10#": "j",
                "11#": "k",
                "12#": "l",
                "13#": "m",
                "14#": "n",
                "15#": "o",
                "16#": "p",
                "17#": "q",
                "18#": "r",
                "19#": "s",
                "20#": "t",
                "21#": "u",
                "22#": "v",
                "23#": "w",
                "24#": "x",
                "25#": "y",
                "26#": "z"
                }
        ans = []
        leng = len(s) - 1
        while leng >= 0:
            if s[leng] == "#":
                ans.append(hashmap[s[leng-2:leng+1]])
                leng -= 3
            else:
                ans.append(hashmap[s[leng]])
                leng -= 1
        
        ans.reverse()
        return ("".join(ans))