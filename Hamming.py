"""Hamming"""
def main():
    """Hammer down!"""
    text, text2 = list(input()), list(input())
    count = 0
    for i in range(len(text)):
        if text[i] != text2[i]:
            count += 1
    print(count)
main()
