"""Password"""
import hashlib
def main():
    """input"""
    password = input().encode('UTF-8')
    hashpass = hashlib.sha512(password).hexdigest().upper()
    print(hashpass)
main()
