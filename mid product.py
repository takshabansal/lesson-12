num=int(input("Enter the number:"))
t=num
nl=0
while t>0:
    nl=nl+1
    t=int(t/10)
print("The length of the word is ",nl)
if nl>=4:
    nl=int(nl/2)
    chk=0
    while num>0:
        rem=num%10
        if chk==nl:
            midone=rem
        elif chk==(nl-1):
            midtwo=rem
        num=int(num/10)
        chk=chk+1
    prod=midone*midtwo
    print("Product of Middle digits(" +str(midone)+ "*" +str(midtwo)+")=", prod)
else:
    print("It is not a 4 or more digit number!")