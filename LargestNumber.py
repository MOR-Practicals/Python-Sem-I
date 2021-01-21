def findMax(arr): 
    ini = arr[0]  
    for i in arr: 
        if i > ini : 
            ini = i 
    return ini

def main():
    print("Enter numbers with a whitespace in between (Example: 23 12 43 4 3 ...) ") 
    arr = [int(x) for x in input().split()]
    print(findMax(arr),"is the largest number")
    
if __name__=="__main__": 
    main()