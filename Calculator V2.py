"""Calculator V2"""
def calculator():
    """How to cal"""
    num = int(input())
    text = ""
    list_txt = []
    if num > 1:
        for i in range(1, num+1):
            text += str(i)
            list_txt.append(text)
            if i != num:
                text += "+"
            list_txt.append(text)
        print(list_txt)


calculator()
