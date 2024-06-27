# def sum(*args):
#     s=0
#     for i in args:
#         s=s+i
#     print("sum is:",s)
# sum(9,3,2)

# def sum(a,b,c):
#     print(a,b,c)
# l=[90,6,3]
# sum(*l)

# def myFun(**a):
#     for i,j in a.items():
#         print(i,j)
# myFun(a="one",b="two",c="three")

def myFun(a,b,c):
    print(a,b,c)
l={'a':"one",'b':"two",'c':"three"}
myFun(**l)