"""Temp"""
def main():
    """temp"""
    temp = float(input())
    from_temp = input()
    to_temp = input()

    if from_temp == "F":
        temp = (temp - 32) * (5/9)
    elif from_temp == "K":
        temp = temp - 273.15
    elif from_temp == "R":
        temp = temp*(5/9) - 273.15
    elif from_temp == "C":
        temp = temp

    if to_temp == "F":
        temp = (temp*(9/5)) + 32
    elif to_temp == "K":
        temp = temp + 273.15
    elif to_temp == "R":
        temp = (temp+273.15) * (9/5)
    elif to_temp == "C":
        temp = temp
    print('%.2f' %temp)
main()
