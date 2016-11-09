import re
data=open('access.log', 'r')
list=re.findall(r'[0-9]{1,3}[.][0-9]{1,3}[.][0-9]{1,3}[.][0-9]{1,3}', str(data.read()))
list2=sorted(list)
list3=[]
for b in list2:
    if b not in list3:
        list3.append(b)
    else:
        pass
#print(list3)
list4=re.findall(r'[0-9]{1,3}[.][0-9]{1,3}[.][0-9]{1,3}', str(list3))
print(list4)
list5=re.split(r'([0-9]{1,3}[.][0-9]{1,3}[.][0-9]{1,3})[.][0-9]{1,3}', str(list2))
#print(list5)
i=1
list_all=[]
for a in list5:
    if i%2==0:
        list_all.append(a)
    else:
        pass
    i=i+1
#print(list_all)
j=0
k=0
while j<len(list4):
    print()
    print(list4[j])
    while k<len(list_all) and list4[j]==list_all[k]:
        print(list2[k])
        k=k+1
    j=j+1

