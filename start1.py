# Created 2024.04.27
# by 彧同学

# 功能 1 —— # 调查问卷以及药物推荐
# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
import bot
import func

last_msg_id_01_01 = None
last_msg_id_01_02 = None

user_answers = []
score = 0
index = 0
lock = 0

last_reply_message_01_id_01 = None
last_reply_message_01_id_02 = None
last_reply_message_01_id_03 = None
last_reply_message_01_id_04 = None
last_reply_message_01_id_05 = None
last_reply_message_01_id_06 = None
last_reply_message_01_id_07 = None

last_reply_message_02_id_01 = None
last_reply_message_02_id_02 = None
last_reply_message_02_id_03 = None
last_reply_message_02_id_04 = None
last_reply_message_02_id_05 = None
last_reply_message_02_id_06 = None

last_reply_message_03_id_01 = None
last_reply_message_03_id_02 = None
last_reply_message_03_id_03 = None
last_reply_message_03_id_04 = None
last_reply_message_03_id_05 = None
last_reply_message_03_id_06 = None
last_reply_message_03_id_07 = None
last_reply_message_03_id_08 = None
last_reply_message_03_id_09 = None
last_reply_message_03_id_10 = None

last_reply_message_04_id_01 = None
last_reply_message_04_id_02 = None
last_reply_message_04_id_03 = None
last_reply_message_04_id_04 = None
last_reply_message_04_id_05 = None
last_reply_message_04_id_06 = None


def start1_01(chat_id):
    global last_msg_id_01_01, score, index
    score = 0
    index = 0

    last_msg_id_01_01 = bot.main_bot.send_message(chat_id=chat_id,
                                                  text=f'Ответьте на вопрос *(1/9)*:\n\n'
                                                       f'{func.start1_questions[0]}',
                                                  reply_markup=func.keyboard(4, '01234'),
                                                  parse_mode='Markdown').message_id


@bot.main_bot.callback_query_handler(func=lambda call: call.data == '0' or
                                     call.data == '1' or call.data == '2' or
                                     call.data == '3' or call.data == '4')
def start1_02(call):
    global score, index, last_msg_id_01_02

    if call.data != '4':
        score += int(call.data)
        user_answers.append(int(call.data))

        index += 1
        if index < len(func.start1_questions):
            bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                           message_id=last_msg_id_01_01,
                                           text=f'Ответьте на вопрос *({index + 1}/9)*:\n\n'
                                                f'{func.start1_questions[index]}',
                                           reply_markup=func.keyboard(4, '01234'),
                                           parse_mode='Markdown')

        else:
            if score <= 4:
                result_text = f'Общее кол-во баллов: *【{score}】*\n\n' \
                              f'У пациента отсутствует депрессия или уровень депрессии минимальный.'
                bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                               message_id=last_msg_id_01_01,
                                               text=f'{result_text}\n\n'
                                                    f'{func.ending_words[4]}',
                                               reply_markup=func.keyboard(3, '4'),
                                               parse_mode='Markdown')
            else:
                if 4 < score <= 9:  # 轻度
                    text = ['легкая', 'легкой']
                elif 9 < score <= 14:  # 中度
                    text = ['умеренная', 'умеренной']
                elif 14 < score <= 19:  # 重度
                    text = ['тяжелая', 'тяжелой']
                else:  # 极度
                    text = ['крайне тяжелая', 'крайне тяжелой']
                result_text = f'Общее кол-во баллов: *【{score}】*\n\n' \
                              f'У пациента *{text[0]} депрессия*. ' \
                              f'Рекомендуется получить медикаментозное лечение и/или консультацию психотерапевта.'
                bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                               message_id=last_msg_id_01_01,
                                               text=result_text,
                                               parse_mode='Markdown')
                last_msg_id_01_02 = bot.main_bot.send_message(chat_id=call.message.chat.id,
                                                              text=f'Хотите получить рекомендации '
                                                                   f'по лечению *{text[1]} депрессии*?',
                                                              reply_markup=func.keyboard(2, '564'),
                                                              parse_mode='Markdown').message_id
    else:
        if index == 0:
            bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                           message_id=last_msg_id_01_01,
                                           text=f'{func.ending_words[0]}',
                                           reply_markup=func.keyboard(1, '78'))
        else:
            global lock
            index -= 1
            score -= user_answers.pop()
            bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                           message_id=last_msg_id_01_01,
                                           text=f'Ответьте на вопрос *({index + 1}/9)*:\n\n'
                                                f'{func.start1_questions[index]}',
                                           reply_markup=func.keyboard(4, '01234'),
                                           parse_mode='Markdown')

            if last_msg_id_01_02 is not None and last_msg_id_01_02 != lock:
                lock = last_msg_id_01_02
                bot.main_bot.delete_message(chat_id=call.message.chat.id,  # 从下一个问题返回上来的
                                            message_id=last_msg_id_01_02)


def start1_03(chat_id, s):
    text = ''
    keyboard = None

    if 4 < s <= 14:  # 中轻度
        text = 'Получал ли пациент лечение от депрессии ранее?'
        keyboard = func.keyboard(2, ['9', '10', '11'])
    elif 14 < s <= 19:  # 重度
        text = 'Получал ли пациент лечение от тяжелой депрессии ранее?'
        keyboard = func.keyboard(2, ['12', '13', '14'])
    elif 19 < s <= 27:  # 极度
        text = 'Получал ли пациент лечение от крайней депрессии ранее?'
        keyboard = func.keyboard(2, ['15', '16', '17'])

    bot.main_bot.edit_message_text(chat_id=chat_id,
                                   message_id=last_msg_id_01_02,
                                   text=text,
                                   reply_markup=keyboard)


@bot.main_bot.callback_query_handler(func=lambda call:
                                     call.data == '5' or call.data == '6' or
                                     call.data == '7' or call.data == '8' or call.data == '_')
def start1_04(call):
    global score, index

    if call.data == '5':
        start1_03(call.message.chat.id, score)
    elif call.data == '6':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_msg_id_01_02,
                                       text=f'{func.ending_words[2]}\n'  # 感谢完成问卷
                                            f'{func.ending_words[3]}\n\n'  # 很高兴可以帮助到你
                                            f'{func.ending_words[4]}',
                                       reply_markup=func.keyboard(3, '_'))  # 更多命令
    elif call.data == '7':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_msg_id_01_01,
                                       text=f'{func.ending_words[1]}\n'  # 感谢完使用此功能
                                            f'{func.ending_words[3]}')  # 很高兴可以帮助到你
    elif call.data == '8':
        score = 0
        index = 0

        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_msg_id_01_01,
                                       text=f'Ответьте на вопрос *(1/9)*:\n\n'
                                            f'{func.start1_questions[0]}',
                                       reply_markup=func.keyboard(4, '01234'),
                                       parse_mode='Markdown')
    elif call.data == '_':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_msg_id_01_02,
                                       text=f'Хотите получить рекомендации '
                                            f'по лечению депрессии?',
                                       reply_markup=func.keyboard(2, '564'))


