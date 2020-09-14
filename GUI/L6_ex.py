# 6강 클래스 메소드 사용 2

class Person:
    def __init__(self, year, month, day, gender):
        self.year = year
        self.month = month
        self.day = day
        self.gender = gender

    def __str__(self):
        return "{}년 {}월 {}일에 태어난 {}입니다.".format(self.year, self.month, self.day, self.gender)

    # 클래스 메소드를 인스턴스 생성자로 처리
    @classmethod
    def id_constructor(cls, id):
        first, second = id.split('-')
        gender = second[0]

        if gender == '1' or gender == '2':
            year = '19' + first[:2]
        else:
            year = '20' + first[:2]

        if (int(gender) % 2) == 0:
            gender = '여성'
        else:
            gender = '남성'

        month = first[2:4]
        day = first[4:6]

        return cls(year, month, day, gender)


def id_process(id):
    first, second = id.split('-')
    gender = second[0]
    if gender == '1' or gender == '2':
        year = '19' + first[:2]
    else:
        year = '20' + first[:2]

    if (int(gender) % 2) == 0:
        gender = '여성'
    else:
        gender = '남성'

    month = first[2:4]
    day = first[4:6]

    return year, month, day, gender


id_number1 = "751111-1006016"
id_number2 = "151109-4006016"

person1 = Person.id_constructor(id_number1)
person2 = Person.id_constructor(id_number2)

print(person1)
print(person2)
