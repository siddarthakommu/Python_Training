#5. Given an array of integers nums, return the number of good pairs.A pair (i, j) is called good if nums[i] == nums[j] and i < j.

arr=[1,2,3]
c=0

for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i]==arr[j] and i<j:
            c+=1           
print(c)