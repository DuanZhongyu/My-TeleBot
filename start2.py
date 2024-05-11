# Created 2024.04.27
# by 彧同学

# 功能 2 —— 临床治疗策略
# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
import bot
import func

last_message_id_04 = None

last_reply_message02_01_id_01 = None
last_reply_message02_01_id_02 = None
last_reply_message02_01_id_03 = None
last_reply_message02_01_id_04 = None


def start2_01(chat_id):
    global last_message_id_04

    last_message_id_04 = bot.main_bot.send_message(chat_id=chat_id,
                                                   text=f'Прежде всего убедитесь, что:\n'
                                                        f'*1. У пациента подтвержден диагноз '
                                                        f'депрессивного расстройства.*\n'
                                                        f'*2. В течение 3-4 недель пациент '
                                                        f'получал СИОЗС/СИОЗСН/атипичные* '
                                                        f'*антидепрессанты/ТЦА. Пациенту была '
                                                        f'назначена психотерапия.*\n\n'
                                                        f'Ответьте на вопрос *(1/17)*:\n\n'
                                                        f'{func.start2_questions[0]}',
                                                   reply_markup=func.keyboard(1, ['_1', '_2']),
                                                   parse_mode='Markdown').message_id


@bot.main_bot.callback_query_handler(func=lambda call: call.data == '_1' or call.data == '_2')
def start2_02(call):
    if call.data == '_1':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_message_id_04,
                                       text=f'Ответьте на вопрос *(2/17)*:\n\n'
                                            f'{func.start2_questions[1]}',
                                       reply_markup=func.keyboard(2, ['_3', '_4', '_5']),
                                       parse_mode='Markdown')
    else:
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_message_id_04,
                                       text=f'Назначить АД с другим механизмом действия (1А).\n\n'
                                            f'Ответьте на вопрос *(3/17)*:\n\n'
                                            f'{func.start2_questions[2]}',
                                       reply_markup=func.keyboard(1, ['_6', '_7']),
                                       parse_mode='Markdown')


@bot.main_bot.callback_query_handler(func=lambda call: call.data == '_3' or call.data == '_4')
def start2_03(call):
    global last_reply_message02_01_id_01

    if call.data == '_3':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_message_id_04,
                                       text=f'Продолжить терапию до достижения ремиссии.')
        last_reply_message02_01_id_01 = bot.main_bot.send_message(chat_id=call.message.chat.id,
                                                                  text=f'{func.ending_words[0]}',
                                                                  reply_markup=func.keyboard(2, ['_8', '_9',
                                                                                                 '_10'])).message_id
    else:
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_message_id_04,
                                       text=f'Повысить дозу до максимальной и продолжить '
                                            f'терапию ещё 3-4 недели (1А)\n\n'
                                            f'Ответьте на вопрос *(3/17)*:\n\n'
                                            f'{func.start2_questions[2]}',
                                       reply_markup=func.keyboard(1, ['_6', '_7']),
                                       parse_mode='Markdown')


@bot.main_bot.callback_query_handler(func=lambda call: call.data == '_6' or call.data == '_7')
def start2_04(call):
    global last_reply_message02_01_id_02

    if call.data == '_6':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_message_id_04,
                                       text=f'Продолжить терапию до достижения ремиссии.')
        last_reply_message02_01_id_02 = bot.main_bot.send_message(chat_id=call.message.chat.id,
                                                                  text=f'{func.ending_words[0]}',
                                                                  reply_markup=func.keyboard(2, ['__11', '___11',
                                                                                                 '_11'])).message_id
    else:
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_message_id_04,
                                       text=f'Уточнить диагноз, диагностировать соматическую патологию, коморбндные '
                                            f'психические расстройства, органическое поражение ЦНС, неразрешенные '
                                            f'стрессовые факторы, выявить некомплаентность.\n\n'
                                            f'Ответьте на вопрос *(4/17)*:\n\n'
                                            f'{func.start2_questions[3]}',
                                       reply_markup=func.keyboard(2, ['_12', '_13', '_14']),
                                       parse_mode='Markdown')


