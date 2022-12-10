"""NumDays"""
def main(day_1, month_1, day_2, month_2):

    lst_day = [31, 28, 31, 30, 31, 30 ,31, 31, 30 ,31, 30, 31]
    if month_2 == month_1:
        print(day_2 - day_1)
    elif month_2 > month_1:
        print(day_2 - day_1)

main(int(input()), int(input()), int(input()), int(input()))
