"""is_prime_LARGER"""
def main(num):
    """is_prime_LARGER"""
    if num == 1:
        return "False"
    for i in range(2, int(num*0.05)+1, 3):
        if num % i == 0:
            return "False"
    return "True"
print(main(int(input())))
