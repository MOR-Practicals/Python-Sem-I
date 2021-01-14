def checkarmstrong(n):
    length=len(n)
    n=int(n)
    dummy=n
    sum=0
    while(dummy>0):
        temp=dummy%10
        sum+=temp**length
        dummy=dummy//10
    if (sum==n):
        return True
    else:
        return False

def main():
    n = input("Enter a number:")
    if (checkarmstrong(n)):
        print(n,"is an armstrong number")
    else:
        print(n,"is not an armstrong number")

if __name__=="__main__": 
    main()