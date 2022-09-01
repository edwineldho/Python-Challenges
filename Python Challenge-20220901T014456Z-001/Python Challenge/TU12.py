MYLIST = ["1","2","3","4","5","6"]
print(MYLIST[3])

MYLIST.append("7")
print(MYLIST)

MYLIST.remove("7")
print(MYLIST)

NewNumber = input("add a number")
MYLIST.append(NewNumber)
print(MYLIST)

MYLIST.sort()

Superherolist = []
Superheroes = input("write a superhero 1")
Superherolist.append(Superheroes)
Superheroes1 = input("write a superhero 2")
Superherolist.append(Superheroes1)
Superheroes2 = input("write a superhero 3")
Superherolist.append(Superheroes2)

anymore = input(" do you need to add anymore")

if anymore == ("yes"):
    print("too bad")

print(Superherolist)
