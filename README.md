# Pizza Bot

This Telegram bot is designed for convenient ordering of dishes from the "Pizza" restaurant menu. The bot provides the ability to reserve a table at the restaurant or order delivery.

## Key Features:

1. **Start and Interaction:**
   - Upon bot launch, the user receives a welcome message and access to basic commands.

2. **Working Hours:**
   - Users can inquire about the restaurant's operating hours, address, and contact number.

3. **Menu:**
   - The bot provides a link to an online menu where users can explore the offered dishes.

4. **Table Reservation:**
   - Users can reserve a table at the restaurant by following the bot's instructions:
     - Choose "🤳Reserve a Table."
     - Provide a phone number.
     - Enter the name.
     - Specify the date and time of the reservation.
     - Confirm the reservation.

5. **Delivery:**
   - Users can place an order for food delivery by following these steps:
     - Choose "🚘Delivery."
     - Provide a phone number.
     - Enter the name.
     - Specify the delivery address.
     - List the desired dishes.
     - Confirm the order.

6. **Confirmation and Cancellation:**
   - After entering the required information, users can confirm or cancel their choice:
     - "✅Yes" - confirm the reservation or order.
     - "❌No" - cancel the reservation or order.

## Installation and Execution:

1. **Dependency Installation:**
   - Ensure Python is installed on your system.
   - Create a virtual environment: `python -m venv venv`
   - Activate the virtual environment:
     - On Windows: `venv\Scripts\activate`
     - On MacOS/Linux: `source venv/bin/activate`
   - Install dependencies: `pip install -r requirements.txt`

2. **Environment Variable Configuration:**
   - Create a file named `.env` in the project's root and specify the following variables:
     ```
     BOT_TOKEN=your_bot_token
     ADMIN_CHANNEL_ID=admin_channel_identifier
     ```

3. **Bot Launch:**
   - Start the bot with the command: `python main.py`

## Technologies Used:

- [aiogram](https://docs.aiogram.dev/) - Library for creating Telegram bots.
- [pydantic](https://pydantic-docs.helpmanual.io/) - Library for handling settings and data validation.

## Developer:

Project developed by [lilrory](https://github.com/lilrory).
