class Solution:
    def compress(self, chars: List[str]) -> int:
        copy = chars[:]
        chars.clear()

        holder = 0
        seeker = 0
        while seeker < len(copy):
            count = 0
            current = copy[seeker]
            while seeker < len(copy) and copy[seeker] == current:
                seeker += 1
                count += 1
            chars.append(current)

            if count > 1:
                chars.extend(list(str(count)))
        return len(chars)