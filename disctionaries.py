a={
    "name":"robot",
    "fathername":"robota",
    "mothername":"robotica",
    "age":100,
    "contact no": +110011000110,
    "programme":["python","java"]}
print(a)
print(type(a))
print(len(a))
print(a["age"])
#acces
x=a["name"]
print(x)
y=a.get("age")
print(y)
#keys
books={"english":"london",
       "maths":"india",
       "history":"greek",
       "science":True,
       "marks":55}
_a=books.keys()
print(_a)
print(books)
books["algebra"]:"by me"
print(_a)
_b={"my loan":"15000/month",
    "my loan1":"16000/month",
    "my loan2":"18000/month",}
_b1=_b.keys()
_b["my loan41"]="25000/month"
print(_b)
#values
c={"name":"sohel",
   "div":"class a",
   "percentage":"78%"}

c1=c.values()
print(c1)
c["class rank"]="1 st rank"
print(c1)
c["name"]="maaz"
print(c)
items_1={"item1":"maaz",
       "item2":"tanveer",
       "item3":"fazal",
       "item4":"saeed maner",}
i=items_1.items()
print(items_1)
items_1["item1"]="maaz"
print(i)
z={"marks1":95,"marks2":85,"marks3":87}
z1=z.items()
print(z1)
z["marks1"]=195
print(z1)
z2=z.items()
print(z2)
z["marks4"]=100
print(z2)
z={"marks1":95,"marks2":85,"marks3":87}
if "marks4" in z:
    print("yes, its present")
else:
    print("no, not present")
z1={"marks1":95,"marks2":85,"marks3":87,"marks4": 100}
if "marks4" in z1:
    print("yes, its present")
else:
    print("no, not present")
#change items
z2={"house1":1200000,"house2":1500000,"house3":2000000}
z2["house1"]=2500000
print(z2)
z2.update({"house5":4000000,"house6":4500000})
z2.update({"house1":5000000})
print(z2)
#adding items
#remove
'''
z3={"name":"sohel","father name":"abdul","mother name":"nazeema"}
z3.pop("name")
print(z3)
z3.popitem()
print(z3)
z3.clear()
print(z3)
del z3
print(z3)
'''
#for loops
z4={"name":"abc","work":"xyz","salaray":55000}
for x in z4:
    print(x)
    
for x in z4:
    print(z4[x])
    
for x in z4.keys():
    print(x)
    
for x in z4.values():
    print(x)

for x , y in z4.items():
    print(x,y)
#copy    
z5={"train":"golgumbaz express","train no":17869,"bijapur to hubli": "6hours"}
z5c=z5.copy()
z5c1=dict(z5)
print(z5c)
print(z5c1)
#nested
myliferules={
"1st rule":{"professional":"focused", "work":"hard",
                "salary":"strive for what you done",
                "relation":"upto wrk place only"
            },
"2nd rule":{"social":"all is illusion",
                 "relation":"almost fake to show off",
                 "time":"wastage of time"
            },
"3 rd rule":{"personal":"long life",
                 "focus":"should be full",
                 "expectations":"dont go for iy",
                 "time":"give less than tha professional to amke happy life"
             }
    }
print(myliferules)

_1strule={"professional":"focused", "work":"hard",
                "salary":"strive for what you done",
                "relation":"upto wrk place only"
            }
_2ndrule={"social":"all is illusion",
                 "relation":"almost fake to show off",
                 "time":"wastage of time"
            }
_3rdrule={"personal":"long life",
                 "focus":"should be full",
                 "expectations":"dont go for iy",
                 "time":"give less than tha professional to amke happy life"
             }
myfamily1={
    "_1strule":_1strule,
    "_2ndrule":_2ndrule,
    "_3rdrule":_3rdrule}

print(myfamily1)

