"""WordSequence I"""
def main():
    """input"""
    word = input()
    for i in range(len(word)):
        print(word[0:i+1])
main()
