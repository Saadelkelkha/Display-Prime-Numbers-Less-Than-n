prime=[]
n=int(input("Type the number"))
for i in range (1,n) :
    p=0
    for j in range (1,i+1) :
        if i%j==0 :
            p=p+1
    if p==2 :
      prime.append(i)
print("Prime integers less than",n,"are :",prime)