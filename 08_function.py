
def by_tree(number):
    if number % 3 == 0:
        return cube(number)
    else:
        return False


def cube(number):
    return number ** 3


def main():
    result = by_tree(6)
    print(result)


main()



