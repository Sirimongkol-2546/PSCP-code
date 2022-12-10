"""Future Message"""
def main():
    """Future Message"""
    text = input()
    if text.isnumeric(): #ถ้ามี is นำหน้า return เป็น boolean
        print("Number")
    elif text.isupper():
        print("Uppercase")
    elif text.islower():
        print("Lowercase")
    elif text.istitle():
        print("Title")
    elif text.isspace():
        print("Space")
    else:
        print("Other")
main()
