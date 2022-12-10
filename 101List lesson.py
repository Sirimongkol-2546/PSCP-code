"""List lesson101 by Prepro"""
#การเข้าถึง list
a = list()
a =['a', 'b', 'c']
print(a[0])

#การเข้าถึง Nested List
list_list = ["A", 25.64], ["B", 45.78], ["C", 90]
print(list_list[1])
print(list_list[1][0])
print(list_list[1][1])

#List Slicing
#long_list = ["I", "H", "E", "R", "E", "T", "O", "O"]
#print(long_list[5:0:-1])
#print(long_list[1:5]) #HERE
#print(long_list[0:8:2]) #IEEO

#แก้ค่าสมาชิกใน list
#long_list = ["I", "H", "E", "R", "E", "T", "O", "O"]
#long_list[0:4] = ["E", "D", "O", "K"]
#print(long_list)

#เพิ่มสมาชิกลงlist 
#เพิ่มที่ละตัว .append()
#friend = []
#friend.append("Hi")
#print(friend)

#เพิ่มหลายๆตัว .extend(), +=
#friends = []
#friends.extend(["a", "b", "c"])
#print(friends)

#friends = ["a", "b", "c"]
#friends += ["d", "e", "f"]
#print(friends)

#เพิ่มแบบระบุตำแหน่ง .insert()
#notfriend = ["a", "b", "c"]
#notfriend.insert(1, "h") #(ลำดับที่จะแทรก, ตัวที่แทรก)
#print(notfriend)

#ลบสามาชิกในlist del .remove() .pop() .clear()