#  Copyright (c) 2021 Yeetoxic

#imports
import discord
import time
from datetime import datetime
import pytz
from FlyingWienerOS.BotEvents import ServerList
from FlyingWienerOS.FWVariables import client, FWversion, FWOS_Name, FWOS_Version, FWOS_Production_Date, BotAcronym, clearConsole

#Ready Event
def OnReady():
    TimeNow = datetime.now(pytz.timezone('America/Los_Angeles')).strftime("%m/%d/%Y %I:%M:%S %p %Z")
    clearConsole()
    FBot = (client.user.name)
    FBID = (client.user.id)
    DVer = (discord.__version__)
    SCount = (str(len(client.guilds)))
    print('<-------=======+=======------->')
    print(f'===[Welcome to {FWOS_Name}!]===')
    print('<-------=======+=======------->')
    time.sleep(1)
    print('\n-------[GENERAL INFO]---------')
    print(f'Bot ID: {FBID}')
    print(f'Discord Version: {DVer}')
    print('------------------------------')
    time.sleep(1)
    print('\n---------[BOT INFO]----------')
    print(f'Logged in as: "{FBot}"')
    print(f'Bot Acronym: "{BotAcronym}"')
    print(f'Bot Version: {FWversion}')
    print('------------------------------')
    time.sleep(1)
    print('\n---------[FWOS INFO]----------')
    print(f'Bot OS: "{FWOS_Name}"')
    print(f'Version: {FWOS_Version}')
    print(f'Production Date: {FWOS_Production_Date}')
    print('------------------------------')
    time.sleep(1)
    print('\n--------[Server INFO]---------')
    print('Connected Servers:')
    print('- - - - - - - - - ')
    print('\n           Check "Servers.txt"! \n')
    print('- - - - - - - - - ')
    print(f'Server Count: {SCount}')
    print (f'Loaded: {TimeNow}')
    ServerList()