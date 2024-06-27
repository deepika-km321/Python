# class Myclass:
#     def myfun(self):
#         pass
#     def display(self,name):
#         print("hello",name)
# a=Myclass()
# a.display("deepika")

# class Hello:
#     def m1(self):
#         print("this is instance method")
#     @staticmethod
#     def m2(self,name):
#         print(self,name)
#
# h=Hello()
# h.m1()
# h.m2("hello","deepika")
# Hello.m2("hello","sweety")

# class Hello:
#     a,b=100,50
#     def add(self):
#         print(self.a+self.b)
#     def sub(self):
#         print(self.a*self.b)
# h=Hello()
# h.add()
# h.sub()

# i,j=10,20
# class hello:
#     a,b=1,2
#     def add(self,x,y):
#         print(x+y)
#         print(self.a+self.b)
#         print(i+j)
# h=hello()
# h.add(10,20)


# i,j=10,20
# class hello:
#     i,j=1,2
#     def add(self,i,j):
#         print(i+j)
#         print(self.i+self.j)
#         print(globals()['i']+globals()['j'])
# h=hello()
# h.add(10,10)


# class myclass:
#     def __init__(self):
#         print("hello this is constructor")
#     def m1(self):
#         print("hello")
#     def add(self,a,b):
#         return a+b
#
#
# m=myclass()
# m.m1()
# print(m.add(10,2))


# class A:
#     name="deepika"
#     def __init__(self,name):
#         print(self.name)
#         print(name)
# a=A("deepu")


class emp:
    def __init__(self,eid,ename,sal):
        self.eid=eid
        self.ename=ename
        self.sal=sal
    def display(self):
        print(self.ename,self.eid,self.sal)
e=emp("deepika",11,12000)
e.display()













