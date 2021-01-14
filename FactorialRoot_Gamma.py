import math

def fact(n):
    return math.gamma(n+1)

def main():
    n=int(input("Enter a number : "))
    while(1):
        print("MENU")
        print("1. Factorial of",n)
        print("2. Factorial of root",n)
        print("3. Change number")
        print("0. Exit")
        char = int(input("ENTER CHOICE : "))
        if(char==1):
            print(fact(n))
        elif(char==2):
            print(fact(math.sqrt(n)))
        elif(char==3):
            main()
        elif(char==0):
            exit()
        else :
            print("INVALID CHOICE")

if __name__=="__main__": 
    main()