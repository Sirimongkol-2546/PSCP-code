"""key"""
def main():
    """key"""
    numid = input()
    ans1 = 0
    for i in numid:
        ans1 += int(i) #int + str ไม่ได้
    ans2 = int(numid[-3:]) * 10
    ans3 = ans1 + ans2
    if ans2 >= 10000:
        ans3 = int(str(ans3)[1:])
    elif ans3 < 1000:
        ans3 += 1000
    print("%04d" %ans3)
main()

#hello
#01234
#-5 -4 -3 -2 -1
#9999