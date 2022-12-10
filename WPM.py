"""WPM"""
def main():
    """WWE"""
    text = input()
    wpm = int(input())
    if  (text == "Kids" and wpm < 11) or (text == "Adults" and wpm < 26):
        print("Very Slow")
    elif  text == "Kids" and wpm >= 11 and wpm <= 20:
        print("Slow")
    elif text == "Kids" and wpm >= 21 and wpm <= 30:
        print("Average")
    elif text == "Kids" and wpm >= 31 and wpm <= 40:
        print("Fast")
    elif text == "Kids" and wpm > 40:
        print("Very Fast")

    elif text == "Adults" and wpm >= 26 and wpm <= 35:
        print("Slow/Beginner")
    elif text == "Adults" and wpm >= 36 and wpm <= 45:
        print("Intermediate/Average")
    elif text == "Adults" and wpm >= 46 and wpm <= 65:
        print("Fast/Advanced")
    elif text == "Adults" and wpm >= 66 and wpm <= 80:
        print("Very Fast")
    else:
        print("Insane")
main()
