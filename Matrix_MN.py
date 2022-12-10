"""Matrix_MN"""
def main():
    """โอ้ยเหนาะ อีหยังว่ะสู"""
    num_m = int(input())
    num_n = int(input())
    matrix = []
    for i in range(num_m):
        list_a = []
        for j in range(num_n):
            list_a.append(input())
        matrix.append(list_a)
    for i in range(num_m):
        for j in range(num_n):
            print(matrix[i][j], end=" ")
        print()
main()
