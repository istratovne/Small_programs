from random import choice

DIGITS = '0123456789'
LOWERCASE_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
UPPERCASE_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
PUNCTUATION = '!#$%&*+-=?@^_'


def info_request():
    while True:
        try: 
            pass_amount = int(input('Какое количество паролей сгенерировать? '))
            break
        except TypeError:
            print('Введите целое число')
        except ValueError:
            print('Введите целое число')
    while True:
        try:
            pass_len = int(input('Укажите длину одного пароля '))
            break
        except TypeError:
            print('Введите целое число')
        except ValueError:
            print('Введите целое число')
    while True:
        include_digits = input('Включать ли в пароль цифры от 0 до 9?(y/n) ').lower()
        if not include_digits == 'y' and not include_digits == 'n':
            print('Введите ответ y или n')
        else:
            break
    while True:        
        include_uppercase = input('Включать ли в пароль прописные буквы?(y/n) ').lower()
        if not include_uppercase == 'y' and not include_uppercase == 'n':
            print('Введите ответ y или n')
        else:
            break
    while True:    
        include_lowercase = input('Включать ли в пароль строчные буквы?(y/n) ').lower()
        if not include_lowercase == 'y' and not include_lowercase == 'n':
            print('Введите ответ y или n')
        else:
            break
    while True:        
        include_punctuation = input('Включать ли символы !#$%&*+-=?@^_? (y/n) ').lower()
        if not include_punctuation == 'y' and not include_punctuation == 'n':
            print('Введите ответ y или n')
        else:
            break
    while True:        
        exception = input('Исключать ли неоднозначные символы il1Lo0O? (y/n) ').lower()
        if not exception == 'y' and not exception == 'n':
            print('Введите ответ y или n')
        else:
            break
    chars = ''    
    if include_digits == 'y':
        chars += DIGITS
    if include_uppercase == 'y':
        chars += UPPERCASE_LETTERS
    if include_lowercase == 'y':
        chars += LOWERCASE_LETTERS
    if include_punctuation == 'y':
        chars += PUNCTUATION
    if exception == 'y':
        for i in 'il1Lo0O':
            chars = chars.replace(i, '')        
    return pass_amount, pass_len, chars


def generate_password():
    pass_amount, pass_len, chars = info_request()
    passwords = []
    for i in range(pass_amount):
        password = ''
        for j in range(pass_len):
            password += choice(chars)
        passwords.append(password)
    print(*passwords)


if __name__ == '__main__':
    generate_password()