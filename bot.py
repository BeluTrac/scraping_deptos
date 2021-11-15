from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import gspread
from settings import BOT_TOKEN

def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Hola! Soy un bot!"
    )

start_handler = CommandHandler('start', start)


def añadir_id(update, context):
    gs = gspread.service_account(filename = "/home/belutrac/Documentos/scraping_deptos/zeta-rush-332114-45d522cbfb7c.json")
    hoja = gs.open_by_url("https://docs.google.com/spreadsheets/d/19HUgkqo3uPXozf7PeaGg1MIGnD0GPQOmZyKjMNnjCWc/edit#gid=0")
    hoja1 = hoja.get_worksheet(1)
    hoja1.append_row([update.effective_chat.id])
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Listo che"
    )


echo_handler = CommandHandler('Holi', añadir_id)


if __name__ == "__main__":
    updater = Updater(token=BOT_TOKEN)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(echo_handler)

    updater.start_polling()