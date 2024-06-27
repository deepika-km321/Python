class Employee:
    def __init__(self,eid,ename,esal):
        self.eid=eid
        self.ename=ename
        self.esal=esal
    def display(self):
        print(self.eid,self.ename,self.esal)