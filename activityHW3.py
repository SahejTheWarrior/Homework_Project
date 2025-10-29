num=int(input("enter a number: "))
t=num
numLen =0
while t>0:
    numLen=numLen+1
    t=int(t/10)
if numLen>=4:
    numLen=int(numLen/2)
    chk=0
    while num>0:
        rem=num%10
        if chk==numLen:
            Mid1=rem
        elif chk==(numLen-1):
            Mid2=rem
        num=int(num/10)
        chk=chk+1
    product=Mid1*Mid2
    print("\n There are 4 or more digits in your number")
else:
  print("\nYour number is either 1, 2 or 3 digits long")