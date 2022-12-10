"""Resistor"""
def main():
    """Resistor"""
    band = {"Black":"0", "Brown":"1", "Red":"2", \
        "Orange":"3", "Yellow":"4", "Green":"5",\
        "Blue":"6", "Purple":"7", "Grey":"8", "White":"9"}

    mul = {"Black":1, "Brown":10, "Red":100, "Orange":1000, "Yellow":10000, "Green":100000,\
            "Blue":1000000, "Purple":10000000, "Gold":0.1, "Silver":0.01}

    tol = {"Brown":1, "Red":2, "Green":0.5, "Blue":0.25, "Purple":0.1,\
            "Grey":0.05, "Gold":5, "Silver":10}

    color1 = input()
    color2 = input()
    color3 = input()
    color4 = input()

    condition1 = color1 not in band or color2 not in band
    condition2 = color3 not in mul
    condition3 = color4 not in tol

    if condition1 or condition2 or condition3 == True:
        print("Error")
    else:
        #calculate
        final_num = int(band[color1] + band[color2]) * mul[color3]
        final_min = final_num - (final_num * (tol[color4]/100))
        final_max = final_num + (final_num * (tol[color4]/100))
        print('%.4f' %final_min)
        print('%.4f' %final_max)
main()
