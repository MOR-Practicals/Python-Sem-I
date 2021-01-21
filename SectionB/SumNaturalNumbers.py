def SumN_Formula(n):
    return n*(n+1)/2

def SumN_Iteration(n):
    sum=0
    while(n>0):
        sum+=n
        n-=1
    return sum

def main():
    print("SUM OF FIRST n NATURAL NUMBERS")
    n = int(input("Enter the number:"))
    if(n<1):
        print("n cannot be less than 1")
        main()
    else:
        while(1):
            print("MENU")
            print("1. Sum (Formula)")
            print("2. Sum (Iteration)")
            print("3. Change the value of n")
            print("0. Exit")
            char = int(input("ENTER CHOICE : "))
            if(char==1):
                print("Sum :",SumN_Formula(n))
            elif(char==2):
                print("Sum :",SumN_Iteration(n))
            elif(char==3):
                main()
            elif(char==0):
                exit()
            else :
                print("INVALID CHOICE")
            
if __name__=="__main__": 
    main()
    