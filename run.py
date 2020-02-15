from mmpy_bot.bot import Bot
import re
from mmpy_bot.bot import listen_to
from mmpy_bot.bot import respond_to

@respond_to('hi', re.IGNORECASE)
def hi(message):
    print(message.get_username())
    message.reply('I can understand hi %s'%message.get_username())


@respond_to('I love you')
def love(message):
    message.reply('I love you too!')


@listen_to('Can someone help me?')
def help_me(message):
    # Message is replied to the sender (prefixed with @user)
    message.reply('Yes, I can!')



if __name__ == "__main__":
    Bot().run()