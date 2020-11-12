n=0
s=0
while(n%3==0)or(n%2==0):
    n=eval(input("Introduceti n"))
    if n%2==0:
        s+=n
print("Suma numerelor pare este",s)
