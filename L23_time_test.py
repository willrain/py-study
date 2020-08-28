import time
import subprocess
import logging


# 타이머 프로그램
def countdown(sec):
    time_left = sec

    while time_left > 0:
        logging.debug(time_left)
        time.sleep(1)
        time_left -= 1


def calc_prod():
    product = 1
    for i in range(1, 1000000):
        product = product + 1
    return product


def main():
    start = time.time()
    prod = calc_prod()
    end = time.time()
    print('The result is {0}'.format(len(str(prod))))
    print('Took {0} seconds to calculate.'.format(end - start))

    # 타이머 프로그램 호출
    howmay_sec = 3
    countdown(howmay_sec)
    # 카운트다운이 끝나면 사운드 파일을 실행
    subprocess.Popen(['start', 'alram.wav'], shell=True)
    print("타이머 프로그램 호출 completed.")

    # 계산기 프로그램 호출
    #subprocess.Popen('C:\\windows\\System32\\calc.exec')
    print("계산기 프로그램 호출 completed.")

    # 다른 파이썬 프로그램 호출
    subprocess.Popen(['python.exe', 'L20__Beta_openapi_search.py'])
    print("다른 파이썬 프로그램 호출 completed.")


if __name__ == '__main__':
    main()

