import json
import os

def get_user_list(config, key):
    with open('{}/Manager/{}'.format(os.getcwd(), config), 'r') as json_file:
        return json.load(json_file)[key]


# Create a new config.py or rename this to config.py file in same dir and import, then extend this class.
class Config(object):
    LOGGER = True

    # REQUIRED
    API_KEY = "1823485628:AAE2_i8m3dKXTaTiO0Kw626QoRuApw_2bjs"
    OWNER_ID = "1461968113"  # If you dont know, run the bot and do /id in your private chat with it
    OWNER_USERNAME = "itzz_axel"  #Just write it without the @ ex "Sawada"
    SUPPORT_CHAT = "akenosupportchat" # Your telegram support chat username, must have the "@" Example: @MyBotSupportGroupChat

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = 'postgres://stella:stella123@database-1.cuzno6euao1o.us-east-2.rds.amazonaws.com:5431/dbname'  # needed for any database modules
    MESSAGE_DUMP = -1001395712266  # needed to make sure 'save from' messages persist
    GBAN_LOGS = -1001395712266 #Channel ID here with the hyphen like -123456789
    LOAD = []
    NO_LOAD = ['translation', 'rss', 'cleaner', 'feds']   
    WEBHOOK = False
    URL = None

    # OPTIONAL
    #ID Seperation format [1,2,3,4]
    SUDO_USERS = '1461968113'  # List of id's -  (not usernames) for users which have sudo access to the bot.
    DEV_USERS = '1461968113'  # List of id's - (not usernames) for developers who will have the same perms as the owner
    SUPPORT_USERS = '1461968113'  # List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    WHITELIST_USERS = '1461968113' # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    DONATION_LINK = None  # EG, paypal
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True  #Delete commands that users dont have access to, like delete /ban if a non admin uses it.
    STRICT_GBAN = True
    WORKERS = 8  # Number of subthreads to use. Set as number of threads your processor uses
    BAN_STICKER = 'CAADAgADOwADPPEcAXkko5EB3YGYAg'  # banhammer marie sticker
    ALLOW_EXCL = True  # Allow ! commands as well as / (Leave this to true so that blacklist can work)
    CASH_API_KEY = None # Get one from https://www.alphavantage.co/support/#api-key
    TIME_API_KEY = None # Get one from https://timezonedb.com/register
    AI_API_KEY = None # Coffeehouse chatbot api key, get one from https://coffeehouse.intellivoid.info/
    WALL_API = None # Get one from https://wall.alphacoders.com/api.php
    BL_CHATS = [] # List of groups that you want blacklisted. 


class Production(Config):
    LOGGER = True


class Development(Config):
    SPAMMERS = None
    TIGER_USERS = None
    LOGGER = True
