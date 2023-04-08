def register_messages(bot):

    @bot.message_handler(content_types=['text'])
    def send_welcome(message):
        chatID = message.chat.id
        if message.text.startswith("/"):
            return bot.send_message(chatID, "No entiendo que me intentas decir, mi hijo")
        bot.send_message(chatID, "Estas en el templo del morrogallo, en el templo de tu padre. Mi hijo")