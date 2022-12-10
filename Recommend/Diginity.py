"""Diginity"""
def main():
    while True:
        num = int(input())
        if num == 0:
            break
        if len(str(num)) == 1: #เป็นเลขโดด
            print(num)
        elif len(str(num)) > 1:
            count = 0
            while True:
                for i in str(num): #11
                    count += int(i) # 2
                if len(str(count)) == 1:
                    break
                num = count
            print(count)
main()
# 47 11