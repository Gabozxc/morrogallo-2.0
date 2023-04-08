import os

ruta_modules = os.path.abspath('modules')

def register_commands(bot):

    @bot.message_handler(commands=['qlq'])
    def send_welcome(message):
        chat = message.chat
        ruta_imagen = os.path.join(ruta_modules, 'static', 'qlq.jfif')
        with open(ruta_imagen, 'rb') as imagen:
            imagen_binaria = imagen.read()
        bot.send_photo(chat.id, imagen_binaria, caption="Q paso kausa?");