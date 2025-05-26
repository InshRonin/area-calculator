import math
pi = math.pi

print("================== \nArea Calculator 📐 \n==================")
print()
print(" 1) Triangle \n 2) Rectangle \n 3) Square \n 4) Circle \n 5) Quit")
print()

selector = int(input("Which shape: "))

if selector == 1:
    height = int(input("height: "))
    base = int(input("base: "))
    area1 = (height * base) / 2
    print(f"The area is {area1}")
elif selector == 2:
    length = int(input("length: "))
    width = int(input("width: "))
    area2 = length * width
    print(f"The area is {area2}")
elif selector == 3:
    side = int(input("side length: "))
    area3 = side ** 2
    print(f"The area is {area3}")
elif selector == 4:
    radius = int(input("radius: "))
    area4 = pi * (radius ** 2)
    print(f"The area is {area4}")
else:
    print("Thanks for using the Area Calculator 📐 ")
