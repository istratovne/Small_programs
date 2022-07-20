print('Добро пожаловать в программу шифрования/дешифрования методом Цезаря!')

ENGALPHA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
RUSALPHA = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

def info_request():
    while True:
        direction = input('Будем шифровать или дешифровать?(e/d) ').lower()
        if not direction == 'e' and not direction == 'd':
            print('Введите ответ e или d ')
        else:
            break            
    while True:
        lang = input('Какой алфавит будем использовать?(en/ru) ').lower()
        if not lang == 'en' and not lang == 'ru':
            print('Введите ответ en или ru ')
        else:
            break        
    while True:
        try: 
            key = int(input('Введите ключ шифрования '))
            break
        except TypeError:
            print('Введите целое число ')
        except ValueError:
            print('Введите целое число ')            
    while True:
        text = input('Введите текст шифровки ')
        if key == '':
            print('Введите хоть какой-нибудь текст ')
        else:
            break
    return direction, lang, key, text
    
def encription():
    direction, lang, key, text = info_request()
    if lang == 'en':
        for i in text:
            if direction == 'e':
                if i.isalpha():
                    char = ENGALPHA[(ENGALPHA.index(i.upper()) + key) % len(ENGALPHA)]
                    print(char if i.isupper() else char.lower(), end = '')
                else:
                    print(i, end = '')
            else:
                if i.isalpha():
                    char = ENGALPHA[(ENGALPHA.index(i.upper()) - key) % len(ENGALPHA)]
                    print(char if i.isupper() else char.lower(), end = '')
                else:
                    print(i, end = '')
    else:
        for i in text:
            if direction == 'e':
                if i.isalpha():
                    char = RUSALPHA[(RUSALPHA.index(i.upper()) + key) % len(RUSALPHA)]
                    print(char if i.isupper() else char.lower(), end = '')
                else:
                    print(i, end = '')
            else:
                if i.isalpha():
                    char = RUSALPHA[(RUSALPHA.index(i.upper()) - key) % len(RUSALPHA)]
                    print(char if i.isupper() else char.lower(), end = '')
                else:
                    print(i, end = '')
                    

if __name__ == '__main__':
    encription()