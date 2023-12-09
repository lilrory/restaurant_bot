Pizza Bot
This Telegram bot is designed for convenient ordering of dishes from the "Pizza" restaurant menu. The bot provides the ability to reserve a table at the restaurant or order delivery.

Key Features:
Start and Interaction:

Upon bot launch, the user receives a welcome message and access to basic commands.
🕓Working Hours:

Users can inquire about the restaurant's operating hours, address, and contact number.
📕Menu:

The bot provides a link to an online menu where users can explore the offered dishes.
Table Reservation:

Users can reserve a table at the restaurant by following the bot's instructions:
Choose "🤳Reserve a Table."
Provide a phone number.
Enter the name.
Specify the date and time of the reservation.
Confirm the reservation.
Delivery:

Users can place an order for food delivery by following these steps:
Choose "🚘Delivery."
Provide a phone number.
Enter the name.
Specify the delivery address.
List the desired dishes.
Confirm the order.
Confirmation and Cancellation:

After entering the required information, users can confirm or cancel their choice:
"✅Yes" - confirm the reservation or order.
"❌No" - cancel the reservation or order.
Installation and Execution:
Dependency Installation:

Ensure Python is installed on your system.
Create a virtual environment: python -m venv venv
Activate the virtual environment:
On Windows: venv\Scripts\activate
On MacOS/Linux: source venv/bin/activate
Install dependencies: pip install -r requirements.txt
Environment Variable Configuration:

Create a file named .env in the project's root and specify the following variables:
makefile
Copy code
BOT_TOKEN=your_bot_token
ADMIN_CHANNEL_ID=admin_channel_identifier
Bot Launch:

Start the bot with the command: python main.py
Technologies Used:
aiogram - Library for creating Telegram bots.
pydantic - Library for handling settings and data validation.
Developer:
Project developed by ([https://github.com/lilrory]).



Pizza Bot
Этот Telegram-бот предназначен для удобного заказа блюд из меню ресторана "Pizza". Бот предоставляет возможность забронировать стол в ресторане или заказать доставку.

Основные функции:
Старт и общение:

При запуске бота, пользователь получает приветственное сообщение и доступ к основным командам.
🕓Режим работы:

Пользователь может узнать режим работы ресторана, адрес и контактный номер.
📕Меню:

Бот предоставляет ссылку на онлайн-меню, где пользователь может ознакомиться с предлагаемыми блюдами.
Забронировать стол:

Пользователь может зарезервировать стол в ресторане, следуя инструкциям бота:
Выбор "🤳Забронировать стол".
Указание номера телефона.
Ввод имени.
Указание даты и времени бронирования.
Подтверждение бронирования.
Доставка:

Пользователь может оформить заказ на доставку блюд:
Выбор "🚘Доставка".
Указание номера телефона.
Ввод имени.
Указание адреса доставки.
Указание желаемых блюд.
Подтверждение заказа.
Подтверждение и отмена:

После ввода необходимой информации, пользователь может подтвердить или отменить свой выбор:
"✅Да" - подтверждение бронирования или заказа.
"❌Нет" - отмена бронирования или заказа.
Установка и запуск:
Установка зависимостей:

Убедитесь, что у вас установлен Python.
Создайте виртуальное окружение: python -m venv venv
Активируйте виртуальное окружение:
В Windows: venv\Scripts\activate
В MacOS/Linux: source venv/bin/activate
Установите зависимости: pip install -r requirements.txt
Настройка переменных окружения:

Создайте файл .env в корне проекта и укажите следующие переменные:
BOT_TOKEN=ваш_токен_бота
ADMIN_CHANNEL_ID=идентификатор_канала_администратора
Запуск бота:

Запустите бота командой: python main.py
Используемые технологии:
aiogram - библиотека для создания ботов на платформе Telegram.
pydantic - библиотека для работы с настройками и валидацией данных.
Разработчик:
Проект разработан ([https://github.com/lilrory]).
