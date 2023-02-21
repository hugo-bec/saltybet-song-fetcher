from twitchio.ext import commands
from twitchio.client import Client
from dotenv import load_dotenv
from datetime import date, datetime
import os

load_dotenv()


bot = commands.Bot(
    irc_token=os.environ['TMI_TOKEN'],
    client_id=os.environ['CLIENT_ID'],
    nick='tintingaisongfetcher',
    prefix='!',
    initial_channels=['saltybet'],
)


client = Client(
    client_id=os.environ['CLIENT_ID'],
    client_secret=os.environ['CLIENT_SECRET'],
)


@bot.event
async def event_message(ctx):
    if ctx.author.name == "waifu4u":
        message = ctx.content
        if message[:7] == "wtfSalt":
            today_str = date.today().strftime("%Y-%m_%d")
            now_str = datetime.now().strftime("%Y-%m-%d_%H:%M")
            song_history = now_str + " " + message[10:]
            path_folder = "/var/www/html/twitch-bot/history-saltysongs/"
            f = open(path_folder + "saltysongs_" + today_str + ".txt", "a")
            f.write(song_history + "\n")
            f.close()
            #print("song saved !")
        #if ctx.content
        #print("BOT: ", ctx.content)


if __name__ == '__main__':
    bot.run()
