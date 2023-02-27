#ADDITION OF FRACTIONAL NUMBERS
#INPUT
n1=int(input("Enter the numerator of number1:"))
d1=int(input("Enter the denominator of number1:"))
n2=int(input("Enter the numerator of number2:"))
d2=int(input("Enter the denominator of number2:"))
hcf=1
num1=1
num2=1
for i in range(1,(d1*d2)+1):
    if d1%i==0 and d2%i==0:
        hcf=i
lc=(d1*d2)/hcf
lcm=int(lc)
print(lcm)
for i in range(1,int(lcm)+1):
    if d1*i==lcm:
        num1=i
        
for i in range(1,lcm+1):
    if d2*i==lcm:
        num2=i
print("the addition of the given numbers is:",(n1*num1)+(n2*num2),"/",lcm)
f1=(n1*num1)+(n2*num2)
f2=lcm
import math

print("simplest form is:",_fractions_(f1,f2))
