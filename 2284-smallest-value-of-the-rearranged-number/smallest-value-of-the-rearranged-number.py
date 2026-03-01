class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return 0
        pos = False
        if num > 0:
            pos = True
        arr = []
        num = abs(num)
        while num > 0:
            digit = num%10
            num //= 10          
            arr.append(digit)
        if pos:
            arr.sort()
            if arr[0] == 0:
                idx = 0
                for idx in range(len(arr)):
                    if arr[idx] != 0:
                        arr[0], arr[idx] = arr[idx], arr[0]
                        break

        else:
            arr.sort(reverse = True)
        final = "".join([str(i) for i in arr])
        final = int(final)
        if not pos:
            return (0 - int(final))
        return int(final)
        # print(final)