@bot.main_bot.callback_query_handler(func=lambda call: call.data == '9' or call.data == '10' or call.data == '11')
def start1_05(call):
    global last_reply_message_01_id_01
    global last_reply_message_01_id_02, last_reply_message_01_id_03
    global last_reply_message_01_id_04, last_reply_message_01_id_05
    global last_reply_message_01_id_06, last_reply_message_01_id_07

    if call.data == '9':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_msg_id_01_02,
                                       text=f'Отмечался ли эффект от терапии 1-ой линии?',
                                       reply_markup=func.keyboard(2, ['18', '19', '20']))
    elif call.data == '10':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_msg_id_01_02,
                                       text=f'Вы можете назначить любой из данных препаратов при '
                                            f'лечении пациента, справа '
                                            f'указаны средние терапевтические дозировки.\n\n'
                                            f'*Эсциталопрам* 10-20мг\n'
                                            f'*Сертралин* 50-200мг\n'
                                            f'*Пароксетин* 50-200мг\n'
                                            f'*Флувоксамин* 100-300мг\n'
                                            f'*Фпуоксетин* 20-80мг\n'
                                            f'*Циталопрам* 20-40мг\n'
                                            f'*Агомелатин* 25-50мг\n'
                                            f'*Вортиоксетин* 10-20мг',
                                       parse_mode='Markdown')

        last_reply_message_01_id_01 = bot.main_bot.send_message(chat_id=call.message.chat.id,
                                                                text='Показать схему повышения / отмены  препарата '
                                                                     '*Сертралин*?',
                                                                reply_markup=func.keyboard(5, ['21', '22', '23']),
                                                                parse_mode='Markdown').message_id

        last_reply_message_01_id_02 = bot.main_bot.send_message(chat_id=call.message.chat.id,
                                                                text='Показать схему повышения / отмены  препарата '
                                                                     '*Эсциталопрам*?',
                                                                reply_markup=func.keyboard(5, ['24', '25', '26']),
                                                                parse_mode='Markdown').message_id

        last_reply_message_01_id_03 = bot.main_bot.send_message(chat_id=call.message.chat.id,
                                                                text='Показать схему повышения / отмены  препарата '
                                                                     '*Пароксетин*?',
                                                                reply_markup=func.keyboard(5, ['27', '28', '29']),
                                                                parse_mode='Markdown').message_id

        last_reply_message_01_id_04 = bot.main_bot.send_message(chat_id=call.message.chat.id,
                                                                text='Показать схему повышения / отмены  препарата '
                                                                     '*Флувоксамин*?',
                                                                reply_markup=func.keyboard(5, ['30', '31', '32']),
                                                                parse_mode='Markdown').message_id

        last_reply_message_01_id_05 = bot.main_bot.send_message(chat_id=call.message.chat.id,
                                                                text='Показать схему повышения / отмены  препарата '
                                                                     '*Флуоксетин*?',
                                                                reply_markup=func.keyboard(5, ['33', '34', '35']),
                                                                parse_mode='Markdown').message_id

        last_reply_message_01_id_06 = bot.main_bot.send_message(chat_id=call.message.chat.id,
                                                                text='Показать схему повышения / отмены  препарата '
                                                                     '*Агомелатин*?',
                                                                reply_markup=func.keyboard(5, ['36', '37', '38']),
                                                                parse_mode='Markdown').message_id

        last_reply_message_01_id_07 = bot.main_bot.send_message(chat_id=call.message.chat.id,
                                                                text='Показать схему повышения / отмены  препарата '
                                                                     '*Вортиоксетин*?',
                                                                reply_markup=func.keyboard(5, ['39', '40', '41']),
                                                                parse_mode='Markdown').message_id
        bot.main_bot.send_message(chat_id=call.message.chat.id,
                                  text=func.ending_words[4])
    elif call.data == '11':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_msg_id_01_02,
                                       text='Хотите получить рекомендации по лечению?',
                                       reply_markup=func.keyboard(2, '564'),  # 询问是否愿意获得治疗建议
                                       parse_mode='Markdown')


@bot.main_bot.callback_query_handler(func=lambda call:
                                     call.data == '21' or call.data == '22' or call.data == '23' or
                                     call.data == '24' or call.data == '25' or call.data == '26' or
                                     call.data == '27' or call.data == '28' or call.data == '29' or
                                     call.data == '30' or call.data == '31' or call.data == '32' or
                                     call.data == '33' or call.data == '34' or call.data == '35' or
                                     call.data == '36' or call.data == '37' or call.data == '38' or
                                     call.data == '39' or call.data == '40' or call.data == '41')
def start1_06(call):
    global last_reply_message_01_id_01
    global last_reply_message_01_id_02, last_reply_message_01_id_03
    global last_reply_message_01_id_04, last_reply_message_01_id_05
    global last_reply_message_01_id_06, last_reply_message_01_id_07

    if call.data == '21':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_01_id_01,
                                       text=f'Начальная доза 50 мг, суточную дозу можно '
                                            f'повышать с шагом 50 мг и с интервалом '
                                            f'как минимум одна неделя в течение нескольких недель.',
                                       reply_markup=func.keyboard(3, '42'))
    elif call.data == '22':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_01_id_01,
                                       text=f'Во избежания развития синдрома «отмены» снижать дозировку '
                                            f'необходимо постепенно в течение нескольких недель. Так как в РГЛС '
                                            f'не указаны конкретные дозировку, основываясь на опыте врачей, '
                                            f'рекомендовано снижать на ¼ суточной дозы 1 раз в 1-2 недели (на 25 мг).',
                                       reply_markup=func.keyboard(3, '43'))
    elif call.data == '23':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_01_id_01,
                                       text=f'Терапевтическая доза – 100-150 мг/сутки. Максимальная доза – '
                                            f'200 мг/сутки. Прием 1-2 раза в день (утром и днем).',
                                       reply_markup=func.keyboard(3, '44'))
    elif call.data == '24':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_01_id_02,
                                       text=f'Начальная доза 10 мг/сутки, при необходимости повысить до '
                                            f'20 мг/сутки через 1-2 недели.',
                                       reply_markup=func.keyboard(3, '45'))
    elif call.data == '25':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_01_id_02,
                                       text=f'Постепенно снижать дозировку на ¼ суточной дозы каждые '
                                            f'1-2 недели (на 2,5 мг).',
                                       reply_markup=func.keyboard(3, '46'))
    elif call.data == '26':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_01_id_02,
                                       text=f'Терапевтическая доза – 10-20 мг/сутки, для пожилых – '
                                            f'5-10 мг/сутки. Прием утром.',
                                       reply_markup=func.keyboard(3, '47'))
    elif call.data == '27':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_01_id_03,
                                       text=f'Начальная доза 10 мг/сутки, рекомендовано повышать дозу на 10 мг '
                                            f'до достижения желаемого терапевтического эффекта 1 раз в неделю.',
                                       reply_markup=func.keyboard(3, '48'))
    elif call.data == '28':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_01_id_03,
                                       text=f'В связи с тем, что пароксетин чаще остальных препаратов '
                                            f'группы СИОЗС вызывает симптомы «отмены», прекращать его прием '
                                            f'необходимо очень медленно. Хотя в РГЛС не указана конкретная схема '
                                            f'отмены препараты, врачи рекомендуют снижать суточную '
                                            f'дозу на ¼-1/6 каждые 4-6 недель (на 5 мг).',
                                       reply_markup=func.keyboard(3, '49'))
    elif call.data == '29':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_01_id_03,
                                       text=f'Терапевтическая доза – 20-50 мг. Максимальная доза – 60 мг/сутки. '
                                            f'Прием утром во время еды (в соответствии с гайдом Шталя – принимать на '
                                            f'ночь, но особой разницы нет).',
                                       reply_markup=func.keyboard(3, '50'))
    elif call.data == '30':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_01_id_04,
                                       text=f'Начальная доза 50 мг/сутки, повышение дозировки возможно через 4-7 дней. '
                                            f'Суточную дозу свыше 150 мг рекомендовано разделять 2-3 приема.',
                                       reply_markup=func.keyboard(3, '51'))
    elif call.data == '31':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_01_id_04,
                                       text=f'Во избежания развития синдрома «отмены» снижать дозировку '
                                            f'необходимо постепенно в течение нескольких недель. Так как в РГЛС не '
                                            f'указаны конкретные дозировку, основываясь на опыте врачей, рекомендовано '
                                            f'снижать на ¼ суточной дозы 1 раз в 1-2 недели (на 25 мг).',
                                       reply_markup=func.keyboard(3, '52'))
    elif call.data == '32':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_01_id_04,
                                       text=f'Терапевтическая доза – 100 мг/сутки. Максимальная доза – '
                                            f'300 мг/сутки. Прием вечером.',
                                       reply_markup=func.keyboard(3, '53'))
    elif call.data == '33':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_01_id_05,
                                       text=f'Начальная доза – 20 мг/сутки, при необходимости для '
                                            f'достижения терапевтического эффекта возможно повышение дозировки '
                                            f'постепенно до 60 мг/сутки через несколько недель.',
                                       reply_markup=func.keyboard(3, '54'))
    elif call.data == '34':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_01_id_05,
                                       text=f'Во избежания развития синдрома «отмены» снижать дозировку '
                                            f'необходимо постепенно в течение нескольких недель. Так как в РГЛС '
                                            f'не указаны конкретные дозировки, основываясь на опыте врачей, '
                                            f'рекомендовано принимать препарат по 1 капс через день в течение '
                                            f'2,5 месяцев, затем прекратить прием.',
                                       reply_markup=func.keyboard(3, '55'))
    elif call.data == '35':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_01_id_05,
                                       text=f'Терапевтическая доза – 20 мг/сутки. Максимальная доза – '
                                            f'60 мг/сутки. Прием утром.',
                                       reply_markup=func.keyboard(3, '56'))
    elif call.data == '36':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_01_id_06,
                                       text=f'Начать с 25 мг/сутки, через 2 недели при '
                                            f'необходимости повысить до 50 мг/сутки.',
                                       reply_markup=func.keyboard(3, '57'))
    elif call.data == '37':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_01_id_06,
                                       text=f'Нет необходимости в постепенном снижении дозировки.',
                                       reply_markup=func.keyboard(3, '58'))
    elif call.data == '38':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_01_id_06,
                                       text=f'Терапевтическая доза – 25-50 мг/сутки, на ночь. '
                                            f'Максимальная доза 50 мг/сутки.',
                                       reply_markup=func.keyboard(3, '59'))
    elif call.data == '39':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_01_id_07,
                                       text=f'Начальная доза 10 мг/сутки. При необходимости суточная доза '
                                            f'может быть повышена до 20 мг/сутки или снижена до 5 мг/сутки.',
                                       reply_markup=func.keyboard(3, '60'))
    elif call.data == '40':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_01_id_07,
                                       text=f'Возможно одномоментное прекращение приема препарата без '
                                            f'постепенного снижения суточной дозы. Однако, основываясь на '
                                            f'опыте врачей, во избежание синдрома «отмены» рекомендовано '
                                            f'постепенное снижение дозировки в течение 2 недель (на 5 мг).',
                                       reply_markup=func.keyboard(3, '61'))
    elif call.data == '41':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_01_id_07,
                                       text=f'Терапевтическая доза – 10 мг/сутки. Максимальная доза – 20 мг/сутки.',
                                       reply_markup=func.keyboard(3, '62'))