@bot.main_bot.callback_query_handler(func=lambda call: call.data == '_12' or call.data == '_13' or call.data == '_15')
def start2_05(call):
    if call.data == '_12':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_message_id_04,
                                       text=f'Принять соответствуюцие меры.\n\n'
                                            f'Уточнить диагноз, диагностировать соматическую патологию, коморбндные '
                                            f'психические расстройства, органическое поражение ЦНС, неразрешенные '
                                            f'стрессовые факторы, выявить некомплаентность.\n\n'
                                            f'Ответьте на вопрос *(4/17)*:\n\n'
                                            f'{func.start2_questions[3]}',
                                       reply_markup=func.keyboard(2, ['_15', '_13', '_14']),
                                       parse_mode='Markdown')
    elif call.data == '_15':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_message_id_04,
                                       text=f'Принять соответствуюцие меры.\n\n'
                                            f'Уточнить диагноз, диагностировать соматическую патологию, коморбндные '
                                            f'психические расстройства, органическое поражение ЦНС, неразрешенные '
                                            f'стрессовые факторы, выявить некомплаентность.\n\n'
                                            f'Ответьте на вопрос *(4/17)*:\n\n'
                                            f'*Ответьте еще раз*, обнаружена ли какая-либо причина?',
                                       reply_markup=func.keyboard(2, ['_12', '_13', '_14']),
                                       parse_mode='Markdown')
    else:
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_message_id_04,
                                       text=f'Регистрировать относитентность и перейти к любой из опций III этапа.\n\n'
                                            f'Ответьте на вопрос *(5/17)*:\n\n'
                                            f'{func.start2_questions[4]}',
                                       reply_markup=func.keyboard(2, ['_16', '_17', '_18']),
                                       parse_mode='Markdown')


@bot.main_bot.callback_query_handler(func=lambda call: call.data == '_16' or call.data == '_17')
def start2_06(call):
    if call.data == '_16':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_message_id_04,
                                       text=f'Ответьте на вопрос *(8/17)*:\n\n'
                                            f'{func.start2_questions[7]}',
                                       reply_markup=func.keyboard(1, ['_19', '_20']),
                                       parse_mode='Markdown')
    else:
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_message_id_04,
                                       text=f'Ответьте на вопрос *(6/17)*:\n\n'
                                            f'{func.start2_questions[5]}',
                                       reply_markup=func.keyboard(2, ['_21', '_22', '_23']),
                                       parse_mode='Markdown')


@bot.main_bot.callback_query_handler(func=lambda call: call.data == '_21' or call.data == '_22')
def start2_07(call):
    if call.data == '_21':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_message_id_04,
                                       text=f'Ответьте на вопрос *(8/17)*:\n\n'
                                            f'{func.start2_questions[7]}',
                                       reply_markup=func.keyboard(1, ['_19', '_20']),
                                       parse_mode='Markdown')
    else:
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_message_id_04,
                                       text=f'Ответьте на вопрос *(7/17)*:\n\n'
                                            f'{func.start2_questions[6]}',
                                       reply_markup=func.keyboard(2, ['_24', '_25', '_26']),
                                       parse_mode='Markdown')


@bot.main_bot.callback_query_handler(func=lambda call: call.data == '_24' or call.data == '_25')
def start2_08(call):
    if call.data == '_24':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_message_id_04,
                                       text=f'Пожалуйста, ответьте на вопрос *(8/17)*:\n\n'
                                            f'{func.start2_questions[7]}',
                                       reply_markup=func.keyboard(1, ['_19', '_20']),
                                       parse_mode='Markdown')
    else:
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_message_id_04,
                                       text=f'Регистрировать относитентность и перейти к любой из опций III этапа.\n\n'
                                            f'Ответьте на вопрос *(5/17)*:\n\n'
                                            f'{func.start2_questions[4]}',
                                       reply_markup=func.keyboard(2, ['_16', '_17', '_18']),
                                       parse_mode='Markdown')


