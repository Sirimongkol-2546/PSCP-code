"""RunGame"""
def main():
    """Cookie run kingdom is fun"""
    jelly = input().split()
    this_x = 0
    all_jelly = 0
    for i in jelly:
        this_x += abs(all_jelly - int(i))
        all_jelly = int(i)
    print(this_x)
main()
