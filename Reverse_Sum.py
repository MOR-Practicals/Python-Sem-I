def compute(n):
    rev = 0   
    addall = 0 
    while(n > 0):  
        rem = n%10    
        rev = (rev *10) + rem
        addall+=rem    
        n=n//10
    return rev,addall
        
def main():
    n = int(input("Enter the number:"))
    reverse, sum= compute(n)
    while(1):
        print("MENU")
        print("1. Reverse")
        print("2. Sum")
        print("3. Change number")
        print("0. Exit")
        char = int(input("ENTER CHOICE : "))
        if(char==1):
            print("REVERSE OF",n,"IS",reverse)
        elif(char==2):
            print("SUM OF ALL DIGITS OF",n,"IS",sum)
        elif(char==3):
            main()
        elif(char==0):
            exit()
        else :
            print("INVALID CHOICE")


if __name__=="__main__": 
    main()
    