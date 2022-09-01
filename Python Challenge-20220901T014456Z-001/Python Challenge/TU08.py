while True:
    subject = input ('is computer science your fav subject(Yes or No)')
    if subject == "yes" :
        break

number = 0 #You have to declare this first
while number < 15 or number > 20 :
    print("Please enter a number between 15 and 20")
    number = float(input("enter a number:"))
    if 15<number>20 :
        break
