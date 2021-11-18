from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("➕ Add me to your Group ➕", url="https://t.me/youtube_Downloder_4k_bot?startgroup=true")],
        
        [
            InlineKeyboardButton("MY😊 Group", url="https://t.me/anujasu"),
            InlineKeyboardButton("MY😊 Channel", url="https://t.me/musicworldanu"),
        
        ],
        [
            InlineKeyboardButton(
            "🎯 Owner", url="https://t.me/Anujasupulsara")]
    ])
    welcomed = f"✨ Welcome <b>{message.from_user.first_name}</b>\n\n 🎯.allows you to youtube video Download📥 on groups through the new Telegram's Youtube link \n\n 🎯. /help 👈 For more information"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
