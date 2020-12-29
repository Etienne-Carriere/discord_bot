import discord
import asyncio
import os

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if message.content.startswith('!helloprivate'):
            private = message.author
            person = message.author.display_name
            await private.send(f'Say helloprivate! {person} ')
        if message.content.startswith('!hellorole'):
            role = None
            person = message.author.display_name
            for r in self.guilds[0].roles:
                if r.name == 'Lannister':
                    role = r
                    break
            for member in role.members:
                print(member.name)
                await member.send(f'Say hellorole! it\'s {person}')
        if message.content.startswith('!hello'):
            channel = message.channel
            person = message.author.display_name
            await channel.send(f'Say hellopublic! {person} ')

intents = discord.Intents.all()
client = MyClient(intents=intents)
client.run(os.environ["DISCORD_KEY"])