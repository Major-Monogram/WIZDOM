import discord
from discord import Intents
from keep_alive import keep_alive
coco = input("Enter here: ")
coco = str(coco)
intents = Intents.default()
intents.messages = True
intents.reactions = True

bot = discord.Client(intents=intents)

verified_role_id = 1156611742789541959  # Replace with your verified role ID
verification_channel_id = 1209554471764492338  # Replace with your verification channel ID

async def send_verification_message_with_reactions(channel):
    embed = discord.Embed(
        title="Verification",
        description="React with ✅ to get verified!",
    )
    message = await channel.send(embed=embed)
    return message

# Reaction handler
@bot.event
async def on_reaction_add(reaction, user):
    if (
        reaction.message.channel.id == verification_channel_id
        and reaction.emoji == "✅"
        and user != bot.user
        and reaction.message.author == bot.user  # Check if message is sent by the bot
    ):
        verified_role = user.guild.get_role(verified_role_id)
        if verified_role:
            try:
                await user.add_roles(verified_role)
                await reaction.message.channel.send(f"{user.mention} has been verified!")
            except discord.Forbidden:
                await reaction.message.channel.send("Verification failed. I don't have the permissions to assign roles.")
        else:
            await reaction.message.channel.send("Verification failed. Verified role not found.")

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')

    verification_message = await send_verification_message_with_reactions(bot.get_channel(verification_channel_id))
    await verification_message.pin()

keep_alive()
bot.run(coco)
