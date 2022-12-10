"""iPad Air"""

def main():
    """อยากได้นะ เบื่อจดกระดาษแบ้ว"""
    color = input()
    capacity = input()
    wi_fi = input()
    if color == "Space Gray" or color == "Silver" or color == "Green"\
        or color == "Rose Gold" or color == "Sky Blue":
        check(capacity, wi_fi)
    else:
        print("Not Available")

def check(capacity, wi_fi):
    """check"""
    if capacity == "64" and wi_fi == "Wi-Fi":
        print(19900)
    elif capacity == "64" and wi_fi == "Wi-Fi + Cellular":
        print(24400)
    elif capacity == "256" and wi_fi == "Wi-Fi":
        print(24900)
    elif capacity == "256" and wi_fi == "Wi-Fi + Cellular":
        print(29400)
    else:
        print("Not Available")

main()

