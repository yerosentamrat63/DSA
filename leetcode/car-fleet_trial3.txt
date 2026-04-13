class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [] 
        for p, s in zip(position, speed):
            cars.append([p,s])
        st = []
        
        for p, s in sorted(cars)[::-1]:
            time_taken = (target - p) / s
            if not st or time_taken > st[-1]:
                st.append(time_taken)
        return len(st)