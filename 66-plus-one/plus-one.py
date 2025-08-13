class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        merged = "".join(map(str, digits))
        to_num = int(merged) + 1
        return list(map(int, str(to_num)))