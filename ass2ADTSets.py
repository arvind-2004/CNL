n=int(input("Enter the number of element in set 1: "))
S1=set()
print("Enter the Elements of set 1: ")
for i in range(n):
  a=int(input())
  S1.add(a)
print("First Set is: ",S1)

#-----------------------------------------------------------------------------

n=int(input("Enter the number of elements in set 2: "))
S2=set()
print("Enter the elements of set 2: ")
for i in range(n):
  a=int(input())
  S2.add(a)
print("Second Set is: ",S2)
#-------------------------------------------------------------------
#menu
i = 1
while i == 1:
    print("\n----------------MENU----------------\n")
    print("1. Insert New Element")
    print("2. Remove an Element")
    print("3. Search an element")
    print("4. Return Size of the Set")
    print("5. Intersection of Two Sets")
    print("6. Union of Two Sets")
    print("7. Difference Between Two Sets")
    print("8. Exit")
    ch = int(input("ENTER YOUR CHOICE: "))

    if(ch==1):
        s = (int(input("In which Set you want Insert New Element (1 or 2)")))
        if(s==1):
            new1=(int(input("Enter element you want to Insert in Set1")))
            S1.add(new1)
        elif(s==2):
            new2=(int(input("Enter element you want to Insert in Set2")))
            S2.add(new2)
        else:
            print("INVALID INPUT")
        print("S1 = ",S1)
        print("S2 = ",S2)
    elif(ch==2):
        r = (int(input("From which set you want to Remove an Element (1 or 2)")))
        if(r==1):
            new1=(int(input("Enter the Element you want to Remove form Set1")))
            S1.remove(new1)
        elif(r==2):
            new2=(int(input("Enter the Element you want to Remove form Set2")))
            S2.remove(new2)
        else:
            print("INVALID INPUT")
        print("S1 = ",S1)
        print("S2 = ",S2)
    elif(ch==3):
        s = (int(input("In which Set you want Search Element (1 or 2)")))
        if(s==1):
            n=(int(input("Enter element you want to Search in Set1: ")))
            if s in S1:
                print("Element Found")
            else:
                print("Element Not Found")

        elif(s==2):
            n=(int(input("Enter element you want to Search in Set2: ")))
            if s in S2:
                print("Element Found")
            else:
                print("Element Not Found")
        else:
            print("INVALID INPUT")

    elif(ch==4):
        print("Total Number of Elements in Set1 = ", len(S1))
        print("Total Number of Elements in Set2 = ", len(S2))

    elif(ch==5):
        print("Intersection of Set1 and Set2 are: ")
        print(S1 & S2)

    elif(ch==6):
        print("Union of Set1 and Set2 is: ")
        print(S1 | S2)

    elif(ch==7):
        print("Difference Between Set1 and Set2: ", S1 - S2)
        print("Difference Between Set2 and Set1: ", S2 - S1)
    elif(ch==8):
        i = 0
    else:
        print("INVALID INPUT")
        i = 1