@bot.main_bot.callback_query_handler(func=lambda call:
                                     call.data == '42' or call.data == '43' or call.data == '44' or
                                     call.data == '45' or call.data == '46' or call.data == '47' or
                                     call.data == '48' or call.data == '49' or call.data == '50' or
                                     call.data == '51' or call.data == '52' or call.data == '53' or
                                     call.data == '54' or call.data == '55' or call.data == '56' or
                                     call.data == '57' or call.data == '58' or call.data == '59' or
                                     call.data == '60' or call.data == '61' or call.data == '62')
def start1_07(call):
    if call.data == '42' or call.data == '43' or call.data == '44':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_01_id_01,
                                       text='Показать схему повышения / отмены  препарата *Сертралин*?',
                                       reply_markup=func.keyboard(5, ['21', '22', '23']),
                                       parse_mode='Markdown')

    elif call.data == '45' or call.data == '46' or call.data == '47':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_01_id_02,
                                       text='Показать схему повышения / отмены  препарата *Эсциталопрам*?',
                                       reply_markup=func.keyboard(5, ['24', '25', '26']),
                                       parse_mode='Markdown')

    elif call.data == '48' or call.data == '49' or call.data == '50':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_01_id_03,
                                       text='Показать схему повышения / отмены  препарата *Пароксетин*?',
                                       reply_markup=func.keyboard(5, ['27', '28', '29']),
                                       parse_mode='Markdown')

    elif call.data == '51' or call.data == '52' or call.data == '53':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_01_id_04,
                                       text='Показать схему повышения / отмены  препарата *Флувоксамин*?',
                                       reply_markup=func.keyboard(5, ['30', '31', '32']),
                                       parse_mode='Markdown')

    elif call.data == '54' or call.data == '55' or call.data == '56':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_01_id_05,
                                       text='Показать схему повышения / отмены  препарата *Флуоксетин*?',
                                       reply_markup=func.keyboard(5, ['33', '34', '35']),
                                       parse_mode='Markdown')

    elif call.data == '57' or call.data == '58' or call.data == '59':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_01_id_06,
                                       text='Показать схему повышения / отмены  препарата *Агомелатин*?',
                                       reply_markup=func.keyboard(5, ['36', '37', '38']),
                                       parse_mode='Markdown')

    elif call.data == '60' or call.data == '61' or call.data == '62':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_01_id_07,
                                       text='Показать схему повышения / отмены  препарата *Вортиоксетин*?',
                                       reply_markup=func.keyboard(5, ['39', '40', '41']),
                                       parse_mode='Markdown')


@bot.main_bot.callback_query_handler(func=lambda call: call.data == '18' or call.data == '19' or call.data == '20')
def start1_08(call):
    global last_reply_message_02_id_01, last_reply_message_02_id_02
    global last_reply_message_02_id_03, last_reply_message_02_id_04
    global last_reply_message_02_id_05, last_reply_message_02_id_06

    if call.data == '18':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_msg_id_01_02,
                                       text=f'Рекомендуется продолжить терапию на протяжение как минимум 6 месяцев.\n\n'
                                            f'{func.ending_words[0]}',
                                       reply_markup=func.keyboard(2, '789'))
    elif call.data == '19':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_msg_id_01_02,
                                       text=f'Вы можете назначить любой из данных '
                                            f'препаратов при лечении пациента, справа '
                                            f'указаны средние терапевтические дозировки.\n\n'
                                            f'*Венлафаксин* 75-375мг\n'
                                            f'*Дулоксетин* 60-120мг\n'
                                            f'*Милнаципран* 100мг\n'
                                            f'*Миртазапин* 15-45мг\n'
                                            f'*Амитриптилин* 150-300мг\n'
                                            f'*Имипрамин* 150-300мг\n'
                                            f'*Кломипрамин* 100-250мг\n'
                                            f'*Пипофезин* 150-500мг',
                                       parse_mode='Markdown')

        last_reply_message_02_id_01 = bot.main_bot.send_message(chat_id=call.message.chat.id,
                                                                text='Показать схему повышения / отмены  препарата '
                                                                     '*Венлафаксин*?',
                                                                reply_markup=func.keyboard(5, ['66', '67', '68']),
                                                                parse_mode='Markdown').message_id

        last_reply_message_02_id_02 = bot.main_bot.send_message(chat_id=call.message.chat.id,
                                                                text='Показать схему повышения / отмены  препарата '
                                                                     '*Дулоксетин*?',
                                                                reply_markup=func.keyboard(5, ['69', '70', '71']),
                                                                parse_mode='Markdown').message_id

        last_reply_message_02_id_03 = bot.main_bot.send_message(chat_id=call.message.chat.id,
                                                                text='Показать схему повышения / отмены  препарата '
                                                                     '*Миртазапин*?',
                                                                reply_markup=func.keyboard(5, ['72', '73', '74']),
                                                                parse_mode='Markdown').message_id

        last_reply_message_02_id_04 = bot.main_bot.send_message(chat_id=call.message.chat.id,
                                                                text='Показать схему повышения / отмены  препарата '
                                                                     '*Амитриптилин*?',
                                                                reply_markup=func.keyboard(5, ['75', '76', '77']),
                                                                parse_mode='Markdown').message_id

        last_reply_message_02_id_05 = bot.main_bot.send_message(chat_id=call.message.chat.id,
                                                                text='Показать схему повышения / отмены  препарата '
                                                                     '*Кломипрамин*?',
                                                                reply_markup=func.keyboard(5, ['78', '79', '80']),
                                                                parse_mode='Markdown').message_id

        last_reply_message_02_id_06 = bot.main_bot.send_message(chat_id=call.message.chat.id,
                                                                text='Показать схему повышения / отмены  препарата '
                                                                     '*Пипофезин*?',
                                                                reply_markup=func.keyboard(5, ['81', '82', '83']),
                                                                parse_mode='Markdown').message_id

        bot.main_bot.send_message(chat_id=call.message.chat.id,
                                  text=func.ending_words[4])
    elif call.data == '20':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_msg_id_01_02,
                                       text='Получал лт поциент лечение от депрессии ранее?',
                                       reply_markup=func.keyboard(2, ['9', '10', '11']),  # 询问是否愿意获得治疗建议
                                       parse_mode='Markdown')


@bot.main_bot.callback_query_handler(func=lambda call:
                                     call.data == '66' or call.data == '67' or call.data == '68' or
                                     call.data == '69' or call.data == '70' or call.data == '71' or
                                     call.data == '72' or call.data == '73' or call.data == '74' or
                                     call.data == '75' or call.data == '76' or call.data == '77' or
                                     call.data == '78' or call.data == '79' or call.data == '80' or
                                     call.data == '81' or call.data == '82' or call.data == '83')
