def checkLeap(Year):
   if((Year%400==0)
      or 
   (Year%100!=0)and 
   (Year%4==0)):
     print("Given Year is a Leap Year")
   else:
     print("Given Year isn't a leap Year")
Year=int(input("Enter the Year to be checked:"))
checkLeap(Year)