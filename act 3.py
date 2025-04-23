print("enter marks of 3 subjects")

m1=int(input())
m2=int(input())
m3=int(input())

t=m1+m2+m3

a=t/3

if a>80 and a<100:
    print("grade a+")

elif a>60 and a<80:
    print("b+")

else:
    print("c- or f--") 
