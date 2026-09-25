s="aaab"
l=list(s)
l1=[]
l2=[]

for i in range(len(s)):
    if i==0:
        l1.append(l[i])

    elif i!=0 and l[i]!=l[i-1]:
            l1.append(l[i])

    else:
        if l[i] not in l2:
            l2.append(l[i])
         
        else:
         l1=[]
         l2=[]
         break

print("".join(l1+l2))

            
