#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG & @Mrk_YT

from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram.errors import UserNotParticipant
from bot import Translation # pylint: disable=import-error
from bot.database import Database # pylint: disable=import-error
from bot import UPDATE_CHANNEL # Update Text Message Channel Update
from bot import MRK_YT_MASTER
from bot import MT_GROUP
from bot import MT_CHANNEL # Main Channel Added
from bot.motech import MT_BOT_UPDATES

db = Database()

@Client.on_message(filters.command(["start"]) & filters.private, group=1)
async def start(bot, update):
    update_channel = UPDATE_CHANNEL
    if update_channel:
        try:
            user = await bot.get_chat_member(update_channel, update.chat.id)
            if user.status == "kicked out":
               await update.reply_text("😔 Sorry Dude, You are **🅱︎🅰︎🅽︎🅽︎🅴︎🅳︎ 🤣🤣🤣**")
               return
        except UserNotParticipant:
            #await update.reply_text(f"Join @{update_channel} To Use Me")
            await update.reply_text(
                text="<b>🔰 JOIN ALL MOVIES 🔰.\n\nSORRY..! PLEASE JOIN ALL MOVIES CHANEL..!\nനിങ്ങൾക്ക് സിനിമ കിട്ടണമെങ്കിൽ ALL MOVIES ചാനെലിൽ ജോയിൻ ചെയ്യണം. എന്നാൽ മാത്രമേ എനിക് സിനിമ നിങ്ങൾക്ക് അയക്കാൻ സാധിക്കൂ..!\n സിനിമ ലഭിക്കാൻ താഴെകാണുന്ന ALL MOVIES എന്ന ബട്ടണിൽ അമർത്തുക അവിടെ കാണുന്ന ചാനെലിൽ ജോയിൻ ചെയ്ത ശേഷം വീണ്ടും START കൊടുക്കുക അപ്പൊൾ നിങ്ങൾക്കും BOT അക്ക്‌സസ് ലഭിക്കും..😁</b>",
                reply_markup=InlineKeyboardMarkup(
                    [ InlineKeyboardButton(text=" 💢 ALL MOVIES 💢 ", url="https://t.me/mlm_movie_1")]
              )
            )
            return
        except Exception:
            await update.reply_text(f"<b>This bot should be the admin on your update channel</b>\n\n<b>💢 ഈ ചാനലിൽ  @{UPDATE_CHANNEL} ബോട്ടിനെ അഡ്മിൻ ആക്. എന്നിട്ട് /start കൊടുക്</b>\n\n<b>🗣️ any Doubt @Mo_Tech_Group</b>")
            return  
    try:
        file_uid = update.command[1]
    except IndexError:
        file_uid = False
    
    if file_uid:
        file_id, file_name, file_caption, file_type = await db.get_file(file_uid)
        
        if (file_id or file_type) == None:
            return
        
        caption = file_caption if file_caption != ("" or None) else ("<code>" + file_name + "</code>")
        
        if file_type == "document":
        
            await bot.send_document(
                chat_id=update.chat.id,
                document = file_id,
                caption = caption,
                parse_mode="html",
                reply_to_message_id=update.message_id,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    '🔰 ALL MOVIES 🔰', url="https://t.me/mlm_movie_1"
                                )
                        ],
                        [
                            InlineKeyboardButton
                                (
                                    '🔰 NEW MOVIES 🔰', url="https://t.me/MLM_ROKES"
                                )
                        ]
                    ]
                )
            )

        elif file_type == "video":
        
            await update.bot.send_video(
                chat_id=update.chat.id,
                video = file_id,
                caption = caption,
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    '🔰 ALL MOVIES 🔰', url="https://t.me/mlm_movie_1"
                                )
                        ]
                    ]
                )
            )
            
        elif file_type == "audio":
        
            await update.bot.send_audio(
                chat_id=update.chat.id,
                audio = file_id,
                caption = caption,
                parse_mode="html",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton
                                (
                                    '🔰ALL MOVIES🔰', url="https://t.me/mlm_movie_1"
                                )
                        ]
                    ]
                )
            )

        else:
            print(file_type)
        
        return

    buttons = [[
        InlineKeyboardButton('⭕ MOVIE REQESTING GROUP', url='https://t.me/NEW_MLM_HD_MOVES')
    ],[
        InlineKeyboardButton('⭕ ALL MOVIES', url='https://t.me/mlm_movie_1'),
        InlineKeyboardButton('NEW UPDATES ⭕', url='https://t.me/mlm_movies_update')
    ],[
        InlineKeyboardButton('🔒 CLOSE 🔒', callback_data='close')
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TEXT.format(
                update.from_user.first_name),
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["help"]) & filters.private, group=1)
async def help(bot, update):
    buttons = [[
        InlineKeyboardButton('🏠 𝙷𝚘𝚖𝚎', callback_data='start'),
        InlineKeyboardButton('𝙰𝚋𝚘𝚞𝚝 🚩', callback_data='about')
    ],[
        InlineKeyboardButton('🔐 𝙲𝚕𝚘𝚜𝚎 🔐', callback_data='close')
    ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_TEXT,
        reply_markup=reply_markup,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )


@Client.on_message(filters.command(["about"]) & filters.private, group=1)
async def about(bot, update):
    
    buttons = [[
        InlineKeyboardButton('🏠 Home', callback_data='start'),
    ],[
        InlineKeyboardButton('Close 🔐', callback_data='close')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.ABOUT_TEXT,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        parse_mode="html",
        reply_to_message_id=update.message_id
    )
