class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []

        for astro in asteroids:
            while res and astro < 0 < res[-1]:
                if -astro > res[-1]:
                    res.pop()
                    continue
                elif -astro == res[-1]:
                    res.pop()
                break
            else:
                res.append(astro)
        return res