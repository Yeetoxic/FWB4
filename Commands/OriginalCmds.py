#  Copyright (c) 2021 Yeetoxic

#FlyingWienerOS Imports
from FlyingWienerOS.FWVariables import tree
from FlyingWienerOS.ServiceRequest import send_request

#Variables
V = open('Txts/ChangeLog.txt')
Ver = V.read()

#Commands
def OriginalCmds():
  @tree.command(name='flyingwiener', description='The command where it all started..."')
  async def flyingwiener(interaction):
        send_request()
        await interaction.response.send_message("Flying Wiener go brrrrrr")
  
  @tree.command(name='changelog', description='Shows the current changelog for the bot!"')
  async def ChangeLog(interaction):
        send_request()
        await interaction.response.send_message(Ver)