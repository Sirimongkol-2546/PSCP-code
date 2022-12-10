"""BigFrame"""
def main():
    """BigFrame"""
    text1 = input().rstrip()
    text2 = input().rstrip()
    text3 = input().rstrip()
    text4 = input().rstrip()
    text5 = input().rstrip()
    dokjan = max(len(text1),len(text2), len(text3), len(text4), len(text5))
    print("**" + dokjan*"*" + "**")
    print("*" + " " + text1 + (dokjan-len(text1))*" " + " *")
    print("*" + " " + text2 + (dokjan-len(text2))*" " + " *")
    print("*" + " " + text3 + (dokjan-len(text3))*" " + " *")
    print("*" + " " + text4 + (dokjan-len(text4))*" " + " *")
    print("*" + " " + text5 + (dokjan-len(text5))*" " + " *")
    print("**" + dokjan*"*" + "**")
main()
