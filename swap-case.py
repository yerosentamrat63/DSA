def swap_case(s):
    temp =""
    for i in range(len(s)):
        if s[i] == s[i].upper():
            temp += s[i].lower()
        else:
            temp += s[i].upper()
    return temp

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