def start1_09(call):
    global last_reply_message_02_id_01, last_reply_message_02_id_02
    global last_reply_message_02_id_03, last_reply_message_02_id_04
    global last_reply_message_02_id_05, last_reply_message_02_id_06

    if call.data == '66':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_02_id_01,
                                       text=f'Начальная доза 37,5 мг 2 раза в день (в соответствии с гайдом Шталя – 37,'
                                            f'5 мг 1 раз в день), постепенное повышение суточной дозы возможно на '
                                            f'75 мг каждые 4-7 дней (безопаснее повышать дозу раз в неделю).',
                                       reply_markup=func.keyboard(3, '86'))
    elif call.data == '67':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_02_id_01,
                                       text=f'Во избежания развития синдрома «отмены» снижать дозировку '
                                            f'необходимо постепенно в течение нескольких недель. Так как в РГЛС не '
                                            f'указаны конкретные дозировку, основываясь на опыте врачей, рекомендовано '
                                            f'снижать на ¼ суточной дозы 1 раз в 1-2 недели (на 37,5 мг).',
                                       reply_markup=func.keyboard(3, '87'))
    elif call.data == '68':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_02_id_01,
                                       text=f'Терапевтическая доза – 150-225 мг/сутки. '
                                            f'Максимальная доза – 375 мг/сутки.',
                                       reply_markup=func.keyboard(3, '88'))
    elif call.data == '69':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_02_id_02,
                                       text=f'Начальная доза 60 мг/сутки 1 раз в день. При необходимости '
                                            f'нарастить дозу до 120 мг/сутки.',
                                       reply_markup=func.keyboard(3, '89'))
    elif call.data == '70':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_02_id_02,
                                       text=f'Во избежания развития синдрома «отмены» снижать дозировку '
                                            f'необходимо постепенно в течение нескольких недель. Так как в РГЛС не '
                                            f'указаны конкретные дозировки, основываясь на опыте врачей, рекомендовано '
                                            f'принимать препарат по 1 табл через день в течение 2,5 месяцев, '
                                            f'затем прекратить прием.',
                                       reply_markup=func.keyboard(3, '90'))
    elif call.data == '71':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_02_id_02,
                                       text=f'Терапевтическая доза - 40-60 мг/сутки. Максимальная доза - 120 мг/сутки.',
                                       reply_markup=func.keyboard(3, '91'))
    elif call.data == '72':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_02_id_03,
                                       text=f'Начальная доза 15 мг/сутки, повышать до наступления желаемого '
                                            f'терапевтического эффекта через 1-2 недели.',
                                       reply_markup=func.keyboard(3, '92'))
    elif call.data == '73':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_02_id_03,
                                       text=f'Во избежания развития синдрома «отмены» снижать дозировку '
                                            f'необходимо постепенно в течение нескольких недель. Так как в РГЛС не '
                                            f'указаны конкретные дозировку, основываясь на опыте врачей, рекомендовано '
                                            f'снижать на ¼ суточной дозы 1 раз в 1-2 недели.',
                                       reply_markup=func.keyboard(3, '93'))
    elif call.data == '74':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_02_id_03,
                                       text=f'Терапевтическая доза – 15-45 мг/сутки. Максимальная доза '
                                            f'45 мг/сутки. Принимать на ночь.',
                                       reply_markup=func.keyboard(3, '94'))
    elif call.data == '75':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_02_id_04,
                                       text=f'Начать с 25-50 мг/сутки, разделив на два приема, или '
                                            f'однократный прием за 2 часа до сна. Повышать на 25-50 мг каждые 3-7 '
                                            f'дней до терапевтического эффекта. Максимальная часть дозы '
                                            f'принимается на ночь (например, утром 50 мг, на ночь 100 мг).',
                                       reply_markup=func.keyboard(3, '95'))
    elif call.data == '76':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_02_id_04,
                                       text=f'Во избежания развития синдрома «отмены» снижать суточную '
                                            f'дозировку необходимо постепенно в течение нескольких недель. '
                                            f'Так как в РГЛС не указаны конкретные дозировки, основываясь на '
                                            f'опыте врачей, рекомендовано снижать на ¼ суточной дозы 1 раз в '
                                            f'1-2 недели (на 25 мг). При появлении синдрома «отмены» '
                                            f'вернуть прошлую дозировку и снижать дозу еще медленнее.',
                                       reply_markup=func.keyboard(3, '96'))
    elif call.data == '77':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_02_id_04,
                                       text=f'Терапевтическая доза – 150-200 мг/сутки. Максимальная доза 300 мг/сутки.',
                                       reply_markup=func.keyboard(3, '97'))
    elif call.data == '78':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_02_id_05,
                                       text=f'Начальная доза 50-75 мг/сутки, разделив на 2-3 приема или в '
                                            f'один прием вечером, если пролонгированная форма. Повышение дозы на '
                                            f'25 мг каждые несколько дней до наступления терапевтического эффекта '
                                            f'(в соответствии с гайдом Шталя повышение дозы необходимо делать '
                                            f'каждые две недели).',
                                       reply_markup=func.keyboard(3, '98'))
    elif call.data == '79':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_02_id_05,
                                       text=f'Во избежания развития синдрома «отмены» снижать дозировку '
                                            f'необходимо постепенно в течение нескольких недель. Так как в РГЛС не '
                                            f'указаны конкретные дозировку, основываясь на опыте врачей, рекомендовано '
                                            f'снижать на ¼ суточной дозы 1 раз в 1-2 недели (на 25 мг).',
                                       reply_markup=func.keyboard(3, '99'))
    elif call.data == '80':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_02_id_05,
                                       text=f'Терапевтическая доза – 100-200 мг/сут. Максимальная доза 250 '
                                            f'мг/сутки (300 мг/сутки при стационарном наблюдении).',
                                       reply_markup=func.keyboard(3, '100'))
    elif call.data == '81':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_02_id_06,
                                       text=f'Начальная доза 25-50 мг в 2 приема (утром и днем), в дальнейшем '
                                            f'постепенно увеличивают дозировку до 150-200 мг в 3-4 прием.',
                                       reply_markup=func.keyboard(3, '101'))
    elif call.data == '82':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_02_id_06,
                                       text=f'Во избежания развития синдрома «отмены» снижать дозировку '
                                            f'необходимо постепенно в течение нескольких недель. Так как в РГЛС не '
                                            f'указаны конкретные дозировку, основываясь на опыте врачей, рекомендовано '
                                            f'снижать на ¼ суточной дозы 1 раз в 1-2 недели (на 25-50 мг).',
                                       reply_markup=func.keyboard(3, '102'))
    elif call.data == '83':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_02_id_06,
                                       text=f'Терапевтическая доза – 150-200 мг/сут. Максимальная доза '
                                            f'– 400-500 мг/сутки.',
                                       reply_markup=func.keyboard(3, '103'))


@bot.main_bot.callback_query_handler(func=lambda call:
                                     call.data == '86' or call.data == '87' or call.data == '88' or
                                     call.data == '89' or call.data == '90' or call.data == '91' or
                                     call.data == '92' or call.data == '93' or call.data == '94' or
                                     call.data == '95' or call.data == '96' or call.data == '97' or
                                     call.data == '98' or call.data == '99' or call.data == '100' or
                                     call.data == '101' or call.data == '102' or call.data == '103')
def start1_10(call):
    if call.data == '86' or call.data == '87' or call.data == '88':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_02_id_01,
                                       text='Показать схему повышения / отмены  препарата *Венлафаксин*?',
                                       reply_markup=func.keyboard(5, ['66', '67', '68']),
                                       parse_mode='Markdown')
    elif call.data == '89' or call.data == '90' or call.data == '91':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_02_id_02,
                                       text='Показать схему повышения / отмены  препарата *Дулоксетин*?',
                                       reply_markup=func.keyboard(5, ['69', '70', '71']),
                                       parse_mode='Markdown')
    elif call.data == '92' or call.data == '93' or call.data == '94':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_02_id_03,
                                       text='Показать схему повышения / отмены  препарата *Миртазапин*?',
                                       reply_markup=func.keyboard(5, ['72', '73', '74']),
                                       parse_mode='Markdown')
    elif call.data == '95' or call.data == '96' or call.data == '97':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_02_id_04,
                                       text='Показать схему повышения / отмены  препарата *Амитриптилин*?',
                                       reply_markup=func.keyboard(5, ['75', '76', '77']),
                                       parse_mode='Markdown')
    elif call.data == '98' or call.data == '99' or call.data == '100':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_02_id_05,
                                       text='Показать схему повышения / отмены  препарата *Кломипрамин*?',
                                       reply_markup=func.keyboard(5, ['78', '79', '80']),
                                       parse_mode='Markdown')
    elif call.data == '101' or call.data == '102' or call.data == '103':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_02_id_06,
                                       text='Показать схему повышения / отмены  препарата *Пипофезин*?',
                                       reply_markup=func.keyboard(5, ['81', '82', '83']),
                                       parse_mode='Markdown')


