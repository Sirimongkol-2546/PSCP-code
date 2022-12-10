"""Run Length Decoding"""
def main():
    """input"""
    text = str(input())
    blank = ""
    for string in text:
        if string.isnumeric():
            blank += string
        else:
            print(string * int(blank), end="")
            blank = ""
main()
