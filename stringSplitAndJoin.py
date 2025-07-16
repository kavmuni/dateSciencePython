

def split_and_join(line):
    # write your code here
    split1 = line.split(" ")
    join1  = "-".join(split1)
    return join1

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)