"""FourDirections"""
def main():
    """FourDirections input"""
    text = input()
    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""
    line5 = ""
    for i in text:
        if i == "U":
            line1 += "  *   "
            line2 += " ***  "
            line3 += "* * * "
            line4 += "  *   "
            line5 += "  *   "
        if i == "D":
            line1 += "  *   "
            line2 += "  *   "
            line3 += "* * * "
            line4 += " ***  "
            line5 += "  *   "
        if i == "L":
            line1 += "  *   "
            line2 += " *    "
            line3 += "***** "
            line4 += " *    "
            line5 += "  *   "
        if i == "R":
            line1 += "  *   "
            line2 += "   *  "
            line3 += "***** "
            line4 += "   *  "
            line5 += "  *   "
    print(line1, line2, line3, line4, line5, sep="\n")

main()
