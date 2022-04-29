#bot.py - 봇 관리
import discord
from discord.ext import commands
from to import Token

bot=commands.Bot(command_prefix='ehe')

@bot.event
async def on_ready():
    print('로그인중입니다. ')
    print(f"봇={bot.user.name}로 연결중")
    print('연결이 완료되었습니다.')
    await bot.change_presence(status=discord.Status.online, activity=None)

@bot.command(aliases=[''])
async def ehe(ctx):
    await ctx.send('Ehe te NADAYO!!!!!')    
@bot.command(aliases=[' ehe ehe'])
async def stop_doing_that_shit(ctx):
    await ctx.send('그만해라.')
@bot.command(aliases=[' bwai'])
async def stop_doing_that_shit(ctx):
    await ctx.send(url='https://cdn.discordapp.com/attachments/857079818872553493/969222351612960798/unknown.png')
@bot.command()
async def 따라하기(ctx,*,text):
    await ctx.send(text)
bot.run(Token)

