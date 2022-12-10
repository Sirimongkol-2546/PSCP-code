import random

select = input("เลือกมาว่าจะลงอะไร (หิน, กระดาษ, กรรไกร): ")
action = ["หิน", "กระดาษ", "กรรไกร"]
it_is_me = random.choice(action)
print(f"\nคุณเลือก {select}, แต่ผมได้ {it_is_me}.\n")