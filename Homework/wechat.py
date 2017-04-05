from __future__ import unicode_literals
from __future__ import print_function

import logging
import threading
import time

from wxpy import *

LOG_FILENAME = 'chat_history.log'
logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG,)

bot = Bot()

def display_headings(text):
    print('*' * 80)
    print('*' * 80)
    print(text.center(80, '*'))
    print('*' * 80)


def display_endings(count):
    count_text = " has {0} items".format(count)
    print(count_text.center(80, '*'))


def display_info():
    display_headings('所有的群')
    groups = bot.groups()
    print(groups)
    display_endings(len(groups))

    display_headings('所有的好友')
    friends = bot.friends()
    print(friends)
    display_endings(len(friends))


@bot.register()
def reply_my_friend(msg):
    logging.info('{0}: {1}'.format(time.time(), msg))


@bot.register(bot.friends().search('Amor')[0])
def reply_myself(msg):
    logging.info('{0}: {1}'.format(time.time(), msg))
    if msg.text == 'backup':
        logging.info('ready to execute linux command to backup file')


def main():
    display_info()
    python_class = bot.groups().search('Python')[0]
    python_class.send('我这条消息使用Python代码发送的')
    python_class.send('以后我们用Python代码聊天吧')
    bot.join()


if __name__ == '__main__':
    main()
