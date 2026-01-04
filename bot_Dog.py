import discord
import aiohttp

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Bot conectado como {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == "$cachorro":
        url_api = "https://dog.ceo/api/breeds/image/random"

        async with aiohttp.ClientSession() as session:
            async with session.get(url_api) as response:
                data = await response.json()
                imagem = data["message"]

        await message.channel.send(imagem)

client.run("SEU TOKEN")
