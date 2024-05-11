# Created 2024.04.29
# by 段仲彧

# 功能 4 —— 禁忌症
# ——————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
import bot
import func

last_message_id_06 = None
last_message_id_07 = None
last_message_id_08 = None


def start4_01(chat_id):
    global last_message_id_06

    last_message_id_06 = bot.main_bot.send_message(chat_id=chat_id,
                                                   text='Хотите посмотреть противопоказания препаратов в '
                                                        'соответствии с характеристиками пациента?',
                                                   reply_markup=func.keyboard(1, ['1_', '2_'])).message_id


@bot.main_bot.callback_query_handler(func=lambda call: call.data == '1_' or call.data == '2_')
def start4_02(call):
    if call.data == '1_':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_message_id_06,
                                       text='Предлагаем на выбор восемь видов противопоказаний:\n\n'
                                            '1. Посмотреть противопоказания *по возрасту*.\n'
                                            '2. Посмотреть противопоказания '
                                            '*по заболеваниям пищеварительной системы*.\n'
                                            '3. Посмотреть противопоказания *по заболеваниям мочеполовой системы*.\n'
                                            '4. Посмотреть противопоказания *по сердечно-сосудистой системе*.\n'
                                            '5. Посмотреть противопоказания *по беременности и периоду лактации*.\n'
                                            '6. Посмотреть противопоказания *по нервной системе*.\n'
                                            '7. Посмотреть противопоказания *по эндокринной системе*.\n'
                                            '8. Посмотреть противопоказания *по другим видам*.\n\n'
                                            'Пожалуйста, выберите вид противопоказания, который Вы хотите посмотреть:',
                                       reply_markup=func.keyboard(8, [str(i) + '_' for i in range(3, 12)]),
                                       parse_mode='Markdown')
    else:
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_message_id_06,
                                       text=f'{func.ending_words[1]}\n'
                                            f'{func.ending_words[3]}\n\n'
                                            f'{func.ending_words[4]}')


@bot.main_bot.callback_query_handler(func=lambda call: call.data == '3_' or
                                     call.data == '4_' or call.data == '5_' or call.data == '6_' or call.data == '7_' or
                                     call.data == '8_' or call.data == '9_' or call.data == '10_' or call.data == '11_')
