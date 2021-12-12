import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = "!", description = "Salam je suis crée par Duwa")

@bot.event
async def on_ready():
    print("C'est bon pelo je suis connecté, verifie par toi meme xD !")

    @bot.command()
    async def coucou(ctx):
        await context.send("Coucou !")

        @bot.command()
        async def serverInfo(ctx):
            server = ctx.guild
            number0fTextChannels = len(server.text_channels)
            number0fVoiceChannels = len(server.voice_channels)
            serverDescription = server.description
            number0fPerson = server.membre_count
            serverName = server.name
            message = f"Le serveur {serverName} contient {number0fPerson} personnes. \n La description du serveur {serverDescription}. \n Ce serveur possède {number0fTextChannels} salons écrit ainsiq que {number0fVoiceChannels} vocaux."
            await ctx.send(message) 

bot.run("")
