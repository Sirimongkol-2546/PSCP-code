"""[Recommend] Temperature"""
def main():
    """[Recommend] Temperature input"""
    temp = float(input())
    temp_from = input()
    temp_to = input()

    if temp_from == "K":
        temp = temp - 273.15
    elif temp_from == "F":
        temp = (temp - 32) * (5/9)
    elif temp_from == "F":
        temp = (temp - 32) * (5/9)
    elif temp_from == "R":
        temp = (temp - 491.67) * (5/9)
    elif temp_from == "C":
        temp = temp

    if temp_to == "K":
        temp = temp + 273.15
    elif temp_to == "F":
        temp = (temp * (9/5)) + 32
    elif temp_to == "R":
        temp = (temp * (9/5)) + 491.67
    elif temp_to == "C":
        temp = temp
    print("%.2f" %temp)
main()
