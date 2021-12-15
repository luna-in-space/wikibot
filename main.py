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

    if message.content.startswith('!w '):
        msg = message.content
        new_msg = msg.replace ('!w ', '')
        
        wikisearch = wikipedia.search(new_msg, results = 1) 
        if len(wikisearch) == 0 :
            await message.channel.send('No article found')
        print(wikisearch)
        wikisearch0=wikisearch[0] 
        url=f"https://en.wikipedia.org/wiki/{wikisearch0}" 
        print(wikisearch0) 
	#old way to find links, but bugged out upon disambiguation error
        #summary = wikipedia.summary(str2, sentences=5, auto_suggest=False)
        #url = wikipedia.page(str2, auto_suggest=False).url
        #await message.channel.send(url + '\n' +  summary)
        try:
            summary = wikipedia.summary(wikisearch0, sentences=1, auto_suggest=False)
        except wikipedia.DisambiguationError as err:
            await message.channel.send(err)
        else:
            url = wikipedia.page(wikisearch0, auto_suggest=False).url
            await message.channel.send('<' + url + '>\n' + summary)



    if message.content.startswith('!wk'):
        op = message.content
        nowk = op.replace ('!wk ', '')
        nospace = nowk.replace (' ', '_')
        wiktionary = ('https://en.wiktionary.org/wiki/' + nowk)
        
        await message.channel.send(nowk + "\n" +'<' +wiktionary + '>') 
client.run('token')
