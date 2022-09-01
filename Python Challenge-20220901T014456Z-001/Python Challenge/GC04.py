n = input("Enter Height of Pyramid: ")
height = int(n)

for i in range(height):
	print (" "*(height-1*i)+("x")+("x"*(1*i)))