@bot.main_bot.callback_query_handler(func=lambda call: call.data == '12' or call.data == '13' or call.data == '14')
def start1_11(call):
    global last_reply_message_03_id_01, last_reply_message_03_id_02
    global last_reply_message_03_id_03, last_reply_message_03_id_04
    global last_reply_message_03_id_05, last_reply_message_03_id_06
    global last_reply_message_03_id_07, last_reply_message_03_id_08
    global last_reply_message_03_id_09, last_reply_message_03_id_10

    if call.data == '12':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_msg_id_01_02,
                                       text=f'Вам нужно более подробное лечение?',
                                       reply_markup=func.keyboard(2, ['__', '___', '5']))
    elif call.data == '13':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_msg_id_01_02,
                                       text=f'Вы можете назначить любой из данных препаратов '
                                            f'при лечении пациента, справа '
                                            f'указаны средние терапевтические дозировки.\n\n'
                                            f'*Венлафаксин* 75-375мг\n'
                                            f'*Дулоксетин* 60-120мг\n'
                                            f'*Милнаципран* 100мг\n'
                                            f'*Миртазапин* 15-45мг\n'
                                            f'*Имипрамин* 150-300мг\n'
                                            f'*Кломипрамин* 100-250мг\n'
                                            f'*Эсциталопрам* 10-20мг\n'
                                            f'*Сертралин* 50-200мг\n'
                                            f'*Пароксетин* 20-50мг\n'
                                            f'*Флувоксамин* 100-300мг\n'
                                            f'*Флуоксетин* 20-80мг\n'
                                            f'*Циталопрам* 20-40мг',
                                       parse_mode='Markdown')

        last_reply_message_03_id_01 = bot.main_bot.send_message(chat_id=call.message.chat.id,
                                                                text='Показать схему повышения / отмены  препарата '
                                                                     '*Венлафаксин*?',
                                                                reply_markup=func.keyboard(5, ['107', '108', '109']),
                                                                parse_mode='Markdown').message_id

        last_reply_message_03_id_02 = bot.main_bot.send_message(chat_id=call.message.chat.id,
                                                                text='Показать схему повышения / отмены  препарата '
                                                                     '*Дулоксетин*?',
                                                                reply_markup=func.keyboard(5, ['110', '111', '112']),
                                                                parse_mode='Markdown').message_id

        last_reply_message_03_id_03 = bot.main_bot.send_message(chat_id=call.message.chat.id,
                                                                text='Показать схему повышения / отмены  препарата '
                                                                     '*Миртазапин*?',
                                                                reply_markup=func.keyboard(5, ['113', '114', '115']),
                                                                parse_mode='Markdown').message_id

        last_reply_message_03_id_04 = bot.main_bot.send_message(chat_id=call.message.chat.id,
                                                                text='Показать схему повышения / отмены  препарата '
                                                                     '*Имипрамин*?',
                                                                reply_markup=func.keyboard(5, ['116', '117', '118']),
                                                                parse_mode='Markdown').message_id

        last_reply_message_03_id_05 = bot.main_bot.send_message(chat_id=call.message.chat.id,
                                                                text='Показать схему повышения / отмены  препарата '
                                                                     '*Кломипрамин*?',
                                                                reply_markup=func.keyboard(5, ['119', '120', '121']),
                                                                parse_mode='Markdown').message_id

        last_reply_message_03_id_06 = bot.main_bot.send_message(chat_id=call.message.chat.id,
                                                                text='Показать схему повышения / отмены  препарата '
                                                                     '*Эсциталопрам*?',
                                                                reply_markup=func.keyboard(5, ['122', '123', '124']),
                                                                parse_mode='Markdown').message_id

        last_reply_message_03_id_07 = bot.main_bot.send_message(chat_id=call.message.chat.id,
                                                                text='Показать схему повышения / отмены  препарата '
                                                                     '*Сертралин*?',
                                                                reply_markup=func.keyboard(5, ['125', '126', '127']),
                                                                parse_mode='Markdown').message_id

        last_reply_message_03_id_08 = bot.main_bot.send_message(chat_id=call.message.chat.id,
                                                                text='Показать схему повышения / отмены  препарата '
                                                                     '*Пароксетин*?',
                                                                reply_markup=func.keyboard(5, ['128', '129', '130']),
                                                                parse_mode='Markdown').message_id

        last_reply_message_03_id_09 = bot.main_bot.send_message(chat_id=call.message.chat.id,
                                                                text='Показать схему повышения / отмены  препарата '
                                                                     '*Флувоксамин*?',
                                                                reply_markup=func.keyboard(5, ['131', '132', '133']),
                                                                parse_mode='Markdown').message_id

        last_reply_message_03_id_10 = bot.main_bot.send_message(chat_id=call.message.chat.id,
                                                                text='Показать схему повышения / отмены  препарата '
                                                                     '*Флуоксетин*?',
                                                                reply_markup=func.keyboard(5, ['134', '135', '136']),
                                                                parse_mode='Markdown').message_id

        bot.main_bot.send_message(chat_id=call.message.chat.id,
                                  text=func.ending_words[4])
    elif call.data == '14':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_msg_id_01_02,
                                       text='Хотите получить рекомендации по лечению?',
                                       reply_markup=func.keyboard(2, '564'),  # 询问是否愿意获得治疗建议
                                       parse_mode='Markdown')


@bot.main_bot.callback_query_handler(func=lambda call:
                                     call.data == '107' or call.data == '108' or call.data == '109' or
                                     call.data == '110' or call.data == '111' or call.data == '112' or
                                     call.data == '113' or call.data == '114' or call.data == '115' or
                                     call.data == '116' or call.data == '117' or call.data == '118' or
                                     call.data == '119' or call.data == '120' or call.data == '121' or
                                     call.data == '122' or call.data == '123' or call.data == '124' or
                                     call.data == '125' or call.data == '126' or call.data == '127' or
                                     call.data == '128' or call.data == '129' or call.data == '130' or
                                     call.data == '131' or call.data == '132' or call.data == '133' or
                                     call.data == '134' or call.data == '135' or call.data == '136')
