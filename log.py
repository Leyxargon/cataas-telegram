from datetime import datetime

def start(message):
	log = open('bot.log', 'a')
	timestamp = '[' + str(datetime.now().strftime("%d/%m/%Y %H:%M:%S")) + '] '
	user = str(message.from_user.first_name) + ' ' + str(message.from_user.last_name) + ' (' + str(message.from_user.username) + ') {id: ' + str(message.from_user.id) + '} '
	action = 'ha appena iniziato a usare il bot.\n'
	log.write(timestamp + user + action)
	log.close()

def help(message):
	log = open('bot.log', 'a')
	timestamp = '[' + str(datetime.now().strftime("%d/%m/%Y %H:%M:%S")) + '] '
	user = str(message.from_user.first_name) + ' ' + str(message.from_user.last_name) + ' (' + str(message.from_user.username) + ') {id: ' + str(message.from_user.id) + '} '
	action = 'ha voluto saperne di più sul bot.\n'
	log.write(timestamp + user + action)
	log.close()

def cat(message):
	log = open('bot.log', 'a')
	timestamp = '[' + str(datetime.now().strftime("%d/%m/%Y %H:%M:%S")) + '] '
	user = str(message.from_user.first_name) + ' ' + str(message.from_user.last_name) + ' (' + str(message.from_user.username) + ') {id: ' + str(message.from_user.id) + '} '
	action = 'ha richiesto un gatto.\n'
	log.write(timestamp + user + action)
	log.close()

def gif(message):
	log = open('bot.log', 'a')
	timestamp = '[' + str(datetime.now().strftime("%d/%m/%Y %H:%M:%S")) + '] '
	user = str(message.from_user.first_name) + ' ' + str(message.from_user.last_name) + ' (' + str(message.from_user.username) + ') {id: ' + str(message.from_user.id) + '} '
	action = 'ha richiesto una gif felina.\n'
	log.write(timestamp + user + action)
	log.close()

def cute(message):
	log = open('bot.log', 'a')
	timestamp = '[' + str(datetime.now().strftime("%d/%m/%Y %H:%M:%S")) + '] '
	user = str(message.from_user.first_name) + ' ' + str(message.from_user.last_name) + ' (' + str(message.from_user.username) + ') {id: ' + str(message.from_user.id) + '} '
	action = 'ha richiesto un gatto carino.\n'
	log.write(timestamp + user + action)
	log.close()

def err(message):
	log = open('bot.log', 'a')
	timestamp = '[' + str(datetime.now().strftime("%d/%m/%Y %H:%M:%S")) + '] '
	user = str(message.from_user.first_name) + ' ' + str(message.from_user.last_name) + ' (' + str(message.from_user.username) + ') {id: ' + str(message.from_user.id) + '} '
	action = 'ha scritto un comando non riconosciuto: '
	log.write(timestamp + user + action + message.text + '\n')
	log.close()