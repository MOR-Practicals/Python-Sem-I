def main():
    x=int(input("Enter 1st number : "))
    y=int(input("Enter 2nd number : "))
    while(1):
        print("MENU: \n1: +\n2: - \n3: *\n4: / \n5: // \n6: %\n7: Change numbers\n0: Exit")
        char = int(input("ENTER CHOICE : "))
        if(char==1):
            print(x,"+",y,"=",x+y)
        elif(char==2):
            print(x,"-",y,"=",x-y)
        elif(char==3):
            print(x,"*",y,"=",x*y)
        elif(char==4):
            if(y==0):
                print("Second number cannot be 0 for this operation")
            else:
                print(x,"/",y,"=",x/y)
        elif(char==5):
            if(y==0):
                print("Second number cannot be 0 for this operation")
            else:
                print(x,"//",y,"=",x//y)    
        elif(char==6):
            if(y==0):
                print("Second number cannot be 0 for this operation")
            else:
                print(x,"%",y,"=",x%y)
        elif(char==7):
            main()
        elif(char==0):
            exit()
        else :
            print("INVALID CHOICE")


if __name__=="__main__": 
    main()
    

