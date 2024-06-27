# class A:
#     def m1(self):
#         print("this is m1 method from class a")
#
# class B(A):
#     def m1(self):
#         print("this is m2 method from class b")
#         super().m1()
#
# b=B()
# b.m1()

# class parent:
#     name="deepika"
# class child(parent):
#     name="lali"
#     def test(self):
#         print(super().name)
#
# c=child()
# print(c.name)
# c.test()


class Bank:
    def rateofinterest(self):
        return 0
class Xbank(Bank):
    def rateofinterest(self):
        return 10
class Ybank(Bank):
    def rateofinterest(self):
        return 20

y=Ybank()
print(y.rateofinterest())

x=Xbank()
print(x.rateofinterest())



