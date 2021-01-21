def my_mean(arr):
    return sum(arr)/len(arr)
   
def main():
    print("Enter numbers with a whitespace in between (Example: 23 12 43 4 3 ...) ") 
    arr = [float(x) for x in input().split()]
    print("Mean :",my_mean(arr))

if __name__=="__main__": 
    main()
