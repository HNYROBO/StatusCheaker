from pyrogram import Client, filters
from pyrogram.errors import FloodWait
import asyncio
import datetime
import pytz
import os

app = Client(
    name = "HNY",
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"],
    session_string = os.environ["SESSION_STRING"]
)
TIME_ZONE = os.environ["TIME_ZONE"]
BOT_LIST = [i.strip() for i in os.environ.get("BOT_LIST").split(' ')]
CHANNEL_OR_GROUP_ID = int(os.environ["CHANNEL_OR_GROUP_ID"])
MESSAGE_ID = int(os.environ["MESSAGE_ID"])
BOT_ADMIN_IDS = [int(i.strip()) for i in os.environ.get("BOT_ADMIN_IDS").split(' ')]

async def main_surya():
    async with app:
            while True:
                print("Checking...")
                xxx_surya = f"β ππππ π½ππ πππΌπππ β"
                for bot in BOT_LIST:
                    try:
                        yyy_surya = await app.send_message(bot, "/start")
                        aaa = yyy_surya.id
                        await asyncio.sleep(10)
                        zzz_surya = app.get_chat_history(bot, limit = 1)
                        async for ccc in zzz_surya:
                            bbb = ccc.id
                        if aaa == bbb:
                            xxx_surya += f"\n\nπ€  @{bot}\n        β **βπΏπππβ** β"
                            for bot_admin_id in BOT_ADMIN_IDS:
                                try:
                                    await app.send_message(int(bot_admin_id), f"π¨ **Oops !This @{bot} is down currently** β")
                                except Exception:
                                    pass
                            await app.read_chat_history(bot)
                        else:
                            xxx_surya += f"\n\nπ€  @{bot}\n        β **β ππππΏπΌ ππ π½πΌπ½π β** β"
                            await app.read_chat_history(bot)
                    except FloodWait as e:
                        await asyncio.sleep(e.x)            
                time = datetime.datetime.now(pytz.timezone(f"{TIME_ZONE}"))
                last_update = time.strftime(f"%d %b %Y at %I:%M %p")
                xxx_surya += f"\n\nββοΈ πππ¨π© πππππ ππ π€π£ : {last_update} ({TIME_ZONE})\n\n**β ππ©ππ©πͺπ¨ ππππ§ππ¨π ππͺπ©π€π’ππ©ππππ‘π‘π? πππ©ππ§ ππ«ππ§π? 60 π’ππ£ β**"
                await app.edit_message_text(int(CHANNEL_OR_GROUP_ID), MESSAGE_ID, xxx_surya)
                print(f"Last checked on: {last_update}")                
                await asyncio.sleep(3600)
                        
app.run(main_surya())
