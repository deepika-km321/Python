class A:
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        print(self.add(10,20))
        return a-b

a=A()
#print(a.add(10,20))
print(a.sub(23,60))