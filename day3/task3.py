text = "Hello World!"
s={}
s={i.lower() for i in text if i not in s and i.isalpha()}
print(s)