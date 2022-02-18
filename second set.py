import math
samuel = input("enter a,b or c to learn some math solutions:")
a = math.pow(3,6)
b = math.pow (4,5)
c = math.pow (6,2)

if samuel == 'a':
    print ("The value of 3 to the 6th power is",a,"!")

if samuel == 'b':
    print ("The value of 4 to the 5th power is", b,"!")

if samuel == "c":
    print ("The value of 6 to the 2nd power is",c, "!")


else:
    print("not quite")

