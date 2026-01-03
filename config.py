# config.py
import os
from dotenv import load_dotenv

# ================== НАЛАШТУВАННЯ ==================
# Для локального тестування: створи файл .env в корені проекту і заповни його
# Для Railway: ці змінні будуть автоматично доступні через Environment Variables

# Завантажуємо .env тільки якщо ми НЕ на Railway (там .env не потрібен і може не бути)
if not os.getenv("RAILWAY_ENVIRONMENT"):
    load_dotenv()  # шукає файл .env в корені

# ------------------ ОБОВ'ЯЗКОВІ ЗМІННІ ------------------
BOT_TOKEN = os.getenv("BOT_TOKEN")
DATABASE_URL = os.getenv("DATABASE_URL")

if not BOT_TOKEN:
    raise ValueError("⚠️ BOT_TOKEN не знайдено! Встанови в .env або в змінних Railway.")

if not DATABASE_URL:
    raise ValueError("⚠️ DATABASE_URL не знайдено! Встанови в .env або в змінних Railway.")

# ------------------ ДОДАТКОВІ НАЛАШТУВАННЯ ------------------
# Часовий пояс (можна змінити, якщо потрібно)
TIMEZONE_STR = os.getenv("TIMEZONE", "Europe/Kyiv")

# Логування (опціонально: True для детальних логів під час розробки)
DEBUG = os.getenv("DEBUG", "False").lower() in ("true", "1", "yes")

# Максимальна кількість днів для "останні N днів" (захист від надто великих запитів)
MAX_CUSTOM_DAYS = int(os.getenv("MAX_CUSTOM_DAYS", "730"))  # ~2 роки

# Список адмінів — користувачі, які можуть використовувати /a
ADMIN_USERS = {663289676}  # ← заміни на свій Telegram user_id (можна додати кілька через кому)