import math    

def sin(x,n):
    sinx=0
    for i in range (n):    
        sinx+=((-1)**i)*(x**(2*i+1))/math.factorial(2*i+1)
    print("Sin ({}) = {}".format(x,sinx))   

def main():
    n=int(input("ENTER THE VALUE OF n (FOR LARGE VALUES OVERFLOW ERROR MAY OCCUR):"))
    x=float(input("ENTER THE VALUE OF x (RADIAN):"))      
    sin(x,n)

if __name__=="__main__": 
    main()