

def split_and_join(line):
    # write your code here
    splitted_string = line.split(" ")
    
    return "-".join(s for s in splitted_string)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)