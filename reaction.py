from config import *
from discord.ext import commands


client = commands.Bot(command_prefix = '$')

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
#get message
    message = await fetch_message(payload.channel_id, payload.message_id)
#get user
    user  = await client.fetch_user(payload.user_id)
#itterate in message reactions
    for reaction in message.reactions:
        reaction_user_ids = []
        for user in await reaction.users().flatten():
            reaction_user_ids.append(user.id)
#if reaction emoji is not on the hardcoded emoji list, continue
        if reaction.emoji not in reactions:
            continue
#if reaction being itterated is the same as the one user clicked to initiate event (theoratically impossible), continue
        if reaction.emoji == payload.emoji.name:
            continue
#if the user that initiated the event is in the list of users of this reaction
        if payload.user_id in reaction_user_ids:
            print(f"Removing {reaction.emoji} reaction from {payload.member.name} in message {message.id}.")
            await reaction.remove(user)

async def reaction_add_remove(payload):
    if payload.channel_id not in ALLOWED_CHANNELS:
        return
    if payload.user_id == BOT_USER_ID:
        return
    message = await fetch_message(payload.channel_id, payload.message_id)
    counter = 0
    sum = 0
    for reaction in message.reactions:
        i = reactions.get(reaction.emoji, -1)
# if emoji is not on the list, go to next emoji
        if i == -1:
            continue
        counter = reaction.count - 1 + counter
        sum = (reaction.count-1)*i+sum
    if counter > 0:
        new_post = f"**Score: %.1f/{len(reactions)-1}**" % (sum / counter)

# Edit message right after the picture post
        channel = client.get_channel(payload.channel_id)
        msgs_after = await channel.history(limit=5, after=message).flatten()
        for msg in msgs_after:
            if msg.author.id == BOT_USER_ID:
                await msg.edit(content=new_post)
                print(f"Edited message {msg.id}. New message: {new_post}")
                break
            print("\n")

@client.event
async def on_raw_reaction_add(payload):
    await avoid_double_vote(payload)
    await reaction_add_remove(payload)

@client.event
async def on_raw_reaction_remove(payload):
    await reaction_add_remove(payload)

client.run(CLIENT_TOKEN)
