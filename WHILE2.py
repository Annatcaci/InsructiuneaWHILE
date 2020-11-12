a=1
tp=0
tn=0
s1=0
s2=0
while a<=12:
    t=eval(input("Introduceti temperaturile"))
    if t>=0:
        tp+=1
        s1+=t
    else:
        tn+=1
        s2+=t
    a+=1
m1=round(float(s1/tp),2)
m2=round(float(s2/tn),2)
print("Media pozitiva este",m1,"iar negativa este",m2)
