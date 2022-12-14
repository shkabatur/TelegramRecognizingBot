import os
import telebot
from recognizing import parse_wav
from convert import convert_x_to_wav
from config import BOT_TOKEN


print("READY :)")
bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(content_types=['voice', 'video_note'])
def media_processing(message):
    # get file path and downlaod it
    if message.content_type == 'voice':
        file_info = bot.get_file(message.voice.file_id)
    elif message.content_type == 'video_note':
        file_info = bot.get_file(message.video_note.file_id)

    downloaded_file = bot.download_file(file_info.file_path)

    # extract exactry file name
    file_path = file_info.file_path.split('/')[1]
    file_name = file_path.split('.')[0]

    # write file on disk (needed for ffmpeg)
    with open(file_path, 'wb') as new_file:
        new_file.write(downloaded_file)

    # generate wav file name and write it on disk
    wav_file_path =  file_name + '.wav'
    convert_x_to_wav(file_path, wav_file_path)

    parsed_text = parse_wav(wav_file_path)
    parsed_text = ". ".join(parsed_text)

    os.remove(file_path)
    os.remove(wav_file_path)

    bot.send_message(message.chat.id, f"{message.from_user.username} говорит:\n\n \"{parsed_text}\"")


bot.infinity_polling()
