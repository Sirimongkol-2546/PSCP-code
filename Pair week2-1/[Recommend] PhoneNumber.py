"""[Recommend] PhoneNumber"""

def main():
    """input"""
    number = input()
    sel = input()
    if sel == "Domestic":
        if len(number) == 10:
            print("%s %s %s" %(number[0:2], number[2:6], number[6:10]))
        else:
            print("%s %s %s" %(number[0], number[1:5], number[5:9]))
    elif sel == "International":
        if len(number) == 10:
            print("%s %s %s" %("+66"+number[1], number[2:6], number[6:10]))
        else:
            print("%s %s %s" %("+66", number[1:5], number[5:9]))
main()
