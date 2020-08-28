import pyperclip

pyperclip.copy('Hello world')
print(pyperclip.paste())


PASSWORD = {
    'naver': 'naver12345',
    'gmail': 'gmail1234',
    'facebook': 'facebook1234'
}


def main():
    site = input('input your site')

    password = PASSWORD[site]

    if not password:
        print('not valid site. try again')
        site = input('input your site')

    else:
        pyperclip.copy(password)
        print('your password is copied.')


main()

