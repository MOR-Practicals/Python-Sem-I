def PalindromeCheck(str): 
    reverse=""
    for i in str:
        reverse=i+reverse
    return reverse==str

def main():
    str=input("Enter the string :") 
    if(PalindromeCheck(str)):
        print(str,"is a palindrome")
    else:
        print(str,"is not a palindrome")

if __name__=="__main__": 
    main()





