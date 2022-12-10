"""Calculator"""
def calculator():
    """How to cal"""
    num = int(input())
    text = ""
    if num > 1:
        for i in range(1, num+1):
            text += str(i)
            if i != num:
                text += "+"
        text += "="
        print(len(text))
    elif num == 1:
        print(num)
calculator()
