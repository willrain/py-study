# 사용자 예외 생성
class BizException(Exception):
    pass


try:
    file = open('email_maker.py', 'r')

    line_num = 1
    while True:
        line = file.readline()
        if not line:
            break

        print(str(line_num) + ' : ' + line)
        line_num = line_num + 1

    file.close()

    number = float('hello')
    print(number)

except FileNotFoundError as e:
    print('File Not Found : ' + str(e))

except ValueError as e:
    #print('Not a number : ' + str(e))
    raise BizException(e)

