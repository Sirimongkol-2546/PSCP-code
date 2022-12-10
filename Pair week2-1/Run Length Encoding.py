"""Run Length Encoding"""
def main():
    """Run Length Encoding"""
    text = input()
    check = text[0]
    count = 0
    for i in range(len(text)): #นับว่าtextมีกี่ตัว
        if text[i] == check:
            count += 1
        else:
            print("%d%s" %(count, check), end="")
            check = text[i] #เปลี่ยนตัวตัวต่อไป
            count = 1
    print("%d%s" %(count, check), end="")
main()
