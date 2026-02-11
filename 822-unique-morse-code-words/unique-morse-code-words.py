class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        hashmap = {"a" : ".-",
                "b" : "-...",
                "c" : "-.-.",
                "d" : "-..",
                "e" : ".",
                "f" : "..-.",
                "g" : "--.",
                "h" : "....",
                "i" : "..",
                "j" : ".---",
                "k" : "-.-",
                "l" : ".-..",
                "m" : "--",
                "n" : "-.",
                "o" : "---",
                "p" : ".--.",
                "q" : "--.-",
                "r" : ".-.",
                "s" : "...",
                "t" : "-",
                "u" : "..-",
                "v" : "...-",
                "w" : ".--",
                "x" : "-..-",
                "y" : "-.--",
                "z" : "--.."}

        final_morse = []
        for word in words:
            morse = []
            for char in word:
                morse.append(hashmap[char])
            morse = "".join(morse)
            final_morse.append(morse)
        count = Counter(final_morse)
        return(len(count))