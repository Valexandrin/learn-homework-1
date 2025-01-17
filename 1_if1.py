"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран

"""

def get_action(user_age):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    if user_age < 0:
        return 'Вы еще не родились'

    if user_age < 7:
        return 'Вы ходите в детский сад'

    if user_age < 17:
        return 'Вы учитесь в школе'

    if user_age < 22:
        return 'Вы учитесь в ВУЗе'    

    if user_age < 60:
        return 'Вы работаете'                

    return 'Вы пенсионер'  
        

def main():
    user_age = int(input("Введите Ваш возраст: "))
    output_info = get_action(user_age)
    print(output_info)


if __name__ == "__main__":
    main()
