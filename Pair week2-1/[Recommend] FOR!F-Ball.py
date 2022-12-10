"""[Recommend] FOR!F-Ball"""
def main():
    """[Recommend] FOR!F-Ball"""
    text = input()
    glass1 = 1
    glass2 = 0
    glass3 = 0
    for i in text:
        if i == "A":
            glass1, glass2 = glass2, glass1
        if i == "B":
            glass2, glass3 = glass3, glass2
        if i == "C":
            glass1, glass3 = glass3, glass1

    if glass1 == 1:
        print("1")
    elif glass2 == 1:
        print("2")
    else:
        print("3")
main()
