from mmpy_bot.bot import Bot
import re
from mmpy_bot.bot import listen_to
from mmpy_bot.bot import respond_to
import wisdom
import email_sender

@respond_to('$', re.IGNORECASE)
def hi(message):
    leave_type = "Casual"
    name = message.get_username()
    date, leave_type, response = wisdom.text_analyser(message.get_message())
    email_sender.send_the_mail(name,date,leave_type)
    message.reply(response)

if __name__ == "__main__":
    Bot().run()