def start4_03(call):
    if call.data == '3_':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_message_id_06,
                                       text='Возраст пациента?',
                                       reply_markup=func.keyboard(9, ['12_', '13_', '14_', '15_', '16_']))
    elif call.data == '4_':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_message_id_06,
                                       text='В этой части мы предлагаем информацию о двух противопоказаниях:\n'
                                            '1. Посмотреть противопоказания *при печеночной недостаточности*.\n'
                                            '2. Просмотреть противопоказания *при циррозе печени*.\n\n'
                                            'Пожалуйста, выберите вид противопоказания, который Вы хотите посмотреть.',
                                       reply_markup=func.keyboard(10, ['17_', '18_', '19_']),
                                       parse_mode='Markdown')
    elif call.data == '5_':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_message_id_06,
                                       text='В этой части мы предлагаем шесть противопоказаний:\n'
                                            '1. Посмотреть противопоказания *при почечной недостаточности*.\n'
                                            '2. Посмотреть противопоказания *при дисфункции гиперплазии предстательной '
                                            'железы*.\n'
                                            '3. Посмотреть противопоказания *при атонии мочевого пузыря*.\n'
                                            '4. Посмотреть противопоказания *при обструкции мочевыводящих путей*.\n'
                                            '5. Посмотреть противопоказания *при задержке мочи*.\n'
                                            '6. Посмотреть противопоказания *при наличии приапизма в анамнезе*.\n\n'
                                            'Пожалуйста, выберите вид противопоказания, который Вы хотите посмотреть.',
                                       reply_markup=func.keyboard(11, [str(i) + '_' for i in range(20, 27)]),
                                       parse_mode='Markdown')
    elif call.data == '6_':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_message_id_06,
                                       text='В этой части мы предлагаем информацию о пяти противопоказаниях:\n'
                                            '1. Посмотреть противопоказания *при остром и раннем* '
                                            '*восстановлении в период инфаркта миокарда*.\n'
                                            '2. Посмотреть противопоказания *при неконтролируемой АГ*.\n'
                                            '3. Посмотреть противопоказания *при ишемической болезни сердца*.\n'
                                            '4. Посмотреть противопоказания '
                                            '*при хронической сердечной недостаточности*.\n'
                                            '5. Посмотреть противопоказания *при нарушениях проводимости*.\n\n'
                                            'Пожалуйста, выберите вид противопоказания, который Вы хотите посмотреть.',
                                       reply_markup=func.keyboard(12, [str(i) + '_' for i in range(27, 33)]),
                                       parse_mode='Markdown')
    elif call.data == '7_':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_message_id_06,
                                       text='Противопоказано:\n'
                                            '*Тразодон*\n'
                                            '*Азафен*\n'
                                            '*Миансерин*\n'
                                            '*Доксепин*\n'
                                            '*Тианептин*\n'
                                            '*Пипофезин*\n'
                                            '*Кломипрамин*\n'
                                            '*Имипрамин*\n'
                                            '*Милнаципран*\n'
                                            '*Венлафаксин*\n'
                                            '*Амитриптилин*\n'
                                            '*Миртазапин*\n'
                                            '*Вортиоксетин*\n'
                                            '*Флуоксетин*\n'
                                            '*Флувоксамин*\n'
                                            '*Пароксетин*\n'
                                            '*Эсциталопрам*',
                                       reply_markup=func.keyboard(3, '34_'),
                                       parse_mode='Markdown')
    elif call.data == '8_':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_message_id_06,
                                       text='В этой части мы предлагаем информацию о двух противопоказаниях:\n'
                                            '1. Посмотреть противопоказания *при судорожных состояниях и эпилепсии*.\n'
                                            '2. Посмотреть противопоказания *при состоянии после инсульта*.\n\n'
                                            'Пожалуйста, выберите вид противопоказания, который Вы хотите посмотреть:',
                                       reply_markup=func.keyboard(13, ['35_', '36_', '37_']),
                                       parse_mode='Markdown')
    elif call.data == '9_':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_message_id_06,
                                       text='В этой части мы предлагаем только противопоказания '
                                            '*при сахарном диабете*.\n\n'
                                            'Противопоказано:\n'
                                            '*Пипофезин*\n'
                                            '*Азафен*',
                                       reply_markup=func.keyboard(3, '38_'),
                                       parse_mode='Markdown')
    elif call.data == '10_':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_message_id_06,
                                       text='В этой части мы предлагаем информацию о пяти противопоказаниях:\n'
                                            '1. Посмотреть противопоказания *при мании*.\n'
                                            '2. Посмотреть противопоказания *при закрытоугольной глаукоме*.\n'
                                            '3. Посмотреть противопоказания *при инфекционных заболеваниях*.\n'
                                            '4. Посмотреть противопоказания *при нарушениях функции кроветворения*.\n'
                                            '5. Посмотреть противопоказания '
                                            '*при острой интоксикации алкоголем, снотворными,* '
                                            '*анальгетиками и психотропными препаратами*.\n'
                                            'Пожалуйста, выберите вид противопоказания, который Вы хотите посмотреть:',
                                       reply_markup=func.keyboard(14, [str(i) + '_' for i in range(39, 45)]),
                                       parse_mode='Markdown')
    elif call.data == '11_':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_message_id_06,
                                       text='Хотите посмотреть противопоказания препаратов в '
                                            'соответствии с характеристиками пациента?',
                                       reply_markup=func.keyboard(1, ['1_', '2_']))


