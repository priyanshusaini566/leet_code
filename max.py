s="4206"
l1=list(s)
l2=[]

for i in range(len(l1)):
    if int(l1[i])%2!=0:
        l2.append(l1[i])

if l2==[]:
    print("")

else:
 print(max(l2))
