import telepot, time

bot = telepot.Bot('ID_DO_BOT:TOKEN_DO_BOT')

counter = 0

while True:
    time.sleep(1)
    bot.sendMessage(ID_DA_MENSAGEM, 'Mensagem número {}'.format(counter))
    counter += 1
