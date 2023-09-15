#  Copyright (c) 2021 Yeetoxic

#Discord Imports
import discord

#Discord ext Imports
from discord.ext.commands import CommandNotFound
from discord.ext.commands import MissingRequiredArgument
from discord.ext.commands import MissingPermissions

#FlyingWienerOS Imports
from FlyingWienerOS.FWVariables import FWversion, client, Prefix, tree, token
from FlyingWienerOS.keep_alive import keep_alive
import FlyingWienerOS.OnReady

#Command Imports
from Commands.InnitCmds import InnitCmds
from Commands.OriginalCmds import OriginalCmds 
from Commands.IndexCmds import IndexCmds
from Commands.MemeCmds import MemeCmds


#-------------------------------------------------------
#FlyingWienerOS Essential Startup Functions
keep_alive()


#-------------------------------------------------------
#Error handler
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        return
    raise error

    if isinstance(error, MissingRequiredArgument):
        return
    raise error

    if isinstance(error, MissingPermissions):
        return
    raise error


#-------------------------------------------------------
#Custom Status
@client.event
async def on_ready():
  
    await client.change_presence(
        status=discord.Status.online,
        activity=discord.Game(f'Syncing...'))
    await tree.sync()
  
  
    await client.change_presence(
        status=discord.Status.online,
        activity=discord.Game(f'Starting...'))
    FlyingWienerOS.OnReady.OnReady()
    
    await client.change_presence(
        status=discord.Status.online,
        activity=discord.Game(f'FWB {FWversion} | {Prefix}help'))


#-------------------------------------------------------
#Commands
InnitCmds()
OriginalCmds()
IndexCmds()
MemeCmds()
  

#-------------------------------------------------------
#    DISCLAIMERS
#-----------------
#  This Bot was Made by Yeetoxic, pls don't steal my stuff.
#  Code for use by the SlimeLabs discord exclusive!
#-----------------

#-------------------------------------------------------
#Client Runtime (END OF THE LINE)
client.run(token)