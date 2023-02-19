from twitchio.ext import commands
from twitchio.client import Client
from dotenv import load_dotenv
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
        print("BOT: ", ctx.content)
    else:
        print(ctx.author.name)
    #print(ctx.content)
    #await bot.handle_commands(ctx)


'''@bot.command(name='test')
async def test_command(ctx):
    await ctx.send("this is a test response")


@bot.command(name='who')
async def get_chatters(ctx):
    chatters = await client.get_chatters('incompetent_ian')
    all_chatters = ' '.join(chatters.all)
    await ctx.send(f"In chat: {all_chatters}")'''


if __name__ == '__main__':
    bot.run()
