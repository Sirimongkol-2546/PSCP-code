"""TheFunctionWithin"""
def f_x(value_x):
    """f(x)"""
    return 2*value_x

def g_x(value_x):
    """g(x)"""
    return 3 * (value_x**4) - (value_x**3) + 2*(value_x**2) + 10

def h_x(value_x, value_y, value_z):
    """h(x,y,z)"""
    return (value_z+value_x)**2 - (value_x*value_y) + value_y**2

def i_x(value_a, value_b, value_c, value_d):
    """i(a, b, c, d)"""
    top = value_a**2 + value_b**2 - value_c**2
    bottom = (value_d**2) - (2*value_a*value_d) + (2*value_a)
    return top/bottom

def main():
    """main"""
    value_a = float(input())
    value_b = float(input())
    value_c = float(input())
    value_d = float(input())

    print(f_x(f_x(value_a)))
    print(g_x(f_x(value_a-value_b)))

    f_ab = h_x(f_x(value_a+value_b), f_x(value_a + value_c), g_x(f_x(value_d**2)))
    print(f_ab)

    i_1 = h_x(f_x(value_a+value_b), f_x(value_a-value_c), g_x(f_x(value_d**2)))
    i_2 = g_x(f_x(value_a-value_b))
    i_3 = f_x(f_x(f_x(f_x(f_x(value_c)))))
    print(i_x(i_1, i_2, i_3, value_d**8))
main()