@bot.main_bot.callback_query_handler(func=lambda call:
                                     call.data == '12_' or call.data == '13_' or call.data == '14_' or
                                     call.data == '15_' or call.data == '17_' or call.data == '18_' or
                                     call.data == '20_' or call.data == '21_' or call.data == '22_' or
                                     call.data == '23_' or call.data == '24_' or call.data == '25_' or
                                     call.data == '27_' or call.data == '28_' or call.data == '29_' or
                                     call.data == '30_' or call.data == '31_' or call.data == '35_' or
                                     call.data == '36_' or call.data == '39_' or call.data == '40_' or
                                     call.data == '41_' or call.data == '42_' or call.data == '43_')
def start4_04(call):
    global last_message_id_08

    if call.data == '12_':
        text = 'Противопоказано:\n*Амитриптилин прием внутрь.*'
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_message_id_06,
                                       text=text,
                                       parse_mode='Markdown')
        last_message_id_08 = bot.main_bot.send_message(chat_id=call.message.chat.id,
                                                       text=func.ending_words[0],
                                                       reply_markup=func.keyboard(2, ['45_', '46_', '47_'])).message_id
    elif call.data == '13_':
        text = 'Противопоказано:\n*Амитриптилин в/в введение.*'
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_message_id_06,
                                       text=text,
                                       parse_mode='Markdown')
        last_message_id_08 = bot.main_bot.send_message(chat_id=call.message.chat.id,
                                                       text=func.ending_words[0],
                                                       reply_markup=func.keyboard(2, ['45_', '46_', '47_'])).message_id
    elif call.data == '14_':
        text = 'Противопоказано:\n*Тианептин\nМилнаципран\nЭсциталопрам*'
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_message_id_06,
                                       text=text,
                                       parse_mode='Markdown')
        last_message_id_08 = bot.main_bot.send_message(chat_id=call.message.chat.id,
                                                       text=func.ending_words[0],
                                                       reply_markup=func.keyboard(2, ['45_', '46_', '47_'])).message_id
    elif call.data == '15_':
        text = 'Противопоказано:\n' \
               '*Азафен*\n' \
               '*Миансерин*\n' \
               '*Пипофезин*\n' \
               '*Вортиоксетин*\n' \
               '*Венлафаксин*\n' \
               '*Агомелатин*\n' \
               '*Флувоксамин*\n' \
               '*Пароксетин*'
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_message_id_06,
                                       text=f'{text}',
                                       parse_mode='Markdown')
        last_message_id_08 = bot.main_bot.send_message(chat_id=call.message.chat.id,
                                                       text=func.ending_words[0],
                                                       reply_markup=func.keyboard(2, ['45_', '46_', '47_'])).message_id
    elif call.data == '17_':
        text = 'Противопоказано:\n' \
               '*Пароксетин*\n' \
               '*Флувоксамин*\n' \
               '*Агомелатин*\n' \
               '*Венлафаксин*\n' \
               '*Дулоксетин*\n' \
               '*Миртазапин*\n' \
               '*Имипрамин*\n' \
               '*Кломипрамин*\n' \
               '*Пипофезин*\n' \
               '*Доксепин*\n' \
               '*Миансерин*\n' \
               '*Азафен*'
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_message_id_06,
                                       text=f'{text}',
                                       parse_mode='Markdown')
        last_message_id_08 = bot.main_bot.send_message(chat_id=call.message.chat.id,
                                                       text=func.ending_words[0],
                                                       reply_markup=func.keyboard(2, ['45_', '46_', '48_'])).message_id
    elif call.data == '18_':
        text = 'Противопоказано:\n*Агомелатин*'
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_message_id_06,
                                       text=f'{text}',
                                       parse_mode='Markdown')
        last_message_id_08 = bot.main_bot.send_message(chat_id=call.message.chat.id,
                                                       text=func.ending_words[0],
                                                       reply_markup=func.keyboard(2, ['45_', '46_', '48_'])).message_id
    elif call.data == '20_':
        text = 'Противопоказано:\n' \
               '*Пароксетин*\n' \
               '*Флуоксетин*\n' \
               '*Венлафаксин*\n' \
               '*Дулоксетин*\n' \
               '*Миртазапин*\n' \
               '*Имипрамин*\n' \
               '*Пипофезин*\n' \
               '*Доксепин*\n' \
               '*Азафен*'
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_message_id_06,
                                       text=f'{text}',
                                       parse_mode='Markdown')
        last_message_id_08 = bot.main_bot.send_message(chat_id=call.message.chat.id,
                                                       text=func.ending_words[0],
                                                       reply_markup=func.keyboard(2, ['45_', '46_', '49_'])).message_id
    elif call.data == '21_':
        text = 'Противопоказано:\n' \
               '*Имипрамин*\n' \
               '*Милнаципран*\n' \
               '*Пароксетин*\n' \
               '*Флуоксетин*'
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_message_id_06,
                                       text=f'{text}',
                                       parse_mode='Markdown')
        last_message_id_08 = bot.main_bot.send_message(chat_id=call.message.chat.id,
                                                       text=func.ending_words[0],
                                                       reply_markup=func.keyboard(2, ['45_', '46_', '49_'])).message_id
    elif call.data == '22_':
        text = 'Противопоказано:\n' \
               '*Флуоксетин*\n' \
               '*Имипрамин*'
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_message_id_06,
                                       text=f'{text}',
                                       parse_mode='Markdown')
        last_message_id_08 = bot.main_bot.send_message(chat_id=call.message.chat.id,
                                                       text=func.ending_words[0],
                                                       reply_markup=func.keyboard(2, ['45_', '46_', '49_'])).message_id
    elif call.data == '23_':
        text = 'Противопоказано:\n*Агомелатин*'
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_message_id_06,
                                       text=f'{text}',
                                       parse_mode='Markdown')
        last_message_id_08 = bot.main_bot.send_message(chat_id=call.message.chat.id,
                                                       text=func.ending_words[0],
                                                       reply_markup=func.keyboard(2, ['45_', '46_', '49_'])).message_id
    elif call.data == '24_':
        text = 'Противопоказано:\n*Кломипрамин\nДоксепин*'
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_message_id_06,
                                       text=f'{text}',
                                       parse_mode='Markdown')
        last_message_id_08 = bot.main_bot.send_message(chat_id=call.message.chat.id,
                                                       text=func.ending_words[0],
                                                       reply_markup=func.keyboard(2, ['45_', '46_', '49_'])).message_id
    elif call.data == '25_':
        text = 'Противопоказано:\n*Тразодон*'
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_message_id_06,
                                       text=f'{text}',
                                       parse_mode='Markdown')
        last_message_id_08 = bot.main_bot.send_message(chat_id=call.message.chat.id,
                                                       text=func.ending_words[0],
                                                       reply_markup=func.keyboard(2, ['45_', '46_', '49_'])).message_id
    elif call.data == '27_':
        text = 'Противопоказано:\n' \
               '*Амитриптилин*\n' \
               '*Имипрамин*\n' \
               '*Кломипрамин*\n' \
               '*Пипофезин*\n' \
               '*Доксепин*\n' \
               '*Миансерин*\n' \
               '*Азафен*\n' \
               '*Тразодон*'
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_message_id_06,
                                       text=f'{text}',
                                       parse_mode='Markdown')
        last_message_id_08 = bot.main_bot.send_message(chat_id=call.message.chat.id,
                                                       text=func.ending_words[0],
                                                       reply_markup=func.keyboard(2, ['45_', '46_', '50_'])).message_id
    elif call.data == '28_':
        text = 'Противопоказано:\n*Дулоксетин*'
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_message_id_06,
                                       text=f'{text}',
                                       parse_mode='Markdown')
        last_message_id_08 = bot.main_bot.send_message(chat_id=call.message.chat.id,
                                                       text=func.ending_words[0],
                                                       reply_markup=func.keyboard(2, ['45_', '46_', '50_'])).message_id
    elif call.data == '29_':
        text = 'Противопоказано:\n' \
               '*Пипофезин*\n' \
               '*Азафен*'
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_message_id_06,
                                       text=f'{text}',
                                       parse_mode='Markdown')
        last_message_id_08 = bot.main_bot.send_message(chat_id=call.message.chat.id,
                                                       text=func.ending_words[0],
                                                       reply_markup=func.keyboard(2, ['45_', '46_', '50_'])).message_id
    elif call.data == '30_':
        text = 'Противопоказано:\n' \
               '*Пипофезин*\n' \
               '*Азафен*\n' \
               '*Тахикардия*\n' \
               '*Тразодон*\n' \
               '*Аритмия*\n' \
               '*Тразодон*\n' \
               '*Кломипрамин*'
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_message_id_06,
                                       text=f'{text}',
                                       parse_mode='Markdown')
        last_message_id_08 = bot.main_bot.send_message(chat_id=call.message.chat.id,
                                                       text=func.ending_words[0],
                                                       reply_markup=func.keyboard(2, ['45_', '46_', '50_'])).message_id
    elif call.data == '31_':
        text = 'Противопоказано:\n' \
               '*Амитриптилин*\n' \
               '*Кломипрамин*\n' \
               '*Доксепин*'
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_message_id_06,
                                       text=f'{text}',
                                       parse_mode='Markdown')
        last_message_id_08 = bot.main_bot.send_message(chat_id=call.message.chat.id,
                                                       text=func.ending_words[0],
                                                       reply_markup=func.keyboard(2, ['45_', '46_', '50_'])).message_id
    elif call.data == '35_':
        text = 'Противопоказано:\n*Пароксетин\nФлуоксетин*'
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_message_id_06,
                                       text=f'{text}',
                                       parse_mode='Markdown')
        last_message_id_08 = bot.main_bot.send_message(chat_id=call.message.chat.id,
                                                       text=func.ending_words[0],
                                                       reply_markup=func.keyboard(2, ['45_', '46_', '51_'])).message_id
    elif call.data == '36_':
        text = 'Противопоказано:\n*Азафен\nПипофезин*'
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_message_id_06,
                                       text=f'{text}',
                                       parse_mode='Markdown')
        last_message_id_08 = bot.main_bot.send_message(chat_id=call.message.chat.id,
                                                       text=func.ending_words[0],
                                                       reply_markup=func.keyboard(2, ['45_', '46_', '51_'])).message_id
    elif call.data == '39_':
        text = 'Противопоказано:\n' \
               '*Пароксетин*\n' \
               '*Кломипрамин*\n' \
               '*Миансерин*'
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_message_id_06,
                                       text=f'{text}',
                                       parse_mode='Markdown')
        last_message_id_08 = bot.main_bot.send_message(chat_id=call.message.chat.id,
                                                       text=func.ending_words[0],
                                                       reply_markup=func.keyboard(2, ['45_', '46_', '52_'])).message_id
    elif call.data == '40_':
        text = 'Противопоказано:\n' \
               '*Пароксетин*\n' \
               '*Флуоксетин*\n' \
               '*Длоксетин*\n' \
               '*Амитриптилин*\n' \
               '*Имипрамин*\n' \
               '*Кломипрамин*\n' \
               '*Доксепин*'
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_message_id_06,
                                       text=f'{text}',
                                       parse_mode='Markdown')
        last_message_id_08 = bot.main_bot.send_message(chat_id=call.message.chat.id,
                                                       text=func.ending_words[0],
                                                       reply_markup=func.keyboard(2, ['45_', '46_', '52_'])).message_id
    elif call.data == '41_':
        text = 'Противопоказано:\n*Пипофезин\nАзафен*'
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_message_id_06,
                                       text=f'{text}',
                                       parse_mode='Markdown')
        last_message_id_08 = bot.main_bot.send_message(chat_id=call.message.chat.id,
                                                       text=func.ending_words[0],
                                                       reply_markup=func.keyboard(2, ['45_', '46_', '52_'])).message_id
    elif call.data == '42_':
        text = 'Противопоказано:\n*Пароксетин\nИмипрамин\nДоксепин*'
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_message_id_06,
                                       text=f'{text}',
                                       parse_mode='Markdown')
        last_message_id_08 = bot.main_bot.send_message(chat_id=call.message.chat.id,
                                                       text=func.ending_words[0],
                                                       reply_markup=func.keyboard(2, ['45_', '46_', '52_'])).message_id
    elif call.data == '43_':
        text = 'Противопоказано:\n*Амитриптилин*'
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_message_id_06,
                                       text=f'{text}',
                                       parse_mode='Markdown')
        last_message_id_08 = bot.main_bot.send_message(chat_id=call.message.chat.id,
                                                       text=func.ending_words[0],
                                                       reply_markup=func.keyboard(2, ['45_', '46_', '52_'])).message_id


