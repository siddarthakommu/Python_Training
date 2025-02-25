#4. dictionary contains names as keys and values as scores. You need to return the name and the score of the highest scorer.

dici={"rohit":45,"virat":18,"dhawan":41,"rahul":1}
highest=float("-inf")

for k,v in dici.items():
    if v>highest:
        highest=v
        key=k

print(key,highest)    