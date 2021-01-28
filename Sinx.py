import math    

def sin(x,n):
    sinx=0
    for i in range (n):    
        sinx+=((-1)**i)*(x**(2*i+1))/math.factorial(2*i+1)
    return sinx   

def main():
    n=int(input("ENTER THE VALUE OF n (NUMBER OF TERMS) (FOR LARGE VALUES OVERFLOW ERROR MAY OCCUR):"))
    if(n<1):
        print("n CANNOT BE LESS THAN 1")
        main()
    else:
        x=float(input("ENTER THE VALUE OF x (RADIAN):"))      
        print("Sin ({}) = {}".format(x,sin(x,n)))

if __name__=="__main__": 
    main()
