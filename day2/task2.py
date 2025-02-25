
def total(sen):
    
    count=0
    for char in sen:
        if char==" ":
            count+=1
    return count+1

sen="Hi, welcome to tamilnadu"
print(total(sen))
