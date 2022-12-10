"""Pad Thai"""
def main():
    """ไม่ไหวไม่ไหวไม่ไหวไม่กดาไดสหวเ่วฟหนเาฟว"""

    check_material = ["Pad Thai Sauce", "Tofu", "Pickle Turnip", "Shrimp",\
        "Bean Sprouts", "Noodle", "Chives", "Lime", "Egg", "Oil", "Peanuts"]
    check_favor = ["Sweet", "Sour", "Salty"]

    material_lst = [] #เอาไว้เปรียบเทียบ
    favor_lst = [] #เอาไว้เปรียบเทียบ
    not_in_padthai = [] #นอกเหนือจากวัตถุดิบเอามาใส่ตรงนี้

    while True:
        material = input()
        if material == "Cook":
            break

        if material not in material_lst:
            material_lst.append(material)
        #เพิ่มวัตถุดิบลง list
        #["Tofu", ..... , "Noodle"]

        if material not in check_material:
            not_in_padthai.append(material)
        #อันไหนไม่มีเอาไปเพิ่มลงอีก list

    while True:
        favor = input()
        if favor == "End":
            break
        if favor not in favor_lst:
            favor_lst.append(favor)

    if not_in_padthai != []:
        print("This is not Pad Thai!!!")
    elif material_lst != check_material:
        print("This is bad!")
    elif material_lst == check_material and check_favor != favor_lst:
        print("Not Bad...")
    elif material_lst == check_material and check_favor == favor_lst:
        print("Delicious!")

main()
