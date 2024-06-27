# class A:
#     def m1(self):
#         print("this is m1 method of a class")
# class B(A):
#
#     def m2(self):
#         print("this is m2 method of b class")
# b=B()
# b.m2()
# b.m1()


# class A:
#     x,y=10,20
#     def m1(self):
#         print(self.x+self.y)
# class B(A):
#     a,b=4,5
#     def m2(self):
#         print(self.a-self.b)
#
# b=B()
# b.m2()
# b.m1()



# class A:
#     x,y=10,89
#     def m1(self):
#         print(self.x+self.y)
#
# class B(A):
#     a,b=5,2
#     def m2(self):
#         print(self.a+self.b)
#
# class C(B):
#     i,j=7,7
#     def m3(self):
#         print(self.i+self.j)
#
# c=C()
# c.m3()
# c.m2()
# c.m1()

# class A:
#     x,y=10,89
#     def m1(self):
#         print(self.x+self.y)
#
# class B(A):
#     a,b=5,2
#     def m2(self):
#         print(self.a+self.b)
#
# class C(A):
#     i,j=7,7
#     def m3(self):
#         print(self.i+self.j)
#
# c=C()
# c.m3()
# c.m1()
#
# b=B()
# b.m2()
# b.m1()

class A:
    x,y=10,89
    def m1(self):
        print(self.x+self.y)

class B:
    a,b=5,2
    def m2(self):
        print(self.a+self.b)

class C(A,B):
    i,j=7,7
    def m3(self):
        print(self.i+self.j)

c=C()
c.m3()
c.m2()
c.m1()




