# Thanks @Codeflix_Bots

import os
import logging
from logging.handlers import RotatingFileHandler

#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7242067053:AAHLoLKbLZhAcPzmmEIPcDQCxmVtk1iKsKU")

APP_ID = int(os.environ.get("APP_ID", "28871407"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "d22f32d4606020695cb51cf9aa480ce9")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002227081660"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "6155478725"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://rajeshpro123321:Vs9n8R90yUtCIyu4@clonestore1.w51yrrp.mongodb.net/?retryWrites=true&w=majority&appName=clonestore1")
DB_NAME = os.environ.get("DATABASE_NAME", "clonestore1")

#Shortner (token system) 

SHORTLINK_URL = os.environ.get("SHORTLINK_URL", "Publicearn.com")
SHORTLINK_API = os.environ.get("SHORTLINK_API", "a3726ab13339d68dfd481041dadd4ebebaebc11b")
VERIFY_EXPIRE = int(os.environ.get('VERIFY_EXPIRE', 86400)) # Add time in seconds
IS_VERIFY = os.environ.get("IS_VERIFY", "True")
TUT_VID = os.environ.get("TUT_VID","https://t.me/THEHEATHERS_OFFICIAL/46")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001678918073"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "<b>𝐇𝐞𝐥𝐥𝐨 {first}\n\n 𝐈 𝐚𝐦 𝐇𝐊 𝐒𝐓𝐎𝐑𝐄 𝐁𝐎𝐓 𝐈 𝐰𝐢𝐥𝐥 𝐬𝐡𝐚𝐫𝐞 𝐲𝐨𝐮𝐫 𝐜𝐨𝐧𝐭𝐞𝐧𝐭 𝐡𝐞𝐫𝐞 𝐟𝐢𝐫𝐬𝐭 𝐯𝐞𝐫𝐢𝐟𝐲 𝐌𝐞 𝐟𝐨𝐫 𝟐𝟒𝐡𝐫𝐬 𝐭𝐨 𝐠𝐞𝐭 𝐲𝐨𝐮𝐫 𝐩𝐫𝐞𝐦𝐢𝐮𝐦 𝐂𝐨𝐧𝐭𝐞𝐧𝐭. \n QUERY » @HKOWNER0</b>")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6155478725 5347709348").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "𝐒𝐨𝐫𝐫𝐲 {first} 𝐁𝐫𝐨/𝐒𝐢𝐬 𝐲𝐨𝐮 𝐡𝐚𝐯𝐞 𝐭𝐨 𝐣𝐨𝐢𝐧 𝐦𝐲 𝐜𝐡𝐚𝐧𝐧𝐞𝐥 𝐟𝐢𝐫𝐬𝐭 𝐭𝐨 𝐚𝐜𝐜𝐞𝐬𝐬 𝐟𝐢𝐥𝐞𝐬..\n\n 𝐒𝐨 𝐩𝐥𝐞𝐚𝐬𝐞 𝐣𝐨𝐢𝐧 𝐦𝐲 𝐜𝐡𝐚𝐧𝐧𝐞𝐥 𝐟𝐢𝐫𝐬𝐭 𝐚𝐧𝐝 𝐜𝐥𝐢𝐜𝐤 𝐨𝐧 “𝐍𝐨𝐰 𝐂𝐥𝐢𝐜𝐤 𝐡𝐞𝐫𝐞” 𝐛𝐮𝐭𝐭𝐨𝐧....!")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b> </b>")

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "True") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "HEllO ! ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ OWNER!!\n\n» ᴍʏ ᴏᴡɴᴇʀ : @HKOWNER0"

ADMINS.append(OWNER_ID)
ADMINS.append(6155478725)

LOG_FILE_NAME = "codeflixbot.txt"

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
