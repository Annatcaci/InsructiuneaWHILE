n=int(input("introduceti n"))
s=0
p=1
nr=1
while nr<=n:
    s+=nr
    p*=nr
    nr+=1
print("Suma numerelor este",s,", produsul este p",p,",iar media este",float(s/n))