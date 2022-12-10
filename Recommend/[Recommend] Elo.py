"""[Recommend] Elo"""
def main():
    """[Recommend] Elo"""
    ra_ = int(input())
    rb_ = int(input())
    text = input()
    ea_ = 1 / (1 + 10**((rb_ - ra_)/400))
    eb_ = 1 / (1 + 10**((ra_ - rb_)/400))
    if text == "A":
        print("%.2f" %ea_)
    elif text == "B":
        print("%.2f" %eb_)
main()

