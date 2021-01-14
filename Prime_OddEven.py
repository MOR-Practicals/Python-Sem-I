import math

def checkPrime(n):
    flag = 0   
    for i in range(2,math.floor(math.sqrt(n))+1): 
        if(n%i==0):
            flag=1
            break
    return flag

def checkOddEven(n):
    flag = 0
    if(n%2==0):
        flag=1
    return flag

def main():
    n = int(input("Enter the number:"))
    while(1):
        print("MENU")
        print("1. Check Prime")
        print("2. Check Odd/Even")
        print("3. Change number")
        print("0. Exit")
        char = int(input("ENTER CHOICE : "))
        if(char==1):
            if(n<2):
                print("INPUT SHOULD BE GREATER THAN 2 FOR THIS OPTION")
            else:
                pc=checkPrime(n)
                if(pc==1):
                    print(n,"IS NOT A PRIME NUMBER")
                else:
                    print(n,"IS A PRIME NUMBER")
        elif(char==2):
            oc=checkOddEven(n)
            if(oc==1):
                print(n,"IS EVEN")
            else:
                print(n,"IS ODD")
        elif(char==3):
            main()
        elif(char==0):
            exit()
        else :
            print("INVALID CHOICE")


if __name__=="__main__": 
    main()
    