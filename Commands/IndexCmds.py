#  Copyright (c) 2021 Yeetoxic

#Imports
import discord
from datetime import datetime
import pytz
from FlyingWienerOS.ServiceRequest import send_request
from FlyingWienerOS.FWVariables import Prefix, FWversion, tree, client, FWOS_Name, FWOS_Version, FWOS_Production_Date, BotAcronym


#Commands
def IndexCmds():
  #Help Cmd
  @tree.command(name='help', description='Gives a list of commands"')
  async def help(interaction):
          send_request()
          embed = discord.Embed(title="Commands:",description="//////////////////////////",color=0x2de639)
          embed.add_field(name=f"{Prefix}flyingwiener",value="The command where it all started...",inline=False)
          embed.add_field(name=f"{Prefix}changelog",value="Shows the current changelog for the bot!",inline=False)
          embed.add_field(name=f"{Prefix}bstats",value="Shows current FWB stats",inline=False)
          embed.add_field(name=f"{Prefix}stats",value="Server Specific Stats",inline=False)
          embed.add_field(name=f"{Prefix}memecmds",value="Gives a list of meme commands",inline=False)
          embed.add_field(name=f"{Prefix}help",value="Gives a list of commands",inline=False)
          embed.set_footer(text=f"FlyingWienerBot {FWversion} | Made By: Yeetoxic")
          await interaction.response.send_message(embed=embed)

  #Meme Cmds
  @tree.command(name='memecmds', description='Gives a list of meme commands"')
  async def MemeCmds(interaction):
          send_request()
          embed = discord.Embed(title="Meme Commands:",description="//////////////////////////",color=0x2de639)
          embed.add_field(name=f"{Prefix}rick",value="Summons the DEMON :O",inline=False)
          embed.add_field(name=f"{Prefix}propaganda",value="For use only in dire situations...",inline=False)
          embed.add_field(name=f"{Prefix}elbow",value="Elmo but cursed",inline=False)
          embed.add_field(name=f"{Prefix}catreview",value="Reviews cats",inline=False)
          embed.add_field(name=f"{Prefix}IMG",value="Random memes (pulls images from Reddit)",inline=False)
          embed.add_field(name=f"{Prefix}VID",value="Random Videos from an old deleted command.",inline=False)
          embed.add_field(name=f"{Prefix}bruh",value="random memes from an old deleted command.",inline=False)
          embed.add_field(name=f"{Prefix}height",value="guesses ur height, the bot is never wrong (trust)",inline=False)
          embed.set_footer(text=f"FlyingWienerBot {FWversion} | Made By: Yeetoxic")
          await interaction.response.send_message(embed=embed)


  #Bot stats Command
  @tree.command(name='bstats', description='shows current FWB stats"')
  async def bstats(interaction):
          send_request()
          TimeNow = datetime.now(pytz.timezone('America/Los_Angeles')).strftime("%m/%d/%Y %I:%M:%S %p %Z")
          bot = interaction.client.user
          SCount = len(client.guilds)
          SRCount = 76 - SCount
          SRCount_message = SRCount if SRCount > 0 else "**READY FOR VERIFICATION!**"
          embed = discord.Embed(title="**Current FWB Stats**", description=f"Generated: *{TimeNow}*",color=0x2de639)
          embed.set_thumbnail(url=bot.avatar)
          embed.add_field(name=f"---------------------------------------\n\nGENERAL INFO\n-------------",value="",inline=False)
          embed.add_field(name=f"Bot ID:",value=bot.id,inline=True)
          embed.add_field(name=f"Discord Version:",value=discord.__version__,inline=True)
    
          embed.add_field(name=f"---------------------------------------\n\nBOT INFO\n-------------",value="",inline=False)
          embed.add_field(name=f"Logged in as:",value=bot.name,inline=True)
          embed.add_field(name=f"Bot Acronym:",value=BotAcronym,inline=True)
          embed.add_field(name=f"Bot Version:",value=FWversion,inline=True)
    
          embed.add_field(name=f"---------------------------------------\n\nFWOS INFO\n-------------",value="",inline=False)
          embed.add_field(name=f"Bot OS:",value='"'+FWOS_Name+'"',inline=True)
          embed.add_field(name=f"Version:",value=FWOS_Version,inline=True)
          embed.add_field(name=f"Production Date:",value=FWOS_Production_Date,inline=True)

          embed.add_field(name=f"---------------------------------------\n\nServer INFO\n-------------",value="",inline=False)
          embed.add_field(name=f"Servers Required for Verification:",value=SRCount_message,inline=True)
          embed.add_field(name=f"Server Count:",value=len(client.guilds),inline=True)  
      
          embed.set_footer(text=f"FlyingWienerBot {FWversion} | Made By: Yeetoxic")
          await interaction.response.send_message(embed=embed)


  #Server stats Command
  @tree.command(name='stats', description='shows Server Specific Stats"')
  async def stats(interaction):
    send_request()
    TimeNow = datetime.now(pytz.timezone('America/Los_Angeles')).strftime("%m/%d/%Y %I:%M:%S %p %Z")
    embed = discord.Embed(title="**Server Specific Stats**", description=f"Generated: *{TimeNow}*",color=0x2de639)
    embed.set_thumbnail(url=interaction.guild.icon)
    embed.add_field(name = "Server Name:", value = interaction.guild.name, inline = False)
    embed.add_field(name = "Server ID:", value = interaction.guild.id, inline = False)
    embed.add_field(name = "User Count:", value = interaction.guild.member_count, inline = False)
    embed.add_field(name = "Channel Count:", value = len(interaction.guild.channels), inline = False)
    embed.add_field(name = "Server Owner:", value = interaction.guild.owner, inline = False)
    embed.set_footer(text=f"FlyingWienerBot {FWversion} | Made By: Yeetoxic")
    await interaction.response.send_message(embed=embed)
