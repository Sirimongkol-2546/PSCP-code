"""ball"""
def main():
    text = input()
    pos = 1
    for i in text:
        if i == "A" and pos == 1:
            pos = 2
        if i == "A" and pos == 2:
            pos = 1
        if i == "B" and pos == 2:
            pos = 3
        if i == "B" and pos == 3:
            pos = 2
        if i == "C" and pos == 3:
            pos = 1
        if i == "C" and pos == 1:
            pos = 3
    print(pos)
main()
