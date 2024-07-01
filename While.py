# i=10
# while i>=1:
#     print(i)
#     i=i-1

#list
# l=[10,40,80,22,45]
# print(l[0])
# print(l[1:4])
# l[0]=110
# print(l)
# l.append(9)
# print(l)
# l.insert(1,"hello")
# print(l)
# l.remove("hello")
# print(l)
# del l[5]
# print(l)
# l2=[]
# l2.extend(l)
# # l.clear()
# print(l2)
# l2.pop(2)
# print(l2)

#tuple
t=(44,89,67,10,33)
l=list(t)
l[0]=100
t=tuple(l)
print(t)

#set

# s={"90","20","11","88"}
# print(s)
# s.add(44)
# print(s)
# s.update(["hello","hi"])
# print(s)
# s.remove("hi")
# print(s)
# s1={100,99}
# s2=s.union(s1)
# print(s2)

#dict

d={"one":1,"two":2,"three":3}
print(d["one"])
print(d.get("three"))
d["one"]=7
print(d)
d["four"]=4
print(d)
for i in d:
    print(i)
for i in d:
    print(d[i])
for i in d.keys():
    print(i)
for i in d.values():
    print(i)

for k,v in d.items():
    print(k,v)
d.pop("one")
print(d)

 









