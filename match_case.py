# IN match case if any one condition becomes true it will excute and get stasfied
# default case(will only be matched if the above cases were not matched)
x = int(input("Enter the value of x: "))
match x:
    case 0:
        print("x is zero")
    case 4:
        print("case is 4")

    case _ if x!=90:
        print(x, "is not 90")
    case _ if x!=80:
        print(x, "is not 80")
    case _:
        print(x)

x = int(input("enter the value: "))
match x:
    case 0:
        print("x is zero")
    
    case 4 if x % 2 == 0:
        print("x % 2 == 0 and case is 4")
    case _ if x < 10:
        print("x is < 10")
    case _:
        print(x)