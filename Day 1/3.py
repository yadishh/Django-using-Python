x=int(input("Enter the year: "))
if(x%400==0)or(x%100!=0)and(x%4==0):
    print("leap year")
else:
    print("Not leap year")
