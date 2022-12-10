"""Parallelogram"""
def paralle():
    """input"""
    text = input()
    blank = ""
    space = len(text)
    for i in text:
        print(" "*(space-1), end="") #Top
        space -= 1
        blank += i
        print(blank)
    bottom = len(blank) #Bottom
    for j in range(bottom):
        print(blank[j+1:])
paralle()
