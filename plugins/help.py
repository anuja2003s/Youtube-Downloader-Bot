from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"දැනට සහය දක්වන්නේ Youtube Single එකකට පමණි😇 (ප්ලේලිස්ට් නොමැත) Just Send Youtube Url 📥"
    await message.reply_text(helptxt)
