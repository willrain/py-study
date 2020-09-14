# 2강 클래스 이해하기 1

class Employee:
    empCount = 0

    # 생성자
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def display_count(self):
        print("전체 종업원 수는 %d" % Employee.empCount)
        return

    def display_employee(self):
        print("Name : " + self.name + ", Salary:" + str(self.salary))


emp1 = Employee("A", 100)
emp2 = Employee("B", 200)

emp1.display_employee()
emp2.display_employee()

print("전체 종업원 수 : %d " % Employee.empCount)