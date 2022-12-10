"""[Pre]Hamburger"""
def main():
    """input Hamburger"""
    l_num = int(input())
    r_num = int(input())
    bread1 = '|'* l_num
    bread2 = '|' * r_num
    meat1 = '*' * l_num *2
    meat2 = '*' * r_num *2
    print(bread1 + meat1 + meat2 + bread2)
main()
