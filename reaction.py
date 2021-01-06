from discord.ext import commands

client = commands.Bot(command_prefix = '.')
CLIENT_TOKEN = 'Nzk1NzM2MzI4NjMyMjcwODk5.X_NtNA.GAfYiBJ6vt_eq41bAqyE1a3i1pA'
BOT_USER_ID = 795736328632270899
ALLOWED_CHANNELS = [792940265873997885, 792800988007759892]

@client.event
async def on_ready():
    print('Bot initialized.')

reactions = {"0️⃣": 0, "1️⃣": 1, "2️⃣": 2, "3️⃣": 3, "4️⃣": 4, "5️⃣": 5}


@client.event
async def on_message(message):
    if message.channel.id not in ALLOWED_CHANNELS:
        return
    for attachment in message.attachments:
        if attachment.filename.endswith('.jpg') or attachment.filename.endswith('.png') or attachment.filename.endswith('.jpeg'):
            await message.channel.send("Score: ...")
            for reaction in reactions.keys():
                 await message.add_reaction(reaction)

async def fetch_message(channel_id, message_id):
    channel = client.get_channel(channel_id)
    message = await channel.fetch_message(message_id)
    return message

async def avoid_double_vote(payload):
    if payload.channel_id not in ALLOWED_CHANNELS:
        return
    if payload.user_id == BOT_USER_ID:
        return
    message = await fetch_message(payload.channel_id, payload.message_id)
    user  = await client.fetch_user(payload.user_id)
    for reaction in message.reactions:
        reaction_user_ids = [user.id for user in await reaction.users().flatten()]
        if reaction.emoji in reactions and \
         reaction.emoji != payload.emoji.name and \
         payload.user_id in reaction_user_ids:
            print("Removing...")
            await reaction.remove(user)

async def reaction_add_remove(payload):
    if payload.channel_id not in ALLOWED_CHANNELS:
        return
    if payload.user_id == BOT_USER_ID:
        return
    global msg_media
    message = await fetch_message(payload.channel_id, payload.message_id)
    contador = 0
    soma = 0
    for reaction in message.reactions:
        i = reactions.get(reaction.emoji, -1)
        # if emoji is not on the list, go to next emoji
        if i == -1:
            continue
        contador = reaction.count - 1 + contador
        soma = (reaction.count-1)*i+soma
    if contador > 0:
        new_post = "**Score: %.2f**" % (soma / contador)

        # Edit message right after the picture post
        channel = client.get_channel(payload.channel_id)
        msgs_after = await channel.history(limit=1, after=message).flatten()
        if len(msgs_after) > 0:
            await msgs_after[0].edit(content=new_post)


@client.event
async def on_raw_reaction_add(payload):
    await avoid_double_vote(payload)
    await reaction_add_remove(payload)


@client.event
async def on_raw_reaction_remove(payload):
    await reaction_add_remove(payload)

client.run(CLIENT_TOKEN)
