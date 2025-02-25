def total(s):
    s=s.lower()
    count=0
    for char in s:
        if char in 'aeiou':
            count+=1
    return count
s="Hi WelcOme to Tamilnadu"
print(total(s))