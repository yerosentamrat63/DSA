class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for subarr in range(len(image)):
            image[subarr].reverse()
            for elem in range(len(image[subarr])):
                if image[subarr][elem] == 0:
                    image[subarr][elem] = 1
                else:
                    image[subarr][elem] = 0
        return image
