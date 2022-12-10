"""[Recommend] iPhone 13 Again"""

def main():
    """input"""
    iphone = input()
    storage = input()
    if iphone == "iPhone 13 mini":
        iphone13mini(storage)
    elif iphone == "iPhone 13":
        iphone13(storage)
    elif iphone == "iPhone 13 Pro":
        iphone13pro(storage)
    elif iphone == "iPhone 13 Pro Max":
        iphone13promax(storage)
    else:
        print("Not Available")

def iphone13mini(storage):
    """checkmini"""
    if storage == "128 GB":
        print("25900")
    elif storage == "256 GB":
        print("29900")
    elif storage == "512 GB":
        print("37900")
    else:
        print("Not Available")

def iphone13(storage):
    """check13"""
    if storage == "128 GB":
        print("29900")
    elif storage == "256 GB":
        print("33900")
    elif storage == "512 GB":
        print("42900")
    else:
        print("Not Available")
def iphone13pro(storage):
    """check13pro"""
    if storage == "128 GB":
        print("38900")
    elif storage == "256 GB":
        print("42900")
    elif storage == "512 GB":
        print("50900")
    elif storage == "1 TB":
        print("58900")
    else:
        print("Not Available")
        
def iphone13promax(storage):
    """ckeckpromax"""
    if storage == "128 GB":
        print("42900")
    elif storage == "256 GB":
        print("46900")
    elif storage == "512 GB":
        print("54900")
    elif storage == "1 TB":
        print("62900")
    else:
        print("Not Available")
main()