@bot.main_bot.callback_query_handler(func=lambda call: call.data == '11_' or call.data == '16_' or
                                     call.data == '19_' or call.data == '26_' or call.data == '32_' or
                                     call.data == '34_' or call.data == '37_' or call.data == '38_' or
                                     call.data == '44_' or call.data == '45_' or call.data == '46_' or
                                     call.data == '47_' or call.data == '48_' or call.data == '49_' or
                                     call.data == '50_' or call.data == '51_' or call.data == '52_')
def start4_05(call):
    if call.data == '11_':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_message_id_06,
                                       text='Хотите посмотреть противопоказания препаратов в '
                                            'соответствии с характеристиками пациента?',
                                       reply_markup=func.keyboard(1, ['1_', '2_']))
    elif call.data == '45_':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_message_id_08,
                                       text=f'{func.ending_words[1]}\n'
                                            f'{func.ending_words[3]}')

    elif call.data == '46_':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_message_id_08,
                                       text=f'{func.ending_words[4]}')
    elif call.data == '47_':
        bot.main_bot.delete_message(chat_id=call.message.chat.id,
                                    message_id=last_message_id_08)
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_message_id_06,
                                       text='Возраст пациента?',
                                       reply_markup=func.keyboard(9, ['12_', '13_', '14_', '15_', '16_']))
    elif call.data == '48_':
        bot.main_bot.delete_message(chat_id=call.message.chat.id,
                                    message_id=last_message_id_08)
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_message_id_06,
                                       text='В этой части мы предлагаем информацию о двух противопоказаниях:\n'
                                            '1. Посмотреть противопоказания *при печеночной недостаточности*.\n'
                                            '2. Просмотреть противопоказания *при циррозе печени*.\n\n'
                                            'Пожалуйста, выберите вид противопоказания, который Вы хотите посмотреть.',
                                       reply_markup=func.keyboard(10, ['17_', '18_', '19_']),
                                       parse_mode='Markdown')
    elif call.data == '49_':
        bot.main_bot.delete_message(chat_id=call.message.chat.id,
                                    message_id=last_message_id_08)
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_message_id_06,
                                       text='В этой части мы предлагаем шесть противопоказаний:\n'
                                            '1. Посмотреть противопоказания *при почечной недостаточности*.\n'
                                            '2. Посмотреть противопоказания *при дисфункции гиперплазии предстательной '
                                            'железы*.\n'
                                            '3. Посмотреть противопоказания *при атонии мочевого пузыря*.\n'
                                            '4. Посмотреть противопоказания *при обструкции мочевыводящих путей*.\n'
                                            '5. Посмотреть противопоказания *при задержке мочи*.\n'
                                            '6. Посмотреть противопоказания *при наличии приапизма в анамнезе*.\n\n'
                                            'Пожалуйста, выберите вид противопоказания, который Вы хотите посмотреть.',
                                       reply_markup=func.keyboard(11, [str(i) + '_' for i in range(20, 27)]),
                                       parse_mode='Markdown')
    elif call.data == '50_':
        bot.main_bot.delete_message(chat_id=call.message.chat.id,
                                    message_id=last_message_id_08)
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_message_id_06,
                                       text='В этой части мы предлагаем информацию о пяти противопоказаниях:\n'
                                            '1. Посмотреть противопоказания '
                                            '*при остром и раннем восстановлении в период* '
                                            '*инфаркта миокарда*.\n'
                                            '2. Посмотреть противопоказания *при неконтролируемой АГ*.\n'
                                            '3. Посмотреть противопоказания *при ишемической болезни сердца*.\n'
                                            '4. Посмотреть противопоказания '
                                            '*при хронической сердечной недостаточности*.\n'
                                            '5. Посмотреть противопоказания *при нарушениях проводимости*.\n\n'
                                            'Пожалуйста, выберите вид противопоказания, который Вы хотите посмотреть.',
                                       reply_markup=func.keyboard(12, [str(i) + '_' for i in range(27, 33)]),
                                       parse_mode='Markdown')
    elif call.data == '51_':
        bot.main_bot.delete_message(chat_id=call.message.chat.id,
                                    message_id=last_message_id_08)
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_message_id_06,
                                       text='В этой части мы предлагаем информацию о двух противопоказаниях:\n'
                                            '1. Посмотреть противопоказания *при судорожных состояниях и эпилепсии*.\n'
                                            '2. Посмотреть противопоказания *при состоянии после инсульта*.\n\n'
                                            'Пожалуйста, выберите вид противопоказания, который Вы хотите посмотреть:',
                                       reply_markup=func.keyboard(13, ['35_', '36_', '37_']),
                                       parse_mode='Markdown')
    elif call.data == '52_':
        bot.main_bot.delete_message(chat_id=call.message.chat.id,
                                    message_id=last_message_id_08)
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_message_id_06,
                                       text='В этой части мы предлагаем информацию о пяти противопоказаниях:\n'
                                            '1. Посмотреть противопоказания *при мании*.\n'
                                            '2. Посмотреть противопоказания *при закрытоугольной глаукоме*.\n'
                                            '3. Посмотреть противопоказания *при инфекционных заболеваниях*.\n'
                                            '4. Посмотреть противопоказания *при нарушениях функции кроветворения*.\n'
                                            '5. Посмотреть противопоказания *при острой интоксикации алкоголем,* '
                                            '*снотворными, анальгетиками и психотропными препаратами*.\n\n'
                                            'Пожалуйста, выберите вид противопоказания, который Вы хотите посмотреть:',
                                       reply_markup=func.keyboard(14, [str(i) + '_' for i in range(39, 45)]),
                                       parse_mode='Markdown')
    else:
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_message_id_06,
                                       text='Предлагаем на выбор восемь видов противопоказаний:\n'
                                            '1. Посмотреть противопоказания *по возрасту*.\n'
                                            '2. Посмотреть противопоказания '
                                            '*по заболеваниям пищеварительной системы*.\n'
                                            '3. Посмотреть противопоказания *по заболеваниям мочеполовой системы*.\n'
                                            '4. Посмотреть противопоказания *по сердечно-сосудистой системе*.\n'
                                            '5. Посмотреть противопоказания *по беременности и периоду лактации*.\n'
                                            '6. Посмотреть противопоказания *по нервной системе*.\n'
                                            '7. Посмотреть противопоказания *по эндокринной системе*.\n'
                                            '8. Посмотреть противопоказания *по другим видам*.\n\n'
                                            'Пожалуйста, выберите вид противопоказания, который Вы хотите посмотреть:',
                                       reply_markup=func.keyboard(8, [str(i) + '_' for i in range(3, 12)]),
                                       parse_mode='Markdown')


if __name__ == "__main__":
    bot.main_bot.polling()
