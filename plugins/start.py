from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("➕ Add me to your Group ➕", url="https://t.me/youtube_Downloder_4k_bot?startgroup=true")],
        
        [
            InlineKeyboardButton("👥 Official Group", url="https://t.me/anujasu"),
            InlineKeyboardButton("📣 Official Channel", url="https://t.me/musicworldanu"),
        
        ],
        [
            InlineKeyboardButton(
            "🎯 Owner", url="https://t.me/Anujasupulsara")]
    ])
    welcomed = f"✨ Welcome <b>{message.from_user.first_name}</b>\n\n 💭 ⭕️YouTube Downloader⭕️ allows you to youtube video Download📥 on groups through the new Telegram's Youtube link❕\n💡 All you have to do is send us the youtube link you want to download📥\n ❔Then select the quality of the Video or Song that you want to get \n\n 🎯. /help 👈 For more information"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
