class Solution:
    def sortSentence(self, s: str) -> str:
        splitted = s.split()
        another = [i[::-1] for i in splitted]
        sorted_arr = sorted(another)
        final =[i[::-1][:-1] for i in sorted(sorted_arr)]
        return (" ".join(final))


#Better way:
"""
words = s.split()
words.sort(key=lambda x: int(x[-1]))
result = " ".join(word[:-1] for word in words)
return(result) 

"""