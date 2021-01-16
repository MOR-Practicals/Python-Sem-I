def AsciiToChar():
   n=int(input("Enter ascii value: "))
   print(n,"->",chr(n))

def CharToAscii(): 
    str=input("Enter a character/string: ")
    for i in str:
        print(i,"->",ord(i))

def main():
    while(1):
        print("MENU")
        print("1.Ascii code to character")
        print("2.Character to ascii code")
        print("0.Exit")
        char=int(input("ENTER CHOICE: "))
        if(char==1):
            AsciiToChar()
        elif(char==2):
            CharToAscii()
        elif(char==0):
            exit()
        else :
            print("INVALID CHOICE")

if __name__=="__main__": 
   main()
