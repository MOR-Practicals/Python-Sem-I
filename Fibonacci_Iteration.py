def fibonacci(n):
   first=0
   second=1
   for i in range(1,n+1):
      print(first)
      temp=first+second
      first=second
      second=temp


def main():
   n = int(input("How many terms of fibonacci sequence do you want to display? "))
   fibonacci(n)

if __name__=="__main__": 
   main()