def start1_12(call):
    global last_reply_message_03_id_01, last_reply_message_03_id_02
    global last_reply_message_03_id_03, last_reply_message_03_id_04
    global last_reply_message_03_id_05, last_reply_message_03_id_06
    global last_reply_message_03_id_07, last_reply_message_03_id_08
    global last_reply_message_03_id_09, last_reply_message_03_id_10

    if call.data == '107':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_03_id_01,
                                       text=f'Начальная доза 37,5 мг 2 раза в день (в соответствии с гайдом Шталя – 37,'
                                            f'5 мг 1 раз в день), постепенное повышение суточной дозы возможно '
                                            f'на 75 мг каждые 4-7 дней (безопаснее повышать дозу раз в неделю).',
                                       reply_markup=func.keyboard(3, '139'))
    elif call.data == '108':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_03_id_01,
                                       text=f'Во избежания развития синдрома «отмены» снижать '
                                            f'дозировку необходимо постепенно в течение нескольких недель. '
                                            f'Так как в РГЛС не указаны конкретные дозировку, основываясь на опыте '
                                            f'врачей, рекомендовано снижать на ¼ суточной дозы '
                                            f'1 раз в 1-2 недели (на 37,5 мг).',
                                       reply_markup=func.keyboard(3, '140'))
    elif call.data == '109':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_03_id_01,
                                       text=f'Терапевтическая доза – 150-225 мг/сутки. '
                                            f'Максимальная доза – 375 мг/сутки.',
                                       reply_markup=func.keyboard(3, '141'))
    elif call.data == '110':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_03_id_02,
                                       text=f'Начальная доза 60 мг/сутки 1 раз в день. '
                                            f'При необходимости нарастить дозу до 120 мг/сутки.',
                                       reply_markup=func.keyboard(3, '142'))
    elif call.data == '111':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_03_id_02,
                                       text=f'Во избежания развития синдрома «отмены» снижать дозировку '
                                            f'необходимо постепенно в течение нескольких недель. Так как в РГЛС '
                                            f'не указаны конкретные дозировки, основываясь на опыте врачей, '
                                            f'рекомендовано принимать препарат по 1 табл через день в '
                                            f'течение 2,5 месяцев, затем прекратить прием.',
                                       reply_markup=func.keyboard(3, '143'))
    elif call.data == '112':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_03_id_02,
                                       text=f'Терапевтическая доза - 40-60 мг/сутки. Максимальная доза - 120 мг/сутки.',
                                       reply_markup=func.keyboard(3, '144'))
    elif call.data == '113':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_03_id_03,
                                       text=f'Начальная доза 15 мг/сутки, повышать до наступления '
                                            f'желаемого терапевтического эффекта через 1-2 недели.',
                                       reply_markup=func.keyboard(3, '145'))
    elif call.data == '114':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_03_id_03,
                                       text=f'Во избежания развития синдрома «отмены» снижать дозировку '
                                            f'необходимо постепенно в течение нескольких недель. Так как в РГЛС не '
                                            f'указаны конкретные дозировку, основываясь на опыте врачей, '
                                            f'рекомендовано снижать на ¼ суточной дозы 1 раз в 1-2 недели.',
                                       reply_markup=func.keyboard(3, '146'))
    elif call.data == '115':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_03_id_03,
                                       text=f'Терапевтическая доза – 15-45 мг/сутки. Максимальная '
                                            f'доза 45 мг/сутки. Принимать на ночь.',
                                       reply_markup=func.keyboard(3, '147'))
    elif call.data == '116':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_03_id_04,
                                       text=f'Начальная доза 25 мг/сутки, повышение на 25 мг каждые 3-7 дней до '
                                            f'терапевтической (в соответствии с РГЛС: начальная доза 25 мг 1-3 '
                                            f'раза в сутки, к концу первой недели лечения может быть повышена '
                                            f'до суточной 150-200 мг). Для пожилых пациентов рекомендовано '
                                            f'начать с 25 мг/сутки и повышать постепенно в течение 10 дней '
                                            f'до терапевтической дозировки. В соответствии с гайдом Шталя, '
                                            f'прием утром рекомендован для лечения бессонницы, прием вечером '
                                            f'рекомендован для седативного эффекта в течение дня.',
                                       reply_markup=func.keyboard(3, '148'))
    elif call.data == '117':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_03_id_04,
                                       text=f'Во избежания развития синдрома «отмены» снижать дозировку '
                                            f'необходимо постепенно в течение нескольких недель. Так как в РГЛС не '
                                            f'указаны конкретные дозировку, основываясь на опыте врачей, рекомендовано '
                                            f'снижать на ¼ суточной дозы 1 раз в 1-2 недели (на 25 мг).',
                                       reply_markup=func.keyboard(3, '149'))
    elif call.data == '118':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_03_id_04,
                                       text=f'Терапевтическая доза – 100-150 мг/сутки. '
                                            f'Максимальная доза – 300 мг/сутки. '
                                            f'Для пожилых пациентов применяются более низкие дозы, 50-75 мг/сутки.',
                                       reply_markup=func.keyboard(3, '150'))
    elif call.data == '119':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_03_id_05,
                                       text=f'Начальная доза 50-75 мг/сутки, разделив на 2-3 приема или в '
                                            f'один прием вечером, если пролонгированная форма. Повышение дозы на '
                                            f'25 мг каждые несколько дней до наступления терапевтического эффекта '
                                            f'(в соответствии с гайдом Шталя повышение дозы необходимо '
                                            f'делать каждые две недели).',
                                       reply_markup=func.keyboard(3, '151'))
    elif call.data == '120':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_03_id_05,
                                       text=f'Во избежания развития синдрома «отмены» снижать дозировку '
                                            f'необходимо постепенно в течение нескольких недель. Так как в РГЛС не '
                                            f'указаны конкретные дозировку, основываясь на опыте врачей, '
                                            f'рекомендовано снижать на ¼ суточной дозы 1 раз в 1-2 недели (на 25 мг).',
                                       reply_markup=func.keyboard(3, '152'))
    elif call.data == '121':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_03_id_05,
                                       text=f'Терапевтическая доза – 100-200 мг/сут. Максимальная доза '
                                            f'250 мг/сутки (300 мг/сутки при стационарном наблюдении).',
                                       reply_markup=func.keyboard(3, '153'))
    elif call.data == '122':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_03_id_06,
                                       text=f'Начальная доза 10 мг/сутки, при необходимости повысить до '
                                            f'20 мг/сутки через 1-2 недели.',
                                       reply_markup=func.keyboard(3, '154'))
    elif call.data == '123':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_03_id_06,
                                       text=f'Постепенно снижать дозировку на ¼ суточной '
                                            f'дозы каждые 1-2 недели (на 2,5 мг).',
                                       reply_markup=func.keyboard(3, '155'))
    elif call.data == '124':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_03_id_06,
                                       text=f'Терапевтическая доза - 10-20 мг/сутки, для пожилых – '
                                            f'5-10 мг/сутки. Прием утром.',
                                       reply_markup=func.keyboard(3, '156'))
    elif call.data == '125':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_03_id_07,
                                       text=f'Начальная доза 50 мг, суточную дозу можно повышать с шагом 50 мг '
                                            f'и с интервалом как минимум одна неделя в течение нескольких недель.',
                                       reply_markup=func.keyboard(3, '157'))
    elif call.data == '126':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_03_id_07,
                                       text=f'Во избежания развития синдрома «отмены» снижать дозировку '
                                            f'необходимо постепенно в течение нескольких недель. Так как в РГЛС не '
                                            f'указаны конкретные дозировку, основываясь на опыте врачей, рекомендовано '
                                            f'снижать на ¼ суточной дозы 1 раз в 1-2 недели (на 25 мг).',
                                       reply_markup=func.keyboard(3, '158'))
    elif call.data == '127':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_03_id_07,
                                       text=f'Терапевтическая доза – 100-150 мг/сутки. Максимальная доза – 200 '
                                            f'мг/сутки. Прием 1-2 раза в день (утром и днем).',
                                       reply_markup=func.keyboard(3, '159'))
    elif call.data == '128':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_03_id_08,
                                       text=f'Начальная доза 10 мг/сутки, рекомендовано повышать дозу на 10 мг до '
                                            f'достижения желаемого терапевтического эффекта 1 раз в неделю.',
                                       reply_markup=func.keyboard(3, '160'))
    elif call.data == '129':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_03_id_08,
                                       text=f'В связи с тем, что пароксетин чаще остальных препаратов '
                                            f'группы СИОЗС вызывает симптомы «отмены», прекращать его прием '
                                            f'необходимо очень медленно. Хотя в РГЛС не указана конкретная '
                                            f'схема отмены препараты, врачи рекомендуют снижать суточную '
                                            f'дозу на ¼-1/6 каждые 4-6 недель (на 5 мг).',
                                       reply_markup=func.keyboard(3, '161'))
    elif call.data == '130':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_03_id_08,
                                       text=f'Терапевтическая доза – 20-50 мг. Максимальная доза – 60 мг/сутки. '
                                            f'Прием утром во время еды (в соответствии с гайдом Шталя – принимать на '
                                            f'ночь, но особой разницы нет).',
                                       reply_markup=func.keyboard(3, '162'))
    elif call.data == '131':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_03_id_09,
                                       text=f'Начальная доза 50 мг/сутки, повышение дозировки возможно через 4-7 дней. '
                                            f'Суточную дозу свыше 150 мг рекомендовано разделять 2-3 приема.',
                                       reply_markup=func.keyboard(3, '163'))
    elif call.data == '132':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_03_id_09,
                                       text=f'Во избежания развития синдрома «отмены» снижать дозировку '
                                            f'необходимо постепенно в течение нескольких недель. Так как в '
                                            f'РГЛС не указаны конкретные дозировку, основываясь на опыте '
                                            f'врачей, рекомендовано снижать на ¼ суточной дозы 1 раз в '
                                            f'1-2 недели (на 25 мг).',
                                       reply_markup=func.keyboard(3, '164'))
    elif call.data == '133':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_03_id_09,
                                       text=f'Терапевтическая доза – 100 мг/сутки. Максимальная доза – '
                                            f'300 мг/сутки. Прием вечером.',
                                       reply_markup=func.keyboard(3, '165'))
    elif call.data == '134':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_03_id_10,
                                       text=f'Начальная доза – 20 мг/сутки, при необходимости для '
                                            f'достижения терапевтического эффекта возможно повышение дозировки '
                                            f'постепенно до 60 мг/сутки через несколько недель.',
                                       reply_markup=func.keyboard(3, '166'))
    elif call.data == '135':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_03_id_10,
                                       text=f'Во избежания развития синдрома «отмены» снижать дозировку '
                                            f'необходимо постепенно в течение нескольких недель. Так как в РГЛС не '
                                            f'указаны конкретные дозировки, основываясь на опыте врачей, рекомендовано '
                                            f'принимать препарат по 1 капс через день в течение 2,5 месяцев, '
                                            f'затем прекратить прием.',
                                       reply_markup=func.keyboard(3, '167'))
    elif call.data == '136':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_03_id_10,
                                       text=f'Терапевтическая доза – 20 мг/сутки. Максимальная доза – '
                                            f'60 мг/сутки. Прием утром.',
                                       reply_markup=func.keyboard(3, '168'))


