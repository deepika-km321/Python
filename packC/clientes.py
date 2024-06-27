import sys
sys.path.append("C:/Users/DELL/PycharmProjects/new/packA")
sys.path.append("C:/Users/DELL/PycharmProjects/new/packB")
# import emp
# obj=emp.Employee("e12","deepika",12000)
# obj.display()
# import stu
# obj1=stu.Student(112,"lali",3000)
# obj1.displaystu()

from emp import Employee
obj=Employee("e12","deepika",12000)
obj.display()
from stu import Student
obj1=Student(112,"lali",3000)
obj1.displaystu()