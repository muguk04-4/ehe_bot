#bot.py - 봇 관리
import discord
from discord.ext import commands
#여기 수정해야됨 토큰 못불러오는중
from .to import Token

#명령어: / (강제임)
bot=commands.Bot(command_prefix='/')

@bot.event
async def on_ready():
    print('로그인중입니다. ')
    print(f"봇={bot.user.name}로 연결중")
    print('연결이 완료되었습니다.')
    await bot.change_presence(status=discord.Status.online, activity=None)

#------------------- 명렁어 목록 -------------------
#페이몬 대답하기
@commands.command(aliases=['ehe'])
async def eheyo(ctx):
    await ctx.send("Ehe te NADAYO!!!!!")
#페이몬 움짤 보내기
@commands.command(aliases=['ehehe'])
async def stop_doing_that_shit(ctx):
    await ctx.send('https://tenor.com/view/nandayo-gif-18919523')
#로아 닉네임 입력하면 정보띄워주기

#실행
bot.run(Token)
