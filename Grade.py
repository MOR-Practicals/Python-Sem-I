def grade(maxmarks,obtainedmarks):
    percentage=(sum(obtainedmarks)/(5*maxmarks))*100
    if(percentage>=91):
        return "A"
    elif(percentage>=81 and percentage<91):
        return "B"
    elif(percentage>=71 and percentage<81):
        return "C"
    elif(percentage>=61 and percentage<71):
        return "D"
    else:
        return "E"

def main():
    mm=int(input("Enter maximum marks(1 subject) : "))
    if(mm<0):
        print("MAXIMUM MARKS CANNOT BE NEGATIVE")
        main()
    else:
        print("Enter the marks obtained in 5 subjects with a whitespace in between (Example: 23 12 43 4 3) ") 
        arr = [float(x) for x in input().split()]
        if(len(arr)!=5):
            print("ENTER MARKS FOR 5 SUBJECTS")
            main()
        elif(max(arr)>mm):
            print("OBTAINED MARKS CANNOT BE MORE THAN MAXIMUM MARKS")
            main()
        else:
            print("GRADE : ",grade(mm,arr))
  
if __name__=="__main__": 
    main()