from discord.ext import commands

client = commands.Bot(command_prefix = '.')
CLIENT_TOKEN = 'Nzk1NzM2MzI4NjMyMjcwODk5.X_NtNA.GAfYiBJ6vt_eq41bAqyE1a3i1pA'

@client.event
async def on_ready():
    print('Bot initialized.')

reactions = {"0️⃣": 0, "1️⃣": 1, "2️⃣": 2, "3️⃣": 3, "4️⃣": 4, "5️⃣": 5}

@client.event
async def on_message(message):
    # if message.channel.id == 792940265873997885:
    for attachment in message.attachments:
        if attachment.filename.endswith('.jpg') or attachment.filename.endswith('.png') or attachment.filename.endswith('.jpeg'):
            await message.channel.send("Score: ...")
            for reaction in reactions.keys():
                 await message.add_reaction(reaction)



async def fetch_message(channel_id, message_id):
    channel = client.get_channel(channel_id)
    message = await channel.fetch_message(message_id)
    return message

async def reaction_add_remove(payload):
    global msg_media
    message = await fetch_message(payload.channel_id, payload.message_id)
    contador = 0
    soma = 0
    for reac in message.reactions:
        i = reactions.get(reac.emoji, -1)
        # se o emoji nao eh da nossa lista, vai para o proximo emoji
        if i == -1:
            continue
        print("Emoji: ", i)
        contador = reac.count - 1 + contador
        soma = (reac.count-1)*i+soma
    if contador > 0:
        new_post = "**Score: %.2f**" % (soma / contador)
        channel = client.get_channel(payload.channel_id)
        msgs_after = await channel.history(limit=1, after=message).flatten()
        await msgs_after[0].edit(content=new_post)

    print("Numero de votos: ", contador)


@client.event
async def on_raw_reaction_add(payload):
    await reaction_add_remove(payload)


@client.event
async def on_raw_reaction_remove(payload):
    await reaction_add_remove(payload)

client.run(CLIENT_TOKEN)
