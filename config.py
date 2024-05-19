import os

API_ID = API_ID = 29274614

API_HASH = os.environ.get("API_HASH", "084def93d7b7414f819a7cff68fe9c56")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7119740517:AAHN0QTKaf9JcQc7rkXMxriSTzYMV3volgc")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 6981453498))

LOG = -1002066747117

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5987970971").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


