import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", 20562331))
    API_HASH = os.environ.get("API_HASH", "9e3e4148e73756a85b95fc69980b678d")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7817959650:AAFaBqYG65HUalQQwIDrq3-I80LQkeka_3c")
    BOT_SESSION_NAME = os.environ.get("BOT_SESSION_NAME", "LinkSearchBot")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "BQGqGQsAcI4m62K_TlEglxBYj5SA2hEn_0F6kSTj1D0sMT8Mw8UlAHeSPSjRmsQrvOIjnhKEetbYDMQKWtqDg6YoynD4npLwtZMJYJONXtY2IhfZhEfB4OOOClwyo277SLNCnZyDGKIP3D4HPq7KOzB8WaVgdAFlVuV2HiIv0gfbDe22ZMAHZ849QBu7FiNE7X8Rdz8M0NXyaxPwB2z6CawO614X5nQrYDT-qL5LwQd3l1vjBpI3dwFYfz5efQj8V2MxEOHASSYLs7c9GMJXooDlfEGuF9XrxxDTye7q3Pu057FTOpqqWYS4cM0T52gz-2saJ8RckN3wQx2OeZS3kmgU9UsXGwAAAAB9nzd3AA")
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", -1002390640098))
    BOT_USERNAME = os.environ.get("BOT_USERNAME")
    BOT_OWNER = int(os.environ.get("BOT_OWNER"))
    DATABASE_URL = os.environ.get("DATABASE_URL")
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
    ABOUT_BOT_TEXT = """<b>This is Link Search Bot.
    
    
    
🤖 My Name: <a href='https://youtube.com/@bilijackson'>Link Search Bot</a>

📝 Language : <a href='https://www.python.org'> Python V3</a>

📚 Library: <a href='https://docs.pyrogram.org'> Pyrogram</a>

📡 Server: <a href='koyeb.com'>Koyeb</a>

👨‍💻 Created By: <a href='https://t.me/GreyMatter_Bot'>GreyMatter's Bot</a></b>
"""

    ABOUT_HELP_TEXT = """<b>👨‍💻 Creator : <a href='https://t.me/DramaMob'>Updates Channel</a>
If You Want Your Own Bot Like This Then You Can Contact Our Creator.</b>
"""

    HOME_TEXT = """
<b>Hey! {}😅,

I'm Link Search Bot.🤖

I Can Search 🔍 What You Want❗

<a>Made With ❤ By @DramaMob</a></b>
"""


    START_MSG = """
<b>Hey! {}😅,

I'm Link Search Bot.🤖

I Can Search 🔍 What You Want❗

<a>Made With ❤ By @DramaMob</a></b>
"""

