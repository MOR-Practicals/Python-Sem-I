def fact(n):
    if (n==0):
       return 1
    else:
        factorial=1
        for i in range(1,n+1):
            factorial*=i
        return factorial
         
def main():
    n = int(input("Enter a number to calculate its factorial :"))
    if(n<0):
        print("INPUT SHOULD NOT BE NEGATIVE")
    else:
        print(n,"!=",fact(n))

if __name__=="__main__": 
    main()