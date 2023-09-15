#  Copyright (c) 2021 Yeetoxic

#imports
from FlyingWienerOS.FWVariables import client, FWversion, Prefix
  
#Bot Join message
@client.event
async def on_guild_join(guild):
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            await channel.send(f'Welcome to **FWB {FWversion}**! Do **{Prefix}help** for a list of commands!')
        break
    ServerList()

#Server Lister
def ServerList():
    SCount = (str(len(client.guilds)))
    f = open('Txts/Servers.txt', 'r+')
    f.truncate(0)
    f = open('Txts/Servers.txt', 'a')
    
    priority_servers = [721558492250636317, 949883650873372672, 961720228193140837]
    
    guilds = sorted(client.guilds, key=lambda x: x.id)
    
    f = f.write(f'Server Count: {SCount}' + "\n" + 'Connected Servers:' + "\n" + '- - - - - - - - - ' + "\n" + "\n")
    
    # Write the priority servers section
    f = open('Txts/Servers.txt', 'a')
    f = f.write('~Priority Servers:\n' + '- - - - - - - - - ' + "\n")
    for guild in guilds:
        if guild.id in priority_servers:
            Server = guild.name
            SerID = guild.id
            SerUsers = str(len(guild.members))
            
            f = open('Txts/Servers.txt', 'a')
            f = f.write(f'S-Name: "{Server}"' + "\n" + f'S-ID: {SerID}' + "\n" + f'S-Users: {SerUsers}' + "\n" + "\n")
    
    # Write the regular servers section
    f = open('Txts/Servers.txt', 'a')
    f = f.write('\n\n~Regular Servers:\n' + '- - - - - - - - - ' + "\n")
    for guild in guilds:
        if guild.id not in priority_servers:
            Server = guild.name
            SerID = guild.id
            SerUsers = str(len(guild.members))
            
            f = open('Txts/Servers.txt', 'a')
            f = f.write(f'S-Name: "{Server}"' + "\n" + f'S-ID: {SerID}' + "\n" + f'S-Users: {SerUsers}' + "\n" + "\n")
