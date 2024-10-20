#(©)CodeXBotz




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "8167509992:AAFKCwwnAvPFRGpYJlMXYLZhxzL2alKWq0k")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "23930146"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "39a09d04b37eadf819d6cc64aedb9e44")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002254520923"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "7139599860"))

#Port
PORT = os.environ.get("PORT", "8036")

#Database
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://sy465143:B7UENblZjA3y3xAG>@cluster0.xeac9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "sy465143")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002389611214"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "-1002441410626"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "Hello {first} , Thanks for using me :D ⚡️.")
try:
    ADMINS=[6376328008]
    for x in (os.environ.get("ADMINS", "").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "👋 Hello {first}!\nPlease Join our channel First [ᴛᴀᴘ ᴏɴ ᴊᴏɪɴ ⚡] then\n Download by tapping on ⚡️Try Again  \nThank You ❤️")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "🚫 Please Avoid Direct Messages. I'm Here merely for file sharing!"

ADMINS.append(OWNER_ID)
ADMINS.append(5191566338)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   
