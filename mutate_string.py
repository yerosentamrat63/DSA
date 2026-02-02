def mutate_string(string, position, character):
    list_s = list(string)
    list_s[position] = character
    return("".join(list_s))
    
if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
