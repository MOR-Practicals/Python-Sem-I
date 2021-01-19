def main():
    str="Exasperation"

    print(len(str)) #12
    print(str[2]) #a
    print(str[-4]) #t
    print(str[6:11]) #ratio
    print(str[6:-1]) #ratio
    print('a' in str) #True
    print('z' in str) #False
    print('a' not in str) #False
    print('z' not in str) #True
    print(str.upper()) #EXASPERATION
    print(str.lower()) #exasperation
    print(str.swapcase()) #eXASPERATION
    print(str.casefold()) #exasperation (casefold is more aggresive than lower)
    print(str.capitalize()) #Exasperation
    print(str.center(26,'x')) #xxxxxxxExasperationxxxxxxx
    print(str.count('a')) #2
    print(str.startswith('Ex')) #True
    print(str.endswith('tion')) #True
    print(str.find('a')) #2
    print(str.find('a',3)) #7
    print(str.rfind('a')) #7
    print(str.find('z')) #-1
    #print(str.index('z')) #Exception (Otherwise similar to find())
    print(str.replace('Exas','O')) #Operation
    print(str.isalnum()) #True
    print(str.isalpha()) #True
    print(str.isdecimal()) #False
    print(str.isdigit()) #False	
    print(str.isidentifier()) #True
    print(str.islower()) #False
    print(str.isnumeric())	#False
    print(str.isspace()) #False
    print(str.isupper()) #False
    print(str.zfill(20)) #00000000Exasperation
    print('ABC*MNO*XYZ'.split('*')) #['ABC', 'MNO', 'XYZ']
    print('*'.join(['ABC', 'MNO', 'XYZ'])) #ABC*MNO*XYZ

if __name__=="__main__": 
    main()
    

