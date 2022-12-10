"""Pro"""
def main():
    """Promotion"""
    num_x = int(input()) #มา x คน 4
    num_y = int(input()) #จ่าย y คน 3
    num_a = int(input()) #ราคาต่อคน 100
    num_z = int(input()) #มาทาน z คน 2
    price = (num_z//num_x) * num_a * num_y
    price = price + (num_z % num_x) * num_a
    print(price)
main()
