# 4강 클래스 변수와 인스턴스 변수

# 인스턴스 변수 : 각각의 인스턴스마다 가지고 있는 고유의 데이터
# 클래스 변수 : java static 개념, 모든 인스턴스가 공유하는 데이터


class Employee:
    empCount = 0  # 클래스 변수
    raise_ratio = 1.1

    # 클래스 메소드 (static 메소드)
    @classmethod
    def change_raise_ratio(cls, ratio=1):
        # 인상률이 1보다 작은 경우 재입력 요청
        while float(ratio) < 1:
            print('인상률은 1보다 큰 값을 입력해 주세요. ')
            ratio = input("인상률을 다시 입력해 주세요. \n")

        ratio = float(ratio)
        cls.raise_ratio = ratio
        print("인상률 : {}% 적용 ".format(round((ratio - 1)*100)))

    def __init__(self, name, salary):
        self.name = name  # 인스턴스 변수
        self.salary = salary
        Employee.empCount += 1

    def emp_print(self):
        print('{}, {}'.format(self.name, self.salary))

    def raise_salary(self):
        self.salary = int(self.salary * Employee.raise_ratio)


def emp_count_print():
    print('전체 종업원 수는 {}'.format(Employee.empCount))


emp1 = Employee('김말동', 20000)
emp2 = Employee('고길동', 10000)

emp_count_print()

emp1.emp_print()
emp2.emp_print()

emp1.raise_salary()
emp1.emp_print()

# 인상률 변경
Employee.change_raise_ratio(0.9)
emp1.emp_print()
emp1.raise_salary()
emp1.emp_print()

