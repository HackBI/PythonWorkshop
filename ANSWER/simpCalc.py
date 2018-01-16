def add(x,y):
    return x + y

def sub(x,y):
    return x-y

def mult(x,y):
    return x * y

def div(x,y):
    return x / y

print("Pick an Operation: ")
print("1) Addition \n2) Subtraction \n3) Multiplication \n4) Division")
choice = int(input("Enter choice 1/2/3/4: "))

n1 = float(input("Enter the first number: "))
n2 = float(input("Enter the second number: "))

if choice == 1:
    print(str(n1) + " + " + str(n2) + "= " + str(add(n1,n2)))
elif choice == 2:
    print(str(n1) + " - " + str(n2) + "= " + str(sub(n1,n2)))
elif choice == 3:
    print(str(n1) + " * " + str(n2) + "= " + str(mult(n1,n2)))
elif choice == 4:
    print(str(n1) + " / " + str(n2) + " = " + str(div(n1,n2)))
else:
    print("Thats not a choice you dummy")
    
