def factorial(n):
   if (n==0) or (n == 1):
       return 1
   else:
       return n*factorial(n-1)

def main():
    n = int(input("Enter a number to calculate its factorial :"))
    if(n<0):
        print("INPUT SHOULD NOT BE NEGATIVE")
    else:
        fact=factorial(n)
        print(n,"!=",fact)

if __name__=="__main__": 
    main()