@bot.main_bot.callback_query_handler(func=lambda call: call.data == '_19' or call.data == '_20')
def start2_09(call):
    global last_reply_message02_01_id_03

    if call.data == '_19':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_message_id_04,
                                       text=f'Продолжить терапию до достижения ремиссии.')
        last_reply_message02_01_id_03 = bot.main_bot.send_message(chat_id=call.message.chat.id,
                                                                  text=f'{func.ending_words[0]}',
                                                                  reply_markup=func.keyboard(2, ['_27', '_28',
                                                                                                 '_29'])).message_id
    else:
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_message_id_04,
                                       text=f'Верифицировать диагноз, исключить сопутствующую '
                                            f'патологию и лекарственные взамодействия.\n\n'
                                            f'Ответьте на вопрос *(9/17)*:\n\n'
                                            f'{func.start2_questions[8]}',
                                       reply_markup=func.keyboard(2, ['_30', '_31', '_32']),
                                       parse_mode='Markdown')


@bot.main_bot.callback_query_handler(func=lambda call: call.data == '_30' or call.data == '_31' or call.data == '_33')
def start2_10(call):
    if call.data == '_30':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_message_id_04,
                                       text=f'Принять соответствующие меры.\n\n'
                                            f'Верифицировать диагноз, исключить сопутствующую '
                                            f'патологию и лекарственные взамодействия.\n\n'
                                            f'Ответьте на вопрос *(9/17)*:\n\n'
                                            f'{func.start2_questions[8]}',
                                       reply_markup=func.keyboard(1, ['_33', '_31', '_32']),
                                       parse_mode='Markdown')
    elif call.data == '_33':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_message_id_04,
                                       text=f'Принять соответствующие меры.\n\n'
                                            f'Верифицировать диагноз, исключить сопутствующую '
                                            f'патологию и лекарственные взамодействия.\n\n'
                                            f'Ответьте на вопрос *(9/17)*:\n\n'
                                            f'*Ответьте еще раз*, обнаружена ли какая-либо причина?',
                                       reply_markup=func.keyboard(2, ['_30', '_31', '_32']),
                                       parse_mode='Markdown')
    else:
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_message_id_04,
                                       text=f'Перейти к любой из опций IV этапа.\n\n'
                                            f'Ответьте на вопрос *(10/17)*:\n\n'
                                            f'{func.start2_questions[9]}',
                                       reply_markup=func.keyboard(2, ['_34', '_35', '_36']),
                                       parse_mode='Markdown')


@bot.main_bot.callback_query_handler(func=lambda call: call.data == '_34' or call.data == '_35')
def start2_11(call):
    if call.data == '_34':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_message_id_04,
                                       text=f'Ответьте на вопрос *(17/17)*:\n\n'
                                            f'{func.start2_questions[16]}',
                                       reply_markup=func.keyboard(1, ['_37', '_38']),
                                       parse_mode='Markdown')
    else:
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_message_id_04,
                                       text=f'Ответьте на вопрос *(11/17)*:\n\n'
                                            f'{func.start2_questions[10]}',
                                       reply_markup=func.keyboard(2, ['_39', '_40', '_41']),
                                       parse_mode='Markdown')


@bot.main_bot.callback_query_handler(func=lambda call: call.data == '_39' or call.data == '_40')
def start2_12(call):
    if call.data == '_39':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_message_id_04,
                                       text=f'Оветьте на вопрос *(17/17)*:\n\n'
                                            f'{func.start2_questions[16]}',
                                       reply_markup=func.keyboard(1, ['_37', '_38']),
                                       parse_mode='Markdown')
    else:
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_message_id_04,
                                       text=f'Ответьте на вопрос *(12/17)*:\n\n'
                                            f'{func.start2_questions[11]}',
                                       reply_markup=func.keyboard(2, ['_42', '_43', '_44']),
                                       parse_mode='Markdown')


