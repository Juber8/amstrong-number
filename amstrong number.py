# amstring number
n=int(input('enter the number'))
org=n
sum=0
while (n>0):
    sum = sum + (n%10)*(n%10)*(n%10)
    n=n//10
if org ==sum:
    print('its amstrong number')
else:
    print('not a amstrong number')

x=121
org = x
rev=0
i=0
while (i<x):
    rev = (rev*10) + (x%10)
    x= x//10
if rev == org:
    print('its palindrom')
else:
    print('not a palindrom')