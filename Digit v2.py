"""Digit v2"""
def main():
    """V.2 ละเหรอ V.แรกยังไม่ได้ทำเลยมั้ง"""
    text = input()
    if 'thousand' in text:
        print("4")
    elif 'hundred' in text:
        print("3")
    elif ('ty' in text) or ('teen' in text) or ("ten" in text)\
         or ("eleven" in text) or ("twelve"in text):
        print("2")
    else:
        print("1")
main()
