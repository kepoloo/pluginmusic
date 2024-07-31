import requests
from pyrogram import filters
from pyrogram.enums import ChatAction
from TheApi import api

from YukkiMusic import app


@app.on_message(
    filters.command(
        ["chatgpt", "ai", "ask"], prefixes=["/"]
    )
)
async def _(client, message):
    prs = await EMO.PROSES(client)
    sks = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    try:
        await client.send_chat_action(message.chat.id, ChatAction.TYPING)

        if len(message.command) < 2:
            await message.reply_text(
                f"{ggl}<b>ᴍᴏʜᴏɴ ɢᴜɴᴀᴋᴀɴ ғᴏʀᴍᴀᴛ\nᴄᴏɴᴛᴏʜ : </b><code>ask bagaimana membuat donat?</code>"
            )
        else:
            prs = await message.reply_text(f"<b>{prs}ᴘʀᴏᴄᴄᴇsɪɴɢ....</b>")
            a = message.text.split(' ', 1)[1]
            response = requests.get(f'https://chatgpt.apinepdev.workers.dev/?question={a}')

            try:
                if "answer" in response.json():
                    x = response.json()["answer"]                  
                    await prs.edit(
                      f"{x}<b>{sks}ᴘᴇʀᴛᴀɴʏᴀᴀɴ ɪɴɪ ᴅɪᴊᴀᴡᴀʙ ᴏʟᴇʜ</b> : <code>{bot.me.mention}</code>"
                    )
                else:
                    await message.reply_text(f"<b>{ggl}ɴᴏ 'ʀᴇsᴜʟᴛs' ᴋᴇʏ ғᴏᴜɴᴅ ɪɴ ᴛʜᴇ ʀᴇsᴘᴏɴsᴇ.</b>")
            except KeyError:
                await message.reply_text(f"<b>ᴇʀʀᴏʀ ᴀᴄᴄᴇssɪɴɢ ᴛʜᴇ ʀᴇsᴘᴏɴsᴇ.</b>")
    except Exception as e:
        await message.reply_text(f"{e}")


__MODULE__ = "ChatGPT"
__HELP__ = """
/advice - ɢᴇᴛ ʀᴀɴᴅᴏᴍ ᴀᴅᴠɪᴄᴇ ʙʏ ʙᴏᴛ
/ai [ǫᴜᴇʀʏ] - ᴀsᴋ ʏᴏᴜʀ ǫᴜᴇsᴛɪᴏɴ ᴡɪᴛʜ ᴄʜᴀᴛɢᴘᴛ's ᴀɪ
/gemini [ǫᴜᴇʀʏ] - ᴀsᴋ ʏᴏᴜʀ ǫᴜᴇsᴛɪᴏɴ ᴡɪᴛʜ ɢᴏᴏɢʟᴇ's ɢᴇᴍɪɴɪ ᴀɪ
/bard [ǫᴜᴇʀʏ] -ᴀsᴋ ʏᴏᴜʀ ǫᴜᴇsᴛɪᴏɴ ᴡɪᴛʜ ɢᴏᴏɢʟᴇ's ʙᴀʀᴅ ᴀɪ"""
