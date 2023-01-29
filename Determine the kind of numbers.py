import math
x=int(input("This program determines an integer number is + or - and even or odd.\nPlease enter an integer number:  "))
if x==0:
    print("You entered Zero")
    exit()    
print("The number you intered is: Even " if x%2==0  else "The number you intered is: Odd " )
print("The number you intered is: Positive "  if x>0  else "The number you intered is: Negative")