@bot.main_bot.callback_query_handler(func=lambda call: call.data == '_42' or call.data == '_43')
def start2_13(call):
    if call.data == '_42':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_message_id_04,
                                       text=f'Оветьте на вопрос *(17/17)*:\n\n'
                                            f'{func.start2_questions[16]}',
                                       reply_markup=func.keyboard(1, ['_37', '_38']),
                                       parse_mode='Markdown')
    else:
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_message_id_04,
                                       text=f'Ответьте на вопрос *(13/17)*:\n\n'
                                            f'{func.start2_questions[12]}',
                                       reply_markup=func.keyboard(2, ['_45', '_46', '_47']),
                                       parse_mode='Markdown')


@bot.main_bot.callback_query_handler(func=lambda call: call.data == '_45' or call.data == '_46')
def start2_14(call):
    if call.data == '_45':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_message_id_04,
                                       text=f'Оветьте на вопрос *(17/17)*:\n\n'
                                            f'{func.start2_questions[16]}',
                                       reply_markup=func.keyboard(1, ['_37', '_38']),
                                       parse_mode='Markdown')
    else:
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_message_id_04,
                                       text=f'Ответьте на вопрос *(14/17)*:\n\n'
                                            f'{func.start2_questions[13]}',
                                       reply_markup=func.keyboard(2, ['_48', '_49', '_50']),
                                       parse_mode='Markdown')


@bot.main_bot.callback_query_handler(func=lambda call: call.data == '_48' or call.data == '_49')
def start2_15(call):
    if call.data == '_48':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_message_id_04,
                                       text=f'Оветьте на вопрос *(17/17)*:\n\n'
                                            f'{func.start2_questions[16]}',
                                       reply_markup=func.keyboard(1, ['_37', '_38']),
                                       parse_mode='Markdown')
    else:
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_message_id_04,
                                       text=f'Пожалуйста, ответьте на вопрос *(15/17)*:\n\n'
                                            f'{func.start2_questions[14]}',
                                       reply_markup=func.keyboard(2, ['_51', '_52', '_53']),
                                       parse_mode='Markdown')


@bot.main_bot.callback_query_handler(func=lambda call: call.data == '_51' or call.data == '_52')
def start2_16(call):
    if call.data == '_51':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_message_id_04,
                                       text=f'Оветьте на вопрос *(17/17)*:\n\n'
                                            f'{func.start2_questions[16]}',
                                       reply_markup=func.keyboard(1, ['_37', '_38']),
                                       parse_mode='Markdown')
    else:
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_message_id_04,
                                       text=f'Ответьте на вопрос *(16/17)*:\n\n'
                                            f'{func.start2_questions[15]}',
                                       reply_markup=func.keyboard(2, ['_54', '_55', '_56']),
                                       parse_mode='Markdown')


@bot.main_bot.callback_query_handler(func=lambda call: call.data == '_54' or call.data == '_55')
def start2_17(call):
    if call.data == '_54':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_message_id_04,
                                       text=f'Оветьте на вопрос *(17/17)*:\n\n'
                                            f'{func.start2_questions[16]}',
                                       reply_markup=func.keyboard(1, ['_37', '_38']),
                                       parse_mode='Markdown')
    else:
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_message_id_04,
                                       text=f'Перейти к любой из опций IV этапа.\n\n'
                                            f'Пожалуйста, ответьте на вопрос *(10/17)*:\n\n'
                                            f'{func.start2_questions[9]}',
                                       reply_markup=func.keyboard(2, ['_34', '_35', '_36']),
                                       parse_mode='Markdown')


@bot.main_bot.callback_query_handler(func=lambda call: call.data == '_37' or call.data == '_38')
def start2_18(call):
    global last_reply_message02_01_id_04
    if call.data == '_37':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_message_id_04,
                                       text=f'Продолжить терапию до достижения ремиссии.')
        last_reply_message02_01_id_04 = bot.main_bot.send_message(chat_id=call.message.chat.id,
                                                                  text=f'{func.ending_words[0]}',
                                                                  reply_markup=func.keyboard(2, ['_57', '_58',
                                                                                                 '_59'])).message_id
    else:
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_message_id_04,
                                       text=f'Регистрировать абсолютную резистентность.\n\n'
                                            f'Перейти к любой из опций IV этапа.\n\n'
                                            f'Пожалуйста, ответьте на вопрос *(10/17)*:\n\n'
                                            f'{func.start2_questions[9]}',
                                       reply_markup=func.keyboard(2, ['_34', '_35', '_36']),
                                       parse_mode='Markdown')


