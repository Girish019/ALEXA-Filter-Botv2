
from pyrogram import Client, filters
from info import CHANNELS, PREDVD_CHANNEL
from database.ia_filterdb import save_file , pre_dvd_savefile

media_filter = filters.document | filters.video | filters.audio


@Client.on_message(filters.chat(CHANNELS) & media_filter)
async def media(bot, message):
    """Media Handler"""
    for file_type in ("document", "video", "audio"):
        media = getattr(message, file_type, None)
        if media is not None:
            break
    else:
        return

    media.file_type = file_type
    media.caption = message.caption
    await save_file(media)


@Client.on_message(filters.chat(PREDVD_CHANNEL) & media_filter)
async def premediaindex(bot, message):
    """Media Handler"""
    for file_type in ("document", "video", "audio"):
        media = getattr(message, file_type, None)
        if media is not None:
            break
    else:
        return

    media.file_type = file_type
    media.caption = message.caption
    cout = await pre_dvd_savefile(media)
    try:
        count = cout.count(media)
        await client.send_message(PREDVD_CHANNEL, f"pre DVD files are saved = {count}")
    except:
        await client.send_message(PREDVD_CHANNEL, "pre DVD files are saved in daatabase")



