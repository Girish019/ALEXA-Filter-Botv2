#Coded by KA18 the @AMsupporttbot

import re
from os import environ,getenv
from Script import script 

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', '10755921'))
API_HASH = environ.get('API_HASH', 'd5e49fd3637cba407f17807d31c77977')
BOT_TOKEN = environ.get('BOT_TOKEN', "5864529187:AAEdXiJ4MMV18t0v3H-Y-xhiUonRMLQ84eY")

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 1800))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))

PICS = (environ.get('PICS', 'https://graph.org/file/bde9babd742b7980663fc.jpg')).split() #SAMPLE PIC
NOR_IMG = environ.get("NOR_IMG", "https://graph.org/file/5e57479b041fe676dc0d9.jpg")
MELCOW_VID = environ.get("MELCOW_VID", "")
MELCOW_IMG = environ.get("MELCOW_IMG", "https://graph.org/file/68fb96c0c50a45ca9e378.jpg")
SPELL_IMG = environ.get("SPELL_IMG", "https://graph.org/file/084bb003de163373b8875.jpg")
REST_NOT_FND = environ.get("REST_NOT_FND", "https://graph.org/file/ead67f78d85f79338bdac.jpg")

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '5636224141 1284476297 1147676731 1269341939').split()]
YT_ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('YT_ADMINS', '5636224141 1284476297 1269341939 1147676731').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1001704736253 -1001622331580').split()]
PREDVD_CHANNEL = int(environ.get("PREDVD_CHANNEL", "-1001758218450"))
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '5636224141 1284476297 1147676731 1269341939').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
PREMIUM = [int(user) if id_pattern.search(user) else user for user in environ.get('PREMIUM', "5636224141 1284476297 1147676731 1269341939").split()]
auth_channel = environ.get('AUTH_CHANNEL', '-1001861055084')
auth_grp = environ.get('AUTH_GROUP', '-1001860300137')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None
support_chat_id = environ.get('SUPPORT_CHAT_ID', '')
reqst_channel = environ.get('REQST_CHANNEL_ID', '-1002043663531')
REQST_CHANNEL = int(reqst_channel) if reqst_channel and id_pattern.search(reqst_channel) else None
SUPPORT_CHAT_ID = int(support_chat_id) if support_chat_id and id_pattern.search(support_chat_id) else None
NO_RESULTS_MSG = bool(environ.get("NO_RESULTS_MSG", True))
GRP_START_MSG = bool(environ.get("GRP_START_MSG", True))
OWNER = int(environ.get("OWNER", "5636224141"))

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://cheesy:cheesy.8697@cluster0.kjg8cfb.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Others
VERIFY = bool(environ.get('VERIFY', False))
SHORTLINK_URL = environ.get('SHORTLINK_URL', 'adlinkfly.in')
SHORTLINK_API = environ.get('SHORTLINK_API', 'a3f8fd04f9389222dca40c13c17b0d5f69a7e2be')
IS_SHORTLINK = bool(environ.get('IS_SHORTLINK', False))
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '-1002050485131').split()]
MAX_B_TN = environ.get("MAX_B_TN", "5")
MAX_BTN = is_enabled((environ.get('MAX_BTN', "True")), True)
PORT = environ.get("PORT", "8080")
GRP_LNK = environ.get('GRP_LNK', 'https://t.me/+WFACr-REeWc5Y2Vl')
CHNL_LNK = environ.get('CHNL_LNK', 'https://t.me/alexa_movies')
TUTORIAL = environ.get('TUTORIAL', 'https://t.me/firelinksguide/20')
IS_TUTORIAL = bool(environ.get('IS_TUTORIAL', True))
MSG_ALRT = environ.get('MSG_ALRT', 'Hᴇʟʟᴏ Mʏ Dᴇᴀʀ Fʀɪᴇɴᴅꜱ ❤️')
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1001657067333'))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'AMsupporttbot')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "False")), False)
IMDB = is_enabled((environ.get('IMDB', "False")), True)
AUTO_FFILTER = is_enabled((environ.get('AUTO_FFILTER', "True")), True)
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.IMDB_TEMPLATE_TXT}")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = int(environ.get('FILE_STORE_CHANNEL', '-1002043663531'))
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)

LANGUAGES = ["kannada", "kan", "malayalam", "mal", "tamil", "tam" ,"english", "eng", "hindi", "hin", "telugu", "tel", "Marathi", "Bengali", "Gujarati", "Punjabi", "Haryanvi", "Rajasthani"]

SEASONS = ["season 1" , "season 2" , "season 3" , "season 4", "season 5" , "season 6" , "season 7" , "season 8" , "season 9" , "season 10"]

# Online Stream and Download
NO_PORT = bool(environ.get('NO_PORT', False))
APP_NAME = None
if 'DYNO' in environ:
    ON_HEROKU = True
    APP_NAME = environ.get('APP_NAME')
else:
    ON_HEROKU = False
BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
URL = "https://alexa-filter-b2.onrender.com/".format(FQDN) if ON_HEROKU or NO_PORT else \
    "https://alexa-filter-b2.onrender.com/".format(FQDN, PORT)
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
WORKERS = int(environ.get('WORKERS', '10'))
SESSION_NAME = str(environ.get('SESSION_NAME', 'AMBot'))
MULTI_CLIENT = False
name = str(environ.get('name', 'ALEXA Movies'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
if 'DYNO' in environ:
    ON_HEROKU = True
    APP_NAME = str(getenv('APP_NAME'))

else:
    ON_HEROKU = False
HAS_SSL=bool(getenv('HAS_SSL',False))
if HAS_SSL:
    URL = "https://alexa-filter-b2.onrender.com/".format(FQDN)
else:
    URL = "https://alexa-filter-b2.onrender.com/".format(FQDN)

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"
