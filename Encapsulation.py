# class myClass:
#
#     __a=10
#     def display(self):
#         print(self.__a)
# obj=myClass()
# obj.display()

# class myClass:
#     def __displa(self):
#         print("this is dispay method of private")
#     def test(self):
#         print("to call display method")
#         self.__displa()
#
# m=myClass()
# m.test()

class myClass:
    __a=10
    def test(self,a):
        self.__a=a
    def display(self):
        print(self.__a)
m=myClass()
#m.display()
m.test(60)
