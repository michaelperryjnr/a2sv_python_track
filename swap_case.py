def swap_case(s):
    modified_s = []
    for char in s:
        if char.isupper():
            modified_s.append(char.lower())
        else:
            modified_s.append(char.upper())
    return "".join(char for char in modified_s)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)