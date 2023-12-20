import random

class BotStateMachine:
    def __init__(self):
        self.state = 'start'

    def process_input(self, input_text):
        response = ''

        if self.state == 'start':
            response = 'Здравствуйте! Для работы выберите пункт главного меню:'
            self.state = 'main_menu'

        elif self.state == 'main_menu':
            if input_text == 'Выбор функции':
                response = 'Выберите задание:'
                self.state = 'task_menu'
            elif input_text == 'Завершить программу':
                response = 'Программа завершена.'
                self.state = 'exit'
            else:
                response = 'Некорректный ввод. Пожалуйста, выберите пункт меню.'

        elif self.state == 'task_menu':
            if input_text == 'Любое число до 1000':
                response = str(random.randint(1, 1000))
            elif input_text == 'Любая буква':
                response = f"Случайная буква: {random.choice('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')}"
            elif input_text == 'Завершить программу':
                response = 'Программа завершена.'
                self.state = 'exit'
            else:
                response = 'Некорректный ввод. Пожалуйста, выберите задание.'

        return response


state_machine = BotStateMachine()


def process_message(message):
    input_text = message.text
    response = state_machine.process_input(input_text)

    if state_machine.state == 'exit':
        return response, True
    else:
        return response, False
