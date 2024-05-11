# Created 2024.04.28
# by 彧同学

# 主文件。下述代码用于控制执行各个功能（共四个）的脚本运行。
# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
import bot
import start1
import start2
import start3
import start4


@bot.main_bot.message_handler(commands=['start'])
def main_start(message):
    bot.main_bot.send_message(chat_id=message.chat.id,
                              text='*Здравствуйте!*\n'
                                   'Добро пожаловать в чатбот *ПсихПартнер*. Данный бот может '
                                   'выполнять следующие функции:\n\n'
                                   '/start1 - Опросник по депрессии и рекомендации по лечению.\n'
                                   '/start2 - Клинические рекомендации по лечению.\n'
                                   '/start3 - Взаимодействие между лекарствами.\n'
                                   '/start4 - Противопоказание.',
                              parse_mode='Markdown')


@bot.main_bot.message_handler(commands=['start1'])  # 调查问卷以及药物推荐
def start_1(message):
    bot.main_bot.send_message(chat_id=message.chat.id,
                              text=f'*Здравствуйте!*\n'
                                   f'Пройдите опрос, по результатам которого можно предположить депрессию у '
                                   f'Вашего пациента.',
                              parse_mode='Markdown')
    start1.start1_01(message.chat.id)


@bot.main_bot.message_handler(commands=['start2'])  # 临床治疗策略
def start_2(message):
    bot.main_bot.send_message(chat_id=message.chat.id,
                              text=f'*Здравствуйте!*\n'
                                   f'Здесь Вы можете ознакомиться с клиническими рекомендациями '
                                   f'по лечению депрессии.',
                              parse_mode='Markdown')
    start2.start2_01(message.chat.id)


@bot.main_bot.message_handler(commands=['start3'])  # 药物兼容性分析
def start_3(message):
    bot.main_bot.send_message(chat_id=message.chat.id,
                              text=f'*Здравствуйте!*\n'
                                   f'Это функция для анализа совместимости лекарственных средств!',
                              parse_mode='Markdown')
    start3.start3_01(message.chat.id)


@bot.main_bot.message_handler(commands=['start4'])  # 禁忌症药物分析
def start_4(message):
    bot.main_bot.send_message(chat_id=message.chat.id,
                              text=f'*Здравствуйте!*\n'
                                   f'Эта функция предназначена для запроса информации о противопоказанных '
                                   f'препаратах при некоторых заболеваниях.',
                              parse_mode='Markdown')
    start4.start4_01(message.chat.id)


while True:    # 循环不停
    try:
        if __name__ == "__main__":
            bot.main_bot.polling()
    except Exception as e:
        print(e)
        continue
