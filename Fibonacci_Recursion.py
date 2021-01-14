def fibonacci(n):
   if (n==1):
      return 0
   elif (n==2):
      return 1
   else:
      return (fibonacci(n-1)+fibonacci(n-2))

def main():
   n = int(input("How many terms of fibonacci sequence do you want to display? "))
   for i in range(1,n+1):
      print(fibonacci(i))

if __name__=="__main__": 
   main()