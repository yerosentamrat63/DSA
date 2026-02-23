class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        hashmap = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
        new_num1 = 0
        new_num2 = 0
        for i in num1:
            new_num1 = new_num1 * 10 + hashmap[i]
        for i in num2:
            new_num2 = new_num2 * 10 + hashmap[i]
        sum = new_num1 + new_num2
        str_sum = ""
        while sum > 0:
            str_sum = str_sum + str(sum % 10)
            sum //= 10
        if str_sum == "":
            str_sum = "0"
        return str_sum[::-1]