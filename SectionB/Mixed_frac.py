def mixed_frac(numerator,denominator):
    if(numerator%denominator==0):
        return "WHOLE NUMBER {}/1".format(numerator/denominator)
    else:
        return "MIXED FRACTION {} {}/{}".format(numerator//denominator, numerator%denominator, denominator)
   
def main():
    n = int(input("Enter numerator :"))
    d = int(input("Enter denominator :"))
    if(d==0):
        print("DENOMINATOR CANNOT BE 0")
        main()
    else:
        if(n<d):
            print("PROPER FRACTION {}/{}".format(n,d))
        else:
            print(mixed_frac(n,d))
        

if __name__=="__main__": 
    main()
