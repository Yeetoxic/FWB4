#  Copyright (c) 2021 Yeetoxic

#FlyingWienerOS Imports
from FlyingWienerOS.FWVariables import tree
from FlyingWienerOS.ServiceRequest import send_request


#-------------------------------------------------------
#Commands
# Ping command
def InnitCmds():
  @tree.command(name='ping', description='Responds with "Pong!"')
  async def ping(interaction):
      send_request()
      await interaction.response.send_message('Pong!')
  
  # Echo command
  @tree.command(name='echo', description='A large cave!')
  async def echo(interaction, *, message: str):
      send_request()
      await interaction.response.send_message(message)