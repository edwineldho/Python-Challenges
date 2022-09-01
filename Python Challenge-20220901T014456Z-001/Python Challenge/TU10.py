import random
mynumber = random.randint(0,100)
print(mynumber)


import random
Choose_Name = ["James","John","Mark","Rick"]
for i in range(1,5):
    chosen = random.choice(Choose_Name)
    print(chosen)

Question = input("do you want to keep this in your list")

if Question == ("no"):
    Choose_Name.remove(chosen)
print(Choose_Name)
