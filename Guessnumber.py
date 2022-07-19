from random import randint


def main():
    print('Добро пожаловать в числовую угадайку. Введите верхнюю границу диапазона генерации числа')
    while True:
        try:
            border = int(input())
            break
        except ValueError:
            print('Нужно ввести целое число')
    num = randint(1, border)    
    flag = True
    counter = 1
    while flag == True:
        print(f'Введите целое число от 1 до {border}')
        n = input()
        if not (n.isdigit() and 1 <= int(n) <= border):
            print(f'А может быть все-таки введем целое число от 1 до {border}?')
        else:
            n = int(n)
            if n < num:
                print('Ваше число меньше загаданного, попробуйте еще разок')
                counter += 1
            elif n > num:
                print('Ваше число больше загаданного, попробуйте еще разок')
                counter += 1
            elif n == num:
                print(f'Вы угадали c {counter} попытки, поздравляем!')
                print('Спасибо, что играли в числовую угадайку')
                choise = input()
                if choise == 'y':
                    flag = True
                elif choise == 'n':
                    flag = False
                else:
                    print('Ну ты дурак совсем? Давай пока, короче')
                    flag = False
                
if __name__ == '__main__':
    main()
            