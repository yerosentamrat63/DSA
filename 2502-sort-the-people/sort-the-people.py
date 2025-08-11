class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(heights)

        for i in range(n):
            maxim = i
            
            for j in range(i + 1, n):
                if heights[j] > heights[maxim]:
                    maxim = j

            heights[i], heights[maxim] = heights[maxim], heights[i]
            names[i], names[maxim] = names[maxim], names[i]
        
        return names