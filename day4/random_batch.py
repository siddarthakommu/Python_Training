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

def pairs(names):
    l1=[]
    l2=[]
    l=sorted(names,key=lambda x:random.random())
    n=len(l)
    for i in l:
        if i not in l1 and len(l1)<n/2:
            l1.append(i)
        else:
            l2.append(i)
            
    return f'batch1:{l1}-----------batch2{l2}'

print(pairs(names))
    
 