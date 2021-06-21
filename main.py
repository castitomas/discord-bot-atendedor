with open('token.txt') as f:
    TOKEN = f.readline()

import discord
import random

client = discord.Client()

atender_user = ["boludo", "pelotudo", "huevos", "loco", "gil"]

frases_atender = [
    "Sos boludo y no tenés huevos.",
    "¿A vos quién te conoce?",
    "Tomatela te dije.",
    "Atiendo boludos."
]

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})') 


    if message.author == client.user:
        return

    #Lista comandos

    if user_message.lower() == '!comandos':
        response = f"""Lista de comandos: 
        !boludo --> Nivel de boludo.
        !juegos --> En el canal de juegos papu.
        !micreador --> ;) """
        await message.channel.send(response)
        return

    #Comando para el canal general

    if message.channel.name == 'general':
        if user_message.lower() == 'hola':
            await message.channel.send(f'Hola {username}')
            return
        elif user_message.lower() == '!boludo':
            response = f'Tu nivel de boludo es {random.randrange(10000)}!'
            await message.channel.send(response)
            return
        elif user_message.lower() == '!micreador':
            response = f'https://github.com/castitomas'
            await message.channel.send(response)
            return

    
    #Comando juegos

    if user_message.lower() == '!juegos':
        response = f'Sos boludo {username} y no tenés juegos'
        await message.channel.send(response)
        return

    #Respuesta aleatoria a cualquier palabra de atender_user

    if any(word in user_message for word in atender_user):
        await message.channel.send(random.choice(frases_atender))
        return

client.run(TOKEN)














