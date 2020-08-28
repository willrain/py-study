import logging


# 콘솔 로깅
#logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

# 파일 로깅
logging.basicConfig(filename='log.txt', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

logging.debug('Start of program')


def factorial(n):
    logging.debug('Start of factorial(%s) ' % (n))
    total = 1
    for i in range(n + 1):
        if not i:
            continue
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(%s)' % (n))
    return total

print(factorial(5))
logging.debug('End of program ')
