class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # out = [i[0] for i in len(strs) if i[
        if not strs:
            return ""

        strs.sort()

        first_str = strs[0]
        last_str = strs[-1]

        common_pref = ""

        for i in range(min(len(first_str), len(last_str))):
            if first_str[i] == last_str[i]:
                common_pref += first_str[i]
            else:
                break
        return common_pref