import random

def test_random():
    random_number = random.randint(1, 10)
    geatt = int(input("what is your number"))
    if geatt == random_number:
        print("ทายถูกแล้ว")
    elif geatt < random_number:
        print("น้อยไปอ้วน")
    elif geatt > random_number:
        print("มากไปไออ้วน พอดีๆหน่อยดิ")
    else:
        print("ผิด! เลขที่สุ่มคือ", random_number)

test_random()