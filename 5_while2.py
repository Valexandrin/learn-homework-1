"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например:
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user() которая с помощью функции input()
  просит пользователя ввести вопрос, а затем, если вопрос есть
  в словаре, программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую
    
"""

from random import choice


questions_and_answers = {
    "Как дела?": ["Хорошо!", "Порядок!", "OK"], 
    "Что делаешь?": ["Программирую", "Ем", "Читаю твои вопросы!"],
    "Сколько тебе лет?": [1, 2, 20, 24, 15, 60, 105, 48]
    }

def ask_user(answers_dict):    
    while True:
        user_asks = input("Задай вопрос: ")
        answers = questions_and_answers.get(user_asks)
        if answers:
            print(choice(answers))
        '''
        if user_asks in answers_dict:            
            print(choice(answers_dict[user_asks]))
        '''

    
if __name__ == "__main__":
    ask_user(questions_and_answers)
