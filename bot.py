import discord
from decouple import config

client = discord.Client()


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('/cronograma'):
        await message.channel.send(f'Olá {message.author.name}! Segue o cronograma da semana:',
                                   file=discord.File("cronograma.txt"))

TOKEN = config('TOKEN')
client.run(TOKEN)
