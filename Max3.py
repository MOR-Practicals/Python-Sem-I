def maxout3(x,y,z):
    if (x >= y) and (x >= z): 
        max=x 
    elif (y >= x) and (y >= z): 
        max=y 
    else: 
        max=z 
    return max

def main():
    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter second number:"))
    num3 = int(input("Enter third number:"))
    cm=maxout3(num1,num2,num3)
    print(cm,"is the largest out of the given numbers")

if __name__=="__main__": 
    main()