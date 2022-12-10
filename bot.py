#bot.py - 봇 관리
import discord
from discord.ext import commands
from to import Token

#명령어: ehe
bot=commands.Bot(command_prefix='ehe')
@bot.event
async def on_ready():
    print('로그인중입니다. ')
    print(f"봇={bot.user.name}로 연결중")
    print('연결이 완료되었습니다.')
    await bot.change_presence(status=discord.Status.online, activity=None)

#------------------- 명렁어 목록 -------------------
#페이몬 대답하기
@bot.command(aliases=[''])
async def ehe(ctx):
    await ctx.send('Ehe te NADAYO!!!!!')
#페이몬 움짤 보내기
@bot.command(aliases=['he'])
async def stop_doing_that_shit(ctx):
    await ctx.send('https://tenor.com/view/nandayo-gif-18919523')
#로아 닉네임 입력하면 정보띄워주기
#연동필요
#https://toramko.tistory.com/entry/python-%ED%8C%8C%EC%9D%B4%EC%8D%AC-requests-%EB%A1%9C-REST-API-%ED%98%B8%EC%B6%9C%ED%95%98%EA%B8%B0?category=867426
@bot.command(aliases=['Nickname'])
async def stop_doing_that_shit(ctx):
    await ctx.send('CharacterInfo')

#실행
bot.run(Token)
