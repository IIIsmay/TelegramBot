import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

# Включение логирования
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Ваш API токен
TOKEN = '7646668481:AAG9aBWp3apLqxE4Xu67c1ywhgPdwmV_P2U'

# Словарь для хранения ролей пользователей. В реальном приложении рекомендуется использовать БД.
user_roles = {
    'IIIsmay': 'admin',  # Замените на username администратора
}

# Функция для команды /start
async def start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    username = user.username
    if username in user_roles and user_roles[username] == 'admin':
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Добро пожаловать, администратор!")
    else:
        user_roles[username] = 'user'
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Добро пожаловать, пользователь!")

# Функция для команды /admin
async def admin_command(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    username = user.username
    if username in user_roles and user_roles[username] == 'admin':
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Выполняется административная команда.")
    else:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="У вас нет прав администратора для выполнения этой команды.")

# Основная функция для запуска бота
def main() -> None:
    # Создание приложения
    application = Application.builder().token(TOKEN).build()



    # Регистрация обработчиков команд
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("admin", admin_command))

    # Запуск бота
    application.run_polling()

if __name__ == '__main__':
    main()
