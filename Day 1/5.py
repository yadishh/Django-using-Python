x=int(input("Enter the 1st number: "))
y=int(input("Enter the 2st number: "))
z=int(input("Enter the 3st number: "))
if(x<z)and(y<z):
    print(z,"is maximum")
elif(y<x)and(z<x):
    print(x,"is maximum")
elif(x<y)and(z<y):
    print(y,"is maximum")
else:
    print("All numbers are equal")
