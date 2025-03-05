text = "Hello World!"
s={}
s={i.lower() for i in text if i.isalpha()}
print(s)