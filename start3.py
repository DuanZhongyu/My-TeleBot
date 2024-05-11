# Created 2024.04.28
# by 段仲彧

# 功能 3 —— 药物兼容性查询
# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
import bot
import func

accepting_input = False
first_input = None


def start3_01(chat_id):
    global accepting_input, first_input
    first_input = None
    accepting_input = True

    bot.main_bot.send_message(chat_id=chat_id,
                              text='Укажите название препарата, который Вы хотите назначить пациенту (в МНН):\n\n'
                                   '_(Если нужно повторно ввести или выйти, введите команду напрямую.)_',
                              parse_mode='Markdown')


@bot.main_bot.message_handler(func=lambda msg: msg.text is not None and accepting_input)
def handle_text_messages(message):
    global first_input, accepting_input

    if not message.text.lower().startswith('/start'):
        if first_input is None:
            if message.text.lower() in func.start3_drug:
                first_input = message.text
                _text_03 = f'Название лекарства, которое Вы хотите назначить пациенту, ' \
                           f'- *{first_input}*.\n\nУкажите название ' \
                           f'препарата, который уже принимает пациент (в МНН):\n\n_(Название лекарства, назначенного_ ' \
                           f'_пациенту, было неверным. Если нужно повторно ввести или выйти, введите команду напрямую.)_'
            else:
                _text_03 = f'Названия препарата, который Вы хотите назначить пациенту, ' \
                           f'- {message.text} - *не существует*.\n' \
                           f'\n*Его необходимо повторно ввести.*\n\n' \
                           f'_(Если нужно повторно ввести или выйти, введите команду напрямую.)_'

            bot.main_bot.send_message(chat_id=message.chat.id,
                                      text=_text_03,
                                      parse_mode='Markdown')
        else:
            if message.text.lower() in func.start3_drug[first_input.lower()]:
                __text_03 = f'Название лекарства, которое Вы хотите назначить пациенту, - *{first_input}*.\n' \
                            f'Название лекарства, которое пациент уже принимает, - *{message.text}*.\n\n' \
                            f'Взаимодействие найдено, ознакомьтесь по ссылке:\n' \
                            f'{func.start3_drug[first_input.lower()][message.text.lower()]}\n\n' \
                            f'_(Если нужно повторно ввести или выйти, введите команду напрямую.)_'
            else:
                __text_03 = f'Название лекарства, которое Вы хотите назначить пациенту, - *{first_input}*.\n' \
                            f'Название лекарства, которое пациент уже принимает, - *{message.text}*.\n\n' \
                            f'Взаимодействие *не найдено*.\n\n' \
                            f'_(Если нужно повторно ввести или выйти, введите команду напрямую.)_'

            bot.main_bot.send_message(chat_id=message.chat.id,
                                      text=__text_03,
                                      parse_mode='Markdown')
    else:
        accepting_input = False
        bot.main_bot.send_message(chat_id=message.chat.id,
                                  text=f'Запрос закрыт.\n\n'
                                       f'Пожалуйста, повторно введите услугу, к которой Вы хотите получить доступ:\n\n'
                                       f'{func.ending_words[6]}')


if __name__ == "__main__":
    bot.main_bot.polling()
