import math

def compute(a,b,c):
    d = (b**2) - (4*a*c)
    if (d<0):
        r=-b/(2*a)
        im=math.sqrt(-d)/(2*a)
        print("Alpha :",r,"+",im,"i")
        print("Beta :",r,"-",im,"i")
    else:            
        alpha = (-b-math.sqrt(d))/(2*a)
        beta = (-b+math.sqrt(d))/(2*a)
        print("Alpha :",alpha)
        print("Beta :",beta)

def main():
    a = int(input("Enter coefficient of x^2 :"))
    if(a==0):
        print("INVALID INPUT, COEFFICIENT OF x^2 CANNOT BE 0")
        main()
    else:
        b = int(input("Enter coefficient of x^1 :"))
        c = int(input("Enter coefficient of x^0 :"))
        compute(a,b,c)

if __name__=="__main__": 
    main() 