@bot.main_bot.callback_query_handler(func=lambda call:
                                     call.data == '_5' or call.data == '_8' or call.data == '_9' or
                                     call.data == '_10' or call.data == '_11' or call.data == '_14' or
                                     call.data == '_18' or call.data == '_23' or call.data == '_26' or
                                     call.data == '__11' or call.data == '___11' or call.data == '_27' or
                                     call.data == '_28' or call.data == '_29' or call.data == '_32' or
                                     call.data == '_36' or call.data == '_41' or call.data == '_44' or
                                     call.data == '_47' or call.data == '_50' or call.data == '_53' or
                                     call.data == '_56' or call.data == '_57' or call.data == '_58' or
                                     call.data == '_59')
def start2_19(call):
    if call.data == '_5':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_message_id_04,
                                       text=f'Ответьте на вопрос *(1/17)*:\n\n'
                                            f'{func.start2_questions[0]}',
                                       reply_markup=func.keyboard(1, ['_1', '_2']),
                                       parse_mode='Markdown')
    elif call.data == '_8':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message02_01_id_01,
                                       text=f'{func.ending_words[1]}\n'
                                            f'{func.ending_words[3]}')
    elif call.data == '_9':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message02_01_id_01,
                                       text=f'{func.ending_words[4]}')
    elif call.data == '_10':
        bot.main_bot.delete_message(chat_id=call.message.chat.id,
                                    message_id=last_reply_message02_01_id_01)
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_message_id_04,
                                       text=f'Ответьте на вопрос *(2/17)*:\n\n'
                                            f'{func.start2_questions[1]}',
                                       reply_markup=func.keyboard(2, ['_3', '_4', '_5']),
                                       parse_mode='Markdown')
    elif call.data == '_11':
        bot.main_bot.delete_message(chat_id=call.message.chat.id,
                                    message_id=last_reply_message02_01_id_02)
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_message_id_04,
                                       text=f'Ответьте на вопрос *(3/17)*:\n\n'
                                            f'{func.start2_questions[2]}',
                                       reply_markup=func.keyboard(1, ['_6', '_7']),
                                       parse_mode='Markdown')
    elif call.data == '__11':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message02_01_id_02,
                                       text=f'{func.ending_words[1]}\n'
                                            f'{func.ending_words[3]}')
    elif call.data == '___11':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message02_01_id_02,
                                       text=f'{func.ending_words[4]}')
    elif call.data == '_14':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_message_id_04,
                                       text=f'Ответьте на вопрос *(3/17)*:\n\n'
                                            f'{func.start2_questions[2]}',
                                       reply_markup=func.keyboard(1, ['_6', '_7']),
                                       parse_mode='Markdown')
    elif call.data == '_18':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_message_id_04,
                                       text=f'Ответьте на вопрос *(4/17)*:\n\n'
                                            f'{func.start2_questions[3]}',
                                       reply_markup=func.keyboard(2, ['_12', '_13', '_14']),
                                       parse_mode='Markdown')
    elif call.data == '_23':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_message_id_04,
                                       text=f'Ответьте на вопрос *(5/17)*:\n\n'
                                            f'{func.start2_questions[4]}',
                                       reply_markup=func.keyboard(2, ['_16', '_17', '_18']),
                                       parse_mode='Markdown')
    elif call.data == '_26':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_message_id_04,
                                       text=f'Ответьте на вопрос *(6/17)*:\n\n'
                                            f'{func.start2_questions[5]}',
                                       reply_markup=func.keyboard(2, ['_21', '_22', '_23']),
                                       parse_mode='Markdown')
    elif call.data == '_27':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message02_01_id_03,
                                       text=f'{func.ending_words[4]}')
    elif call.data == '_28':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_message_id_04,
                                       text=f'Ответьте на вопрос *(6/17)*:\n\n'
                                            f'{func.start2_questions[5]}',
                                       reply_markup=func.keyboard(2, ['_21', '_22', '_23']),
                                       parse_mode='Markdown')
    elif call.data == '_29':
        bot.main_bot.delete_message(chat_id=call.message.chat.id,
                                    message_id=last_reply_message02_01_id_03)
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_message_id_04,
                                       text=f'Ответьте на вопрос *(8/17)*:\n\n'
                                            f'{func.start2_questions[7]}',
                                       reply_markup=func.keyboard(1, ['_19', '_20']),
                                       parse_mode='Markdown')
    elif call.data == '_32':
        # bot.main_bot.delete_message(chat_id=call.message.chat.id,
        #                             message_id=last_reply_message02_01_id_03)
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_message_id_04,
                                       text=f'Ответьте на вопрос *(8/17)*:\n\n'
                                            f'{func.start2_questions[7]}',
                                       reply_markup=func.keyboard(1, ['_19', '_20']),
                                       parse_mode='Markdown')
    elif call.data == '_36':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_message_id_04,
                                       text=f'Ответьте на вопрос *(9/17)*:\n\n'
                                            f'{func.start2_questions[8]}',
                                       reply_markup=func.keyboard(2, ['_30', '_31', '_32']),
                                       parse_mode='Markdown')
    elif call.data == '_41':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_message_id_04,
                                       text=f'Ответьте на вопрос *(10/17)*:\n\n'
                                            f'{func.start2_questions[9]}',
                                       reply_markup=func.keyboard(2, ['_34', '_35', '_36']),
                                       parse_mode='Markdown')
    elif call.data == '_44':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_message_id_04,
                                       text=f'Ответьте на вопрос *(11/17)*:\n\n'
                                            f'{func.start2_questions[10]}',
                                       reply_markup=func.keyboard(2, ['_39', '_40', '_41']),
                                       parse_mode='Markdown')
    elif call.data == '_47':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_message_id_04,
                                       text=f'Ответьте на вопрос *(12/17)*:\n\n'
                                            f'{func.start2_questions[11]}',
                                       reply_markup=func.keyboard(2, ['_42', '_43', '_44']),
                                       parse_mode='Markdown')
    elif call.data == '_50':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_message_id_04,
                                       text=f'Ответьте на вопрос *(13/17)*:\n\n'
                                            f'{func.start2_questions[12]}',
                                       reply_markup=func.keyboard(2, ['_45', '_46', '_47']),
                                       parse_mode='Markdown')
    elif call.data == '_53':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_message_id_04,
                                       text=f'Ответьте на вопрос *(14/17)*:\n\n'
                                            f'{func.start2_questions[13]}',
                                       reply_markup=func.keyboard(2, ['_48', '_49', '_50']),
                                       parse_mode='Markdown')
    elif call.data == '_56':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_message_id_04,
                                       text=f'Ответьте на вопрос *(15/17)*:\n\n'
                                            f'{func.start2_questions[14]}',
                                       reply_markup=func.keyboard(2, ['_51', '_52', '_53']),
                                       parse_mode='Markdown')
    elif call.data == '_57':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message02_01_id_04,
                                       text=f'{func.ending_words[1]}\n'
                                            f'{func.ending_words[3]}')
    elif call.data == '_58':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_reply_message02_01_id_04,
                                       text=f'{func.ending_words[4]}')
    elif call.data == '_59':
        bot.main_bot.delete_message(chat_id=call.message.chat.id,
                                    message_id=last_reply_message02_01_id_04)
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_message_id_04,
                                       text=f'Ответьте на вопрос *(17/17)*:\n\n'
                                            f'{func.start2_questions[16]}',
                                       reply_markup=func.keyboard(1, ['_37', '_38']),
                                       parse_mode='Markdown')


if __name__ == "__main__":
    bot.main_bot.polling()
