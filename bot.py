import discord
import responses


async def send_message(message, user_message, is_private):
    try:
        response = responses.get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)


def run_discord_bot():
    TOKEN = 'MTEwNTA5OTgyMDQ4NzY5MjM0OQ.GE0Lej.UYPNbIBuSHHVs5fZrKs8u4AsLZqNTeuhpCGElE'
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        if message.author != client.user and message.content == '🫡':
            await message.delete()
            await message.channel.send({message.author})
    client.run(TOKEN)
