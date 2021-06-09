import telebot
import log
import cataas
from os import environ

# export API_TOKEN=token
bot = telebot.TeleBot(environ.get('API_TOKEN'))

# '/start' command: bot starting first time
@bot.message_handler(commands = ['start'])
def send_welcome(message):
	bot.reply_to(message, """\
		Meow there :3\
		Thanks for using me, I'm so glad! (=^･^=)
		Type /help to know how to require cats. ;3
	""")
	log.start(message)

@bot.message_handler(commands = ['help'])
def send_usage(message):
	bot.reply_to(message, """\
		Meow! So you want to learn more about me (=^-ω-^=)\n
		/cat: send a random cat image
		/cat [...something else]: send a random cat image
		with the rest of the message written on the picture
		(e.g. /cat hello sends a random cat image with hello text)\n
		/gif: send a random animated cat image\n
		/cute: send a random cutie cat image :3
		/cute [...something else]: send a random cutie cat image
		with the rest of the message written on the picture
	""")
	log.help(message)

# '/cat' command: send a random cat
# if the command contains only '/cat' command, it sends a random cat picture
# if the command contains more words after '/cat' command, it sends a random
# cat picture with the rest of the message written on image in Impact font
@bot.message_handler(commands = ['cat'])
def cat(message):
	cid = message.chat.id
	bot.send_chat_action(cid, 'upload_photo')

	if (len(message.text.split()) == 1):
		cat = cataas.get_cat()
	else:
		phrase = (message.text).replace('/cat ', '')
		cat = cataas.get_labeled_cat(phrase)

	bot.send_photo(cid, cat)
	log.cat(message)

# '/cat' command: send a random gif cat
@bot.message_handler(commands = ['gif'])
def gif(message):
	cid = message.chat.id
	bot.send_chat_action(cid, 'upload_video')
	gif = cataas.get_gif()
	bot.send_video(cid, gif)
	log.gif(message)

# '/cute' command: send a cute cat
"""
TODO: check if given image is animated (send_video()) or not (send_photo())
@bot.message_handler(commands = ['cute'])
def cute(message):
	cid = message.chat.id
	bot.send_chat_action(cid, 'upload_photo')

	if (len(message.text.split()) == 1):
		cat = cataas.get_cat()
	else:
		phrase = (message.text).replace('/cute ', '')
		cat = cataas.get_labeled_cat(phrase)

	bot.send_photo(cid, cat)
	log.cute(message)
"""

# handle unknown messages/commands
@bot.message_handler(func=lambda message: True, content_types = ['text'])
def err(message):
	cid = message.chat.id
	bot.send_message(cid, '(ﾐ꒡ᆽ꒡ﾐ)\nUnknown command, please try again! :3')
	log.err(message)

bot.polling()