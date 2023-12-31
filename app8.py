# Импортируем библиотеку random для генерации случайных чисел
import random 
# Задаем константы с максимальным числом попыток и случайным число
max_tries = 5 
number = random.randint(1, 10)

print('Добро пожаловать в игру "Угадай число"!')
print('Я загадал число от 1 до 10 попробуй угадать его за 5 попыток.')

# Отслеживаем количество попыток
tries = 0 
# Цикл продолжается, пока попытки не кончились и число не угадано
while tries < max_tries:
    # Запришиваем ввод числа пользователем
    guess = int(input('Введи число: '))
    # Сравниваем введенное число с загаданным
    if guess == number:
        print('Поздравляю, ты угадал(а) число! Тебе потребовалось', tries + 1, '')
        break
    elif guess < number:
        print('Загаданное число больше!')
    else:
        print('Загаданное число меньше!')
# Увеличиваем счетчик попыток
    tries += 1
# Выводим сообщение, если попытки кончились
else:
    print('', number)
print('')