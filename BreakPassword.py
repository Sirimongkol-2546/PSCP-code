"""BreakPassword"""
import hashlib
def main():
    """BreakPassword"""
    password = input().encode("UTF-8")
    bpass = hashlib.sha512(password).hexdigest().upper()
    print(bpass)
main()
