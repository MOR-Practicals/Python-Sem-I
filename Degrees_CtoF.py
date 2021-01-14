def compute(c):
    f=(c*9/5)+32
    return f

def main():
    c = int(input("Enter temprature in degree celsius :"))
    print("Temprature in degrees Fahrenheit :",compute(c))
    
if __name__=="__main__":
    main() 

