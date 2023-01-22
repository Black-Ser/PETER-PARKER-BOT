from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram import filters, Client, errors, enums
from pyrogram.errors import UserNotParticipant
from pyrogram.errors.exceptions.flood_420 import FloodWait
from database import add_user, add_group, all_users, all_groups, users, remove_user
from configs import cfg
import random, asyncio

app = Client(
    "approver",
    api_id=cfg.API_ID,
    api_hash=cfg.API_HASH,
    bot_token=cfg.BOT_TOKEN
)

gif = [
    'https://te.legra.ph/file/a1b3d4a7b5fce249902f7.mp4',
    'https://te.legra.ph/file/0c855143a4039108df602.mp4',
    'https://te.legra.ph/file/d7f3f18a92e6f7add8fcd.mp4',
    'https://te.legra.ph/file/9e334112ee3a4000c4164.mp4',
    'https://te.legra.ph/file/652fc39ae6295272699c6.mp4',
    'https://te.legra.ph/file/702ca8761c3fd9c1b91e8.mp4',
    'https://te.legra.ph/file/a1b3d4a7b5fce249902f7.mp4',
    'https://te.legra.ph/file/d7f3f18a92e6f7add8fcd.mp4',
    'https://te.legra.ph/file/0c855143a4039108df602.mp4',
    'https://te.legra.ph/file/9e334112ee3a4000c4164.mp4',
    'https://te.legra.ph/file/702ca8761c3fd9c1b91e8.mp4'
]


#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ Main process ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.on_chat_join_request(filters.group | filters.channel & ~filters.private)
async def approve(_, m : Message):
    op = m.chat
    kk = m.from_user
    try:
        add_group(m.chat.id)
        await app.approve_chat_join_request(op.id, kk.id)
        img = random.choice(gif)
        await app.send_video(kk.id,img, "**Hello {}!\nWelcome To {}\n\n__Powerd By : @HyperBotz**".format(m.from_user.mention, m.chat.title))
        add_user(kk.id)
    except errors.PeerIdInvalid as e:
        print("user isn't start bot(means group)")
    except Exception as err:
        print(str(err))    
