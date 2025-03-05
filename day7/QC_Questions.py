#max,second largest element in an array
# l=[1,4,5,3]
# first=second=float('-inf')

# for i in l:
#     if i>first:
#         second=first
#         first=i
#     elif i>second and i!=first:
#         second=i

# print(first,second)

# Write a program to count a uppercase letter present in the string.
# s="HelLo WorLd"
# for i in s:
#     if i.isupper():
#         print(i,end=" ")

# String reverse without using built in functions and check whether it is a palindrome or not

# s="siddu"
# t=''
# for i in s:
#     t=i+t
# print(t)
# if s==t:
#     print("palindrome")
# else:
#     print("not a palindrome")

# Create an array and find the sum of the elements which are at even index positions in the array
# arr=[1,2,3,4,5]
# sum=0
# for i in range(len(arr)):
#     if i%2==0:
#         sum+=arr[i]
# print(sum)

# Print all common elements of two lists
# l1=[1,2,3,4]
# l2=[2,3,4,5]
# l3=[]
# for i in l1:
#     for j in l2:
#         if i==j:
#             l3.append(i)

# print(l3)

# Longest word in a given sentence
s="Longest word in a given sentence"
s1=s.split()
maxi=0
for i in s1:
    if len(i)>maxi:
        maxi=len(i)
        k=i
print(maxi,k)