@bot.main_bot.callback_query_handler(func=lambda call:
                                     call.data == '139' or call.data == '140' or call.data == '141' or
                                     call.data == '142' or call.data == '143' or call.data == '144' or
                                     call.data == '145' or call.data == '146' or call.data == '147' or
                                     call.data == '148' or call.data == '149' or call.data == '150' or
                                     call.data == '151' or call.data == '152' or call.data == '153' or
                                     call.data == '154' or call.data == '155' or call.data == '156' or
                                     call.data == '157' or call.data == '158' or call.data == '159' or
                                     call.data == '160' or call.data == '161' or call.data == '162' or
                                     call.data == '163' or call.data == '164' or call.data == '165' or
                                     call.data == '166' or call.data == '167' or call.data == '168')
def start1_13(call):
    if call.data == '139' or call.data == '140' or call.data == '141':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_03_id_01,
                                       text='Показать схему повышения / отмены  препарата *Венлафаксин*?',
                                       reply_markup=func.keyboard(5, ['107', '108', '109']),
                                       parse_mode='Markdown')
    elif call.data == '142' or call.data == '143' or call.data == '144':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_03_id_02,
                                       text='Показать схему повышения / отмены  препарата *Дулоксетин*?',
                                       reply_markup=func.keyboard(5, ['110', '111', '112']),
                                       parse_mode='Markdown')
    elif call.data == '145' or call.data == '146' or call.data == '147':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_03_id_03,
                                       text='Показать схему повышения / отмены  препарата *Миртазапин*?',
                                       reply_markup=func.keyboard(5, ['113', '114', '115']),
                                       parse_mode='Markdown')
    elif call.data == '148' or call.data == '149' or call.data == '150':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_03_id_04,
                                       text='Показать схему повышения / отмены  препарата *Имипрамин*?',
                                       reply_markup=func.keyboard(5, ['116', '117', '118']),
                                       parse_mode='Markdown')
    elif call.data == '151' or call.data == '152' or call.data == '153':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_03_id_05,
                                       text='Показать схему повышения / отмены  препарата *Кломипрамин*?',
                                       reply_markup=func.keyboard(5, ['119', '120', '121']),
                                       parse_mode='Markdown')
    elif call.data == '154' or call.data == '155' or call.data == '156':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_03_id_06,
                                       text='Показать схему повышения / отмены  препарата *Эсциталопрам*?',
                                       reply_markup=func.keyboard(5, ['122', '123', '124']),
                                       parse_mode='Markdown')
    elif call.data == '157' or call.data == '158' or call.data == '159':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_03_id_07,
                                       text='Показать схему повышения / отмены  препарата *Сертралин*?',
                                       reply_markup=func.keyboard(5, ['125', '126', '127']),
                                       parse_mode='Markdown')
    elif call.data == '160' or call.data == '161' or call.data == '162':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_03_id_08,
                                       text='Показать схему повышения / отмены  препарата *Пароксетин*?',
                                       reply_markup=func.keyboard(5, ['128', '129', '130']),
                                       parse_mode='Markdown')
    elif call.data == '163' or call.data == '164' or call.data == '165':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_03_id_09,
                                       text='Показать схему повышения / отмены  препарата *Флувоксамин*?',
                                       reply_markup=func.keyboard(5, ['131', '132', '133']),
                                       parse_mode='Markdown')
    elif call.data == '166' or call.data == '167' or call.data == '168':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_03_id_10,
                                       text='Показать схему повышения / отмены  препарата *Флуоксетин*?',
                                       reply_markup=func.keyboard(5, ['134', '135', '136']),
                                       parse_mode='Markdown')


@bot.main_bot.callback_query_handler(func=lambda call: call.data == '15' or call.data == '16' or call.data == '17')
def start1_14(call):
    global last_reply_message_04_id_01, last_reply_message_04_id_02
    global last_reply_message_04_id_03, last_reply_message_04_id_04
    global last_reply_message_04_id_05, last_reply_message_04_id_06

    if call.data == '15':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_msg_id_01_02,
                                       text=f'Вам нужно более подробное лечение?',
                                       reply_markup=func.keyboard(2, ['__', '___', '5']))
    elif call.data == '16':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_msg_id_01_02,
                                       text=f'Вы можете назначить любой из данных препаратов при лечении пациента, '
                                            f'справа указаны средние терапевтические дозировки.\n\n'
                                            f'*Венлафаксин* терапевтическая доза – 150-225 мг/сутки\n'
                                            f'*Миртазапин* 15-45 мг/сутки\n'
                                            f'*Кломипрамин* 100-200 мг/сутки\n'
                                            f'*Амитриптилин* 150-200 мг/сутки\n'
                                            f'*СИОЗС* (напр., Пароксетин 20-50 мг/сутки, Флуоксетин 20 мг/сутки)\n'
                                            f'*ИМАО* (напр., Пирилиндол – 150-300 мг/сут)\n'
                                            f'*Литий* (до 800 мг/сутки)\n'
                                            f'*Трийодтиронин* (аугментация)',
                                       parse_mode='Markdown')

        last_reply_message_04_id_01 = bot.main_bot.send_message(chat_id=call.message.chat.id,
                                                                text='Показать схему повышения / отмены  препарата '
                                                                     '*Венлафаксин*?',
                                                                reply_markup=func.keyboard(5, ['172', '173', '174']),
                                                                parse_mode='Markdown').message_id

        last_reply_message_04_id_02 = bot.main_bot.send_message(chat_id=call.message.chat.id,
                                                                text='Показать схему повышения / отмены  препарата '
                                                                     '*Миртазапин*?',
                                                                reply_markup=func.keyboard(5, ['175', '176', '177']),
                                                                parse_mode='Markdown').message_id

        last_reply_message_04_id_03 = bot.main_bot.send_message(chat_id=call.message.chat.id,
                                                                text='Показать схему повышения / отмены  препарата '
                                                                     '*Амитриптилин*?',
                                                                reply_markup=func.keyboard(5, ['178', '179', '180']),
                                                                parse_mode='Markdown').message_id

        last_reply_message_04_id_04 = bot.main_bot.send_message(chat_id=call.message.chat.id,
                                                                text='Показать схему повышения / отмены  препарата '
                                                                     '*Кломипрамин*?',
                                                                reply_markup=func.keyboard(5, ['181', '182', '183']),
                                                                parse_mode='Markdown').message_id

        last_reply_message_04_id_05 = bot.main_bot.send_message(chat_id=call.message.chat.id,
                                                                text='Показать схему повышения / отмены  препарата '
                                                                     '*Пароксетин*?',
                                                                reply_markup=func.keyboard(5, ['184', '185', '186']),
                                                                parse_mode='Markdown').message_id

        last_reply_message_04_id_06 = bot.main_bot.send_message(chat_id=call.message.chat.id,
                                                                text='Показать схему повышения / отмены  препарата '
                                                                     '*Флуоксетин*?',
                                                                reply_markup=func.keyboard(5, ['187', '188', '189']),
                                                                parse_mode='Markdown').message_id
        bot.main_bot.send_message(chat_id=call.message.chat.id,
                                  text=func.ending_words[4])
    elif call.data == '17':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_msg_id_01_02,
                                       text='Хотите получить рекомендации по лечению?',
                                       reply_markup=func.keyboard(2, '564'))


@bot.main_bot.callback_query_handler(func=lambda call:
                                     call.data == '172' or call.data == '173' or call.data == '174' or
                                     call.data == '175' or call.data == '176' or call.data == '177' or
                                     call.data == '178' or call.data == '179' or call.data == '180' or
                                     call.data == '181' or call.data == '182' or call.data == '183' or
                                     call.data == '184' or call.data == '185' or call.data == '186' or
                                     call.data == '187' or call.data == '188' or call.data == '189')
