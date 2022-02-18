"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def comparison(first, second):
    if not isinstance(first, str) and not isinstance(second, str):
        return 0

    if first == second:
        return 1    

    if len(first) > len(second):        
        return 2         
        
    if second == "learn":
        return 3    
                        

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    
    TEST_LIST = [(12, 12), ("word", "word"), ("world", "word"), ("world", "learn"), ("worlds", "learn")]
    
    for string_1, string_2 in TEST_LIST:
        print(comparison(string_1, string_2))

    
if __name__ == "__main__":
    main()
