class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        set1 = set(list1)
        set2 = set(list2)
        inter = set1 & set2
        hashmap = {}
        for word in inter:
            i = list1.index(word)
            j = list2.index(word)
            sum_idx = i + j
            hashmap[i, j] = sum_idx
        leastsum = min(hashmap.values()) 
        indexes = [k for k, v in hashmap.items() if v == leastsum]
        return([list1[i[0]] for i in indexes])