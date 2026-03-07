class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s).most_common()
        new = "".join(k * v for k, v in count)
        return new