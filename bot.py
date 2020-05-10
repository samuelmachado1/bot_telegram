import telepot, time

bot = telepot.Bot('1179774061:AAH3aHOypzml5UExYjf5-u4Qt9NDM6dvEIc')

counter = 0

while True:
    time.sleep(1)
    bot.sendMessage(669262997, 'Mensagem número {}'.format(counter))
    counter += 1