def start1_15(call):
    global last_reply_message_04_id_01, last_reply_message_04_id_02
    global last_reply_message_04_id_03, last_reply_message_04_id_04
    global last_reply_message_04_id_05, last_reply_message_04_id_06

    if call.data == '172':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_04_id_01,
                                       text=f'Начальная доза 37,5 мг 2 раза в день (в соответствии с гайдом Шталя – 37,'
                                            f'5 мг 1 раз в день), постепенное повышение суточной дозы возможно на '
                                            f'75 мг каждые 4-7 дней (безопаснее повышать дозу раз в неделю).',
                                       reply_markup=func.keyboard(3, '192'))
    elif call.data == '173':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_04_id_01,
                                       text=f'Во избежания развития синдрома «отмены» снижать дозировку '
                                            f'необходимо постепенно в течение нескольких недель. Так как в РГЛС не '
                                            f'указаны конкретные дозировку, основываясь на опыте врачей, рекомендовано '
                                            f'снижать на ¼ суточной дозы 1 раз в 1-2 недели (на 37,5 мг).',
                                       reply_markup=func.keyboard(3, '193'))
    elif call.data == '174':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_04_id_01,
                                       text=f'Терапевтическая доза – 150-225 мг/сутки. '
                                            f'Максимальная доза – 375 мг/сутки.',
                                       reply_markup=func.keyboard(3, '194'))
    elif call.data == '175':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_04_id_02,
                                       text=f'Начальная доза 15 мг/сутки, повышать до наступления желаемого '
                                            f'терапевтического эффекта через 1-2 недели.',
                                       reply_markup=func.keyboard(3, '195'))
    elif call.data == '176':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_04_id_02,
                                       text=f'Во избежания развития синдрома «отмены» снижать дозировку '
                                            f'необходимо постепенно в течение нескольких недель. Так как в РГЛС не '
                                            f'указаны конкретные дозировку, основываясь на опыте врачей, рекомендовано '
                                            f'снижать на ¼ суточной дозы 1 раз в 1-2 недели.',
                                       reply_markup=func.keyboard(3, '196'))
    elif call.data == '177':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_04_id_02,
                                       text=f'Терапевтическая доза – 15-45 мг/сутки. Максимальная доза '
                                            f'45 мг/сутки. Принимать на ночь.',
                                       reply_markup=func.keyboard(3, '197'))
    elif call.data == '178':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_04_id_03,
                                       text=f'Начальная доза 50-75 мг/сутки, разделив на 2-3 приема или '
                                            f'в один прием вечером, если пролонгированная форма. Повышение дозы на '
                                            f'25 мг каждые несколько дней до наступления терапевтического эффекта '
                                            f'(в соответствии с гайдом Шталя повышение '
                                            f'дозы необходимо делать каждые две недели).',
                                       reply_markup=func.keyboard(3, '198'))
    elif call.data == '179':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_04_id_03,
                                       text=f'Во избежания развития синдрома «отмены» снижать дозировку '
                                            f'необходимо постепенно в течение нескольких недель. Так как в РГЛС не '
                                            f'указаны конкретные дозировку, основываясь на опыте врачей, рекомендовано '
                                            f'снижать на ¼ суточной дозы 1 раз в 1-2 недели (на 25 мг).',
                                       reply_markup=func.keyboard(3, '199'))
    elif call.data == '180':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_04_id_03,
                                       text=f'Терапевтическая доза – 100-200 мг/сут. Максимальная доза 250 мг/сутки '
                                            f'(300 мг/сутки при стационарном наблюдении).',
                                       reply_markup=func.keyboard(3, '200'))
    elif call.data == '181':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_04_id_04,
                                       text=f'Начать с 25-50 мг/сутки, разделив на два приема, или однократный '
                                            f'прием за 2 часа до сна. Повышать на 25-50 мг каждые 3-7 дней до '
                                            f'терапевтического эффекта. '
                                            f'Максимальная часть дозы принимается на ночь (например, '
                                            f'утром 50 мг, на ночь 100 мг).',
                                       reply_markup=func.keyboard(3, '201'))
    elif call.data == '182':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_04_id_04,
                                       text=f'Во избежания развития синдрома «отмены» снижать суточную '
                                            f'дозировку необходимо постепенно в течение нескольких недель. '
                                            f'Так как в РГЛС не указаны конкретные дозировки, основываясь на '
                                            f'опыте врачей, рекомендовано снижать на ¼ суточной дозы 1 раз в 1-2 '
                                            f'недели (на 25 мг). При появлении синдрома «отмены» вернуть '
                                            f'прошлую дозировку и снижать дозу еще медленнее.',
                                       reply_markup=func.keyboard(3, '202'))
    elif call.data == '183':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_04_id_04,
                                       text=f'Терапевтическая доза – 150-200 мг/сутки. Максимальная доза 300 мг/сутки.',
                                       reply_markup=func.keyboard(3, '203'))
    elif call.data == '184':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_04_id_05,
                                       text=f'Начальная доза 10 мг/сутки, рекомендовано повышать дозу на 10 мг '
                                            f'до достижения желаемого терапевтического эффекта 1 раз в неделю.',
                                       reply_markup=func.keyboard(3, '204'))
    elif call.data == '185':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_04_id_05,
                                       text=f'В связи с тем, что пароксетин чаще остальных препаратов группы '
                                            f'СИОЗС вызывает симптомы «отмены», прекращать его прием необходимо '
                                            f'очень медленно. Хотя в РГЛС не указана конкретная схема отмены '
                                            f'препараты, врачи рекомендуют снижать суточную'
                                            f'дозу на ¼-1/6 каждые 4-6 недель (на 5 мг).',
                                       reply_markup=func.keyboard(3, '205'))
    elif call.data == '186':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_04_id_05,
                                       text=f'Терапевтическая доза – 20-50 мг. Максимальная доза – '
                                            f'60 мг/сутки. Прием утром во время еды (в соответствии с гайдом '
                                            f'Шталя – принимать на ночь, но особой разницы нет).',
                                       reply_markup=func.keyboard(3, '206'))
    elif call.data == '187':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_04_id_06,
                                       text=f'Начальная доза – 20 мг/сутки, при необходимости для '
                                            f'достижения терапевтического эффекта возможно повышение дозировки '
                                            f'постепенно до 60 мг/сутки через несколько недель.',
                                       reply_markup=func.keyboard(3, '207'))
    elif call.data == '188':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_04_id_06,
                                       text=f'Во избежания развития синдрома «отмены» снижать дозировку '
                                            f'необходимо постепенно в течение нескольких недель. Так как в РГЛС не '
                                            f'указаны конкретные дозировки, основываясь на опыте врачей, рекомендовано '
                                            f'принимать препарат по 1 капс через день в течение 2,5 месяцев, '
                                            f'затем прекратить прием.',
                                       reply_markup=func.keyboard(3, '208'))
    elif call.data == '189':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_04_id_06,
                                       text=f'Терапевтическая доза – 20 мг/сутки. '
                                            f'Максимальная доза – 60 мг/сутки. Прием утром.',
                                       reply_markup=func.keyboard(3, '209'))


@bot.main_bot.callback_query_handler(func=lambda call:
                                     call.data == '192' or call.data == '193' or call.data == '194' or
                                     call.data == '195' or call.data == '196' or call.data == '197' or
                                     call.data == '198' or call.data == '199' or call.data == '200' or
                                     call.data == '201' or call.data == '202' or call.data == '203' or
                                     call.data == '204' or call.data == '205' or call.data == '206' or
                                     call.data == '207' or call.data == '208' or call.data == '209')
def start1_16(call):
    if call.data == '192' or call.data == '193' or call.data == '194':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_04_id_01,
                                       text='Показать схему повышения / отмены  препарата *Венлафаксин*?',
                                       reply_markup=func.keyboard(5, ['172', '173', '174']),
                                       parse_mode='Markdown')
    elif call.data == '195' or call.data == '196' or call.data == '197':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_04_id_02,
                                       text='Показать схему повышения / отмены  препарата *Миртазапин*?',
                                       reply_markup=func.keyboard(5, ['175', '176', '177']),
                                       parse_mode='Markdown')
    elif call.data == '198' or call.data == '199' or call.data == '200':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_04_id_03,
                                       text='Показать схему повышения / отмены  препарата *Амитриптилин*?',
                                       reply_markup=func.keyboard(5, ['178', '179', '180']),
                                       parse_mode='Markdown')
    elif call.data == '201' or call.data == '202' or call.data == '203':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_04_id_04,
                                       text='Показать схему повышения / отмены  препарата *Кломипрамин*?',
                                       reply_markup=func.keyboard(5, ['181', '182', '183']),
                                       parse_mode='Markdown')
    elif call.data == '204' or call.data == '205' or call.data == '206':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_04_id_05,
                                       text='Показать схему повышения / отмены  препарата *Пароксетин*?',
                                       reply_markup=func.keyboard(5, ['184', '185', '186']),
                                       parse_mode='Markdown')
    elif call.data == '207' or call.data == '208' or call.data == '209':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message_04_id_06,
                                       text='Показать схему повышения / отмены  препарата *Флуоксетин*?',
                                       reply_markup=func.keyboard(5, ['187', '188', '189']),
                                       parse_mode='Markdown')


@bot.main_bot.callback_query_handler(func=lambda call: call.data == '__' or call.data == '___')
def start1_17(call):
    if call.data == '__':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_msg_id_01_02,
                                       text=f'{func.ending_words[4]}')  # 更多命令
    else:
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_msg_id_01_02,
                                       text=f'{func.ending_words[2]}\n'  # 感谢完成问卷
                                            f'{func.ending_words[3]}')  # 更多命令


if __name__ == "__main__":
    bot.main_bot.polling()
