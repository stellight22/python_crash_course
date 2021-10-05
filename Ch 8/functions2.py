def main():
    start = 1
    add(start)
    sub(start)
    print(start)


def add(start):
    start += 10
    return start

def sub(start):
    start -= 5
    return start

if __name__ == "__main__":
    main()