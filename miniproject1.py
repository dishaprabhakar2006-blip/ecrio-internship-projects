def get_num():
    try:
        n1=float(input("Enter number 1:"))
        n2=float(input("Enter number 2:"))
    except ValueError:
        print("Invalid Input! Enter only numbers")
        return get_num()
    return n1,n2
history=[]
def add(n1,n2):
    history.append(f"{n1}+{n2}={n1+n2}")
    return n1+n2
def sub(n1,n2):
    history.append(f"{n1}-{n2}={n1-n2}")
    return n1-n2
def mul(n1,n2):
    history.append(f"{n1}*{n2}={n1*n2}")
    return n1*n2
def div(n1,n2):
    if(n2==0):
        return "Cannot divide by 0"
    history.append(f"{n1}+{n2}={n1/n2}")
    return n1/n2

while(True):
    print("*Calculator Operations*")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.History")
    print("6.Exit")
    choice=int(input("Enter your choice:"))
    if(choice==1):
        n1,n2=get_num()
        print("Sum:",add(n1,n2))

    elif(choice==2):
        n1,n2=get_num()
        print("Difference:",sub(n1,n2))
    elif(choice==3):
        n1,n2=get_num()
        print("Product:",mul(n1,n2))
    elif(choice==4):
        n1,n2=get_num()
        print("Quotient:",div(n1,n2))
    elif(choice==5):
        if history:
            print(history)
        else:
            print("No History yet!")
        
    elif(choice==6):
        print("Exiting")
        break
    else:
        print("Invalid Choice!")

