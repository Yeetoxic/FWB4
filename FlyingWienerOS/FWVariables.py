#  Copyright (c) 2021 Yeetoxic

#Imports
import os
import discord
from discord import app_commands
from discord.ext import commands

#Editables
Prefix = '/'#DO NOT CHANGE!!!!
FWversion = "v4.1.6"
BotAcronym = "FWB"

#FWOS Info
FWOS_Name = "Wiener 23"
FWOS_Version = "v4.12.9"
FWOS_Production_Date = "04/06/23"

#Universal
token = os.environ['token']
intents = discord.Intents.default()
intents.members=True
discord.Clientbot = commands.Bot(command_prefix=Prefix,intents=intents,help_command=None,case_insensitive=True)
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


#Console Clear (OS COMMAND)
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)