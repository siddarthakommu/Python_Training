import random
names = [
    "Chris Harry K",
    "Siddartha Kommu",
    "Mayank Pathak",
    "Balaji Pappala",
    "Sumanth Kumar Valluru",
    "Japa Harish",
    "Lakshmi Sahithi Vanga",
    "G. VANI",
    "Indukuru Sravani",
    "Sirneni Pavan Sai",
    "Suman Kumar Ghorai",
    "Yugesh Karoti",
    "Chundi Vishnu Priya",
    "Sri Sanjana Indugula",
    "G. Santosh Kumar",
    "Gangiredla Karthik",
    "Venkata Naidu Punnana",
    "Pedapalli Suresh",
    "Prathamesh Pahune",
    "Venkata Krishna Kolli",
    "Ram Mishra"
]

def arrange(names):
    d={}
    p=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
    l=sorted(names,key=lambda x:random.random())
    for i in l:
        if i not in d:
            s=random.choice(p)
            while s in d.values():
                s=random.choice(p)
            d[i]=s
                      
    return d

print(arrange(names))