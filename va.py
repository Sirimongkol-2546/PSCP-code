"""ValidVar"""

def main():
    """ValidVar"""
    num = int(input())
    number = "0123456789"
    blank = ""
    for _ in range(num):
        name = input()
        if "if" == name or "else" == name or "elif" == name or "while" == name or "for" == name \
        or "True" == name or "False" == name or "continue" == name or "break" == name \
        or "return" == name or "is" == name or "in" == name or "and" == name or "or" == name \
        or "from" == name or "as" == name or "pass" == name or "not" == name or "def" == name \
        or "None" == name:
            blank += "Invalid\n"
        elif "!" in name or ")" in name or "-" in name or "]" in name or ";" in name or":" in name\
        or "'" in name or '"' in name or "," in name or ">" in name or "." in name or "//" in name \
        or "?" in name or "@" in name or "\\" in name or "#" in name or "$" in name or "%" in name \
        or "^" in name or "+" in name or "=" in name or "&" in name or "*" in name or "~" in name \
        or "(" in name or "[" in name or "<" in name:
            blank += "Invalid\n"
        elif " " in name[1:-1]:
            blank += "Invalid\n"
        elif name[0] in number:
            blank += "Invalid\n"
        else:
            blank += "Valid\n"
    print(blank)
main()
