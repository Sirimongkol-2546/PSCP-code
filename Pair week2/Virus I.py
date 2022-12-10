"""Virus I"""
def main():
    """Virus I"""
    virus = input()
    body = 0
    for i in virus:
        if i == "o":
            body = body + 1
    print(body)
main()
