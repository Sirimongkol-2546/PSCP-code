"""ISBN"""
def main():
    """ISBN"""
    isbn = input()
    ahe = 10
    for_cal = 0
    ans = 0
    isbn = isbn.replace("-", "")
    isbn_2 = isbn[0:9]

    for i in isbn_2:
        for_cal = ahe * int(i)

        ans += for_cal
        ahe -= 1 #10 9 8...3 2
    ans = (-ans)%11

    if ans == 10:
        ans = "X"

    if isbn[-1] != str(ans):
        print("No", ans)
    else:
        print("Yes")
main()
