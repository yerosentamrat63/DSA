class Solution:
    def interpret(self, command: str) -> str:
        new = command
        for _ in command:
            if "(al)" in command:
                new = new.replace("(al)", "al")
            if "()" in command:
                new = new.replace("()", "o")
        return (new)