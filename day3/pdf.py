with open("C:/Users/user/OneDrive/Desktop/sample.pdf",'rb') as f:
    content=f.read()
    with open("sample.pdf", 'wb') as f:
        f.write(content)
   