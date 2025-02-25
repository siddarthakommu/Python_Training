#6. Remove the duplicates from the list and return it to the user.
li=[1,2,3,1,1,3]
li2=[]
for i in li:
    if i not in li2:
        li2.append(i)

print(li2)


