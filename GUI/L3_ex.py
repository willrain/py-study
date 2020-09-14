# 3강 클래스 이해하기 2

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def empInfo(self):
        print('{}, {}'.format(self.name, self.salary))


emp1 = Employee('김말동', 20000)
emp2 = Employee('고길동', 10000)


# 메모리 주소 확인
print(id(emp1))
print(id(emp2))

# emp1 과 emp2가 같은 클래스인지 확인하는 방법
emp1_class = emp1.__class__
emp2_class = emp2.__class__

print(id(emp1_class))
print(id(emp2_class))



# 인스턴스 변수에 접근하기 위해서는 인스턴스명을 사용한다.
print(emp1.name + " : " + str(emp1.salary))

emp1.empInfo()
emp2.empInfo()