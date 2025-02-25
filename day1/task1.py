#1. Find the closest number to zero in the given list

l1=[3,4,5,6,8,2,-1,-3]
mini=l1[0]

for i in range(len(l1)):
    if abs(l1[i])<abs(mini):
        mini=l1[i]

print(mini)

