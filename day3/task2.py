users = [("Alice", 25, "New York"), ("Bob", 17, "Los Angeles"), ("Charlie", 30,
"Chicago")]

d={name:age for name,age,city in users if age>18}
print(d)