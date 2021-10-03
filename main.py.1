import discord #pip install discord
import os
from discord.ext.commands import Bot
import wikipedia #pip install wikipedia



client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!w'):
        a_string = message.content
        new_string = a_string.replace ('!w ', '')
        
        str1 = wikipedia.search(new_string, results = 1) 
        if len(str1) == 0 :
            await message.channel.send('No article found')
        print(str1)
        str2=str1[0] 
        str3=f"https://en.wikipedia.org/wiki/{str2}" 
        print(str2) 
        #summary = wikipedia.summary(str2, sentences=5, auto_suggest=False)
        #url = wikipedia.page(str2, auto_suggest=False).url
        #await message.channel.send(url + '\n' +  summary)
        try:
            summary = wikipedia.summary(str2, sentences=5, auto_suggest=False)
        except wikipedia.DisambiguationError as err:
            await message.channel.send(err)
        else:
            url = wikipedia.page(str2, auto_suggest=False).url
            await message.channel.send(url + '\n' + summary)

client.run('#your token')
