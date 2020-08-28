#from services import calculator


def main():
    print(calculator.add(3, 4))
    print(calculator.substract(3, 4))
    print(calculator.multiply(3, 4))

# 파라미터를 스트링 타입으로 설정
def validate_password(password=''):
    if len(password) < 8:
        return False
    elif password.isalpha():
        return False
    elif password.isnumeric():
        return False
    else:
        return True


def ch10():
    user_password = input('input your password: ')
    if validate_password(user_password):
        print('valid password')
    else:
        print('not valid password')


ch10()



