#3. find the second largest element in the list
'''li=[6,4,1,8,9,3,4,10]
first,second=li[0],li[1]

for i in li:
    if i>first:
        second =first
        first=i
    if i>second and i<first:
        second=i

print(second)'''

def highest2(numbers):
    num1=num2=float("-inf")
    for i in numbers:
        if i>num1:
            num2=num1
            num1=i
        if num2>i and i<num1:
            num2=i
    return num2

l1=[6,4,1,8,9,3,4,10]
print(highest2(l1))