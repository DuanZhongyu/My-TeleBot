# My-TeleBot
这是一个基于Telegram平台的心理医学诊断聊天机器人项目。
此项目是我2023.9 - 2024.5期间在谢东诺夫莫斯科第一医科大学的“医学数据分析师”培训项目的毕业设计。

毕设分为医学研究和聊天机器人开发（我自认为是这样的哈），而本项目仅聚焦于聊天机器人开发。
该聊天机器人具备4个功能，分别是：
1、抑郁症诊断以及药物治疗建议。
2、临床治疗策略推荐。
3、药物兼容性分析。
4、禁忌症药物分析。
上述四个功能的代码实现，分别位于start1，start2，start3和start4中。
全部代码出自于本人（仅2年的Python学习经验），结构简单，逻辑清晰，最麻烦之处无非就是按照既定逻辑设置大量按钮的回调函数。
请各位继续阅读下述内容，相信在此之后，会更容易理解代码。

使用Python在Telegram平台上开发聊天机器人并不复杂，尤其是在本项目中，仅仅使用了3个特定的库对象便可实现上述全部功能。
我将按照三个库分类为各位讲解使用到的函数。

一、telebot库
导入telebot库即可对机器人进行代码控制。

1、创建机器人

核心语法为：
import telebot
bot = telebot.TeleBot('机器人的API')

实例化一个机器人对象，并赋予其用户创建机器人所获取的API，即可在后续代码中，直接对该机器人进行操作。非常方便！
上述内容在bot.py文件中实现。

2、发送信息

核心语法：
@bot.main_bot.message_handler(commands=['start1'])
  bot.send_message(chat_id=chat_id,
                 text='你好，*世界*！',
                 parse_mode='Markdown')


使用send_message方法即可完成对用户的消息发送。


3、反复编辑

二、InlineKeyboardButton库和InlineKeyboardMarkup库
导入InlineKeyboardButton库和InlineKeyboardMarkup库即可设置聊天当中的按钮事件。

1、设置按钮
核心语法为：
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
keyboard = InlineKeyboardMarkup()  #键盘实例化
button = InlineKeyboardButton('Да', callback_data=b)  # 按钮实例化
keyboard.add(button)  # 按钮添加到键盘中

很好理解，想象一下，想让机器人在聊天中对用户发出问询，假如答案只有“是”与“否”两个回答，那么用户通过点击“是”按钮或者“否”按钮，即可跳转到对应的代码逻辑中继续进行对话。代码 keyboard = InlineKeyboardMarkup() 就是机器人在提问完之后，在下方勾勒出一个内联键盘，当然了，这是不可见的，只为方便后续操作。然后在键盘中添加相应的按钮即可。设置按钮主要设置两方面，一是按钮名称（字符串类型），二是触发事件的标签（字符串类型）。代码 button = InlineKeyboardButton('Да', callback_data=b) 中，'Да'是按钮名称，b是触发事件的标签（注意，到此只设置了触发事件的标签，而非具体的触发事件）。按钮设计完成后，只需要将其加入到内联键盘中即可 keyboard.add(button) 。此处只设置了一个按钮，实际过程中，我们可以添加若干不同的按钮。
上述内容在func.py文件中实现。

bot.main_bot.send_message(chat_id=chat_id,
                          text='你好，世界！',
                          reply_markup=keyboard,
                          parse_mode='Markdown')

2、触发事件
@bot.main_bot.callback_query_handler(func=lambda call: call.data == 'a' or call.data == 'b')
def start1_17(call):
    if call.data == 'a':
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_msg_id_01_02,
                                       text=f'{func.ending_words[4]}')  # 更多命令
    else:
        bot.main_bot.edit_message_text(chat_id=call.message.chat.id,
                                       message_id=last_msg_id_01_02,
                                       text=f'{func.ending_words[2]}\n'
                                            f'{func.ending_words[3]}')  # 更多命令
