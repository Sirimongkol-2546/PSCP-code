"""Kabata"""
def main():
    """banana bana nana"""
    num = int(input())
    for _ in range(1, num+1):
        text = input()
        text = text.replace("baka", "-")
        text = text.replace("bakka", "")
        text = text.replace("ba", "")
        text = text.replace("ka", "")
        text = text. replace("ta", "")
        if text == "":
            print("yes")
        else:
            print("no")
main()
