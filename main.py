import os
import discord
import random
import string
from discord.ext import commands
os.system("cls")
prefix = "!"
characters = string.ascii_letters + string.digits
photos = commands.Bot(prefix, self_bot=True)
photos.remove_command("help")
token = "token-here"
print(f" > Usage : {prefix}photo [photo-url] or {prefix}other [photo-url]")
links = ["https://discord.com","https://www.minecraft.net"] #add your links here or just add one if you want it to be the same everytime
@photos.command()
async def photo(ctx,photolink): 
    await ctx.message.delete()
    randcolor = random.randint(0x000000, 0xFFFFFF)
    embed=discord.Embed(color=randcolor)
    link = random.choice(links)
    embed.set_image(url=photolink)
    await ctx.send(content=f"<{link}>",embed=embed)
@photos.command()
async def other(ctx,photolink):
    await ctx.message.delete()
    randcolor = random.randint(0x000000, 0xFFFFFF)
    embed=discord.Embed(color=randcolor)
    embed.set_image(url=photolink)
    urlstr =  "".join(random.choice(characters) for xd in range(5)) #just so you get a string on the end of your url, some of them look more convincing
    link = random.choice(links)
    await ctx.send(content=f"<{link}/{urlstr}>",embed=embed)
photos.run(token, bot=False)
