#bot.py - 봇 관리
import discord
from discord.ext import commands
from to import Token
import requests
import json

my_jwt = "bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IktYMk40TkRDSTJ5NTA5NWpjTWk5TllqY2lyZyIsImtpZCI6IktYMk40TkRDSTJ5NTA5NWpjTWk5TllqY2lyZyJ9.eyJpc3MiOiJodHRwczovL2x1ZHkuZ2FtZS5vbnN0b3ZlLmNvbSIsImF1ZCI6Imh0dHBzOi8vbHVkeS5nYW1lLm9uc3RvdmUuY29tL3Jlc291cmNlcyIsImNsaWVudF9pZCI6IjEwMDAwMDAwMDAwMDA0OTcifQ.JwVQU-cdtyXpwFMJuZeRxPZb_pyz9JWY-2zZCwNwr2OaD2AbYSbHadZw8dIjO4b1f-BvmvEi0Xr6LDdnu0hWSZu3l1C7SIlf5IJPglJwtqPr2bTG2KVVjoq0SWmhxZkLNNuKBjXHG1ADGzem_3vtKnnbHkANBV8uZGzxfz3v-62bUMEAdKKdougJekJ-r22td_SPzv5jgpKlFAae1bHu2nYx7Q0Dz78pxWBnBLJsLCvs8enEFuYrAfD-IICDPntETTmSQjDOH23OkQJseVJnGfvzTyjcUvZO8d0M4-xv3p27D5E2tr9hUZyNnlDhxpncZ63FyMIT8FpUqM5hsPPDjA"
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
