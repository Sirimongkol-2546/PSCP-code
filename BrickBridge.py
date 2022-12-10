"""BrickBridge"""
def main():
    """BrickBridge"""
    small_a = int(input())
    big_b = int(input())
    goal = int(input()) #สร้างสะพานยาว goal นิ้ว
    iwant = goal//5
    find_big = min(big_b, iwant)
    find_small = goal - find_big*5
    if find_small > small_a:
        print(-1)
    else:
        print(find_small)
main()
