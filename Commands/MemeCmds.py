#  Copyright (c) 2021 Yeetoxic

#FlyingWienerOS Imports
from FlyingWienerOS.FWVariables import tree
from FlyingWienerOS.ServiceRequest import send_request
import requests
import discord
import random
from bs4 import BeautifulSoup as bs

#Variables
SubReddits = ["https://www.reddit.com/r/okbuddyretard/"]
SubReddits2 = ["https://www.reddit.com/r/okbuddyretard/","https://www.reddit.com/r/Catmemes/","https://www.reddit.com/r/memes/","https://www.reddit.com/r/funny/"]
url = random.choice(SubReddits)
headers = {"User-Agent": 'Mozilla/5.0'}
PHC = ["**5ft/5**","**5ft/6**","**5ft/7**","**5ft/8**","**5ft/9**","**5ft/10**","**5ft/11**","**6ft**","**6ft/1**","**6ft/2**","**6ft/3**","**6ft/4**","**6ft/5**","**6ft/6**","**6ft/7**","**6ft/8**","**6ft/9**","**6ft/10**","**6ft/11**","**7ft**","**7ft/1**","**7ft/2**","**7ft/3**","**7ft/4**","**7ft/5**","**7ft/6**","**7ft/7**","**7ft/8** (Damn u is tall)"]
starter_encouragements = [
    "https://www.youtube.com/watch?v=2RlTqFtdlH8",
    "https://www.youtube.com/watch?v=PFkju1-0lZI",
    "https://www.youtube.com/watch?v=s4CdsxyTLuA",
    "https://www.youtube.com/watch?v=uubHtO21J_s",
    "https://www.youtube.com/watch?v=ZokeA2lKB6o",
    "https://www.youtube.com/watch?v=vVXvHNxoBoI",
    "https://www.youtube.com/watch?v=A0LFmGUTsJ8"
]
Cursed_IMGs = [
    "https://media.discordapp.net/attachments/755835663479341266/831262138378354688/Gato_Sexo.png",
    "https://cdn.discordapp.com/attachments/755835663479341266/831262680550473738/THREAT.jpg",
    "https://media.discordapp.net/attachments/755835663479341266/831262775825006672/TANK.jpg",
    "https://media.discordapp.net/attachments/755835663479341266/831262878572609577/searching...png",
    "https://media.discordapp.net/attachments/755835663479341266/831262920918433812/Rick_but_worse.jpg?width=600&height=586",
    "https://media.discordapp.net/attachments/755835663479341266/831262992968187964/Pikachu_except_gud.png?width=990&height=240"
]
Elbow_IMGs = [
    "https://media.discordapp.net/attachments/755835663479341266/831264406943039538/CwC5L0-UEAAMcMe.jpg?width=779&height=586",
    "https://cdn.discordapp.com/attachments/755835663479341266/831265199243264040/ae1581886e3f7a26969fcf1b5c5f7554.png",
    "https://cdn.discordapp.com/attachments/755835663479341266/831265238879305728/81416eda7c733e8562b4055d7359de3c.jpg",
    "https://cdn.discordapp.com/attachments/755835663479341266/831265536653393990/5b391103ca259b755312c5bbbeeca0c0.jpg",
    "https://cdn.discordapp.com/attachments/755835663479341266/831265756901670922/sxe4zdoy9ky21.png",
    "https://media.discordapp.net/attachments/755835663479341266/831266237085515797/aargtlit1zz31.jpg?width=330&height=587",
    "https://cdn.discordapp.com/attachments/755835663479341266/831266402899066930/artworks-000554814903-voqlqv-t500x500.jpg"
]
Cat_IMGs = [
    "https://tenor.com/view/cat-kitty-kitty-review-review-of-cat-cat-review-gif-21098978",
    "https://tenor.com/view/kitty-review-kittyreview-cat-squishy-gif-21044823",
    "https://tenor.com/view/kitty-review-kitty-review-cat-gif-21086233",
    "https://tenor.com/view/kitty-review-cat-kitty-review-gif-20973774",
    "https://tenor.com/view/cat-review-eating-bad-garbage-gif-20951259",
    "https://tenor.com/view/kitty-review-cat-kitty-review-gif-20973783",
    "https://tenor.com/view/kitty-review-kitty-review-cat-dance-gif-21086436",
    "https://tenor.com/view/plus-kitty-review-kitty-cat-meme-gif-20796773",
    "https://tenor.com/view/kitty-review-kitty-cat-meme-funny-gif-20978803",
    "https://tenor.com/view/kitty-review-kitty-cat-review-gif-20973771",
    "https://tenor.com/view/kitty-review-cat-review-gif-21140551",
    "https://tenor.com/view/kitty-review-weird-cat-cat-review-review-of-cat-kitty-gif-21098907",
    "https://tenor.com/view/kitty-review-cat-kitty-review-stanky-gif-21071465",
    "https://tenor.com/view/kitty-review-kitty-review-cat-sleep-gif-21086446",
    "https://tenor.com/view/kitty-review-gif-21031795",
    "https://tenor.com/view/kitty-cat-this-is-going-fucking-gif-21101497",
    "https://tenor.com/view/kitty-review-cat-review-gif-21140352",
    "https://tenor.com/view/kitty-review-kitty-review-cat-stealth-gif-21142091",
    "https://tenor.com/view/kitty-review-cat-review-gif-21140330",
    "https://tenor.com/view/kitty-review-kitty-ballin-kitty-review-cat-gif-21145619",
    "https://tenor.com/view/kitty-review-cat-kitty-review-gif-20973777",
    "https://tenor.com/view/digley-scuff-gif-20939313"
]

#Meme Grabber
def return_image_and_title(url, headers):
    page = requests.get(url, headers=headers)
    if page.status_code == 200:
        soup = bs(page.text, "html.parser")
        
        # Extract post title
        title_tag = soup.select_one('h3[class="_eYtD2XCVieq6emjKBH3m"]')
        if title_tag:
            title = title_tag.get_text()
        else:
            title = None
        
        # Extract post image URL
        img_tag = soup.select_one('img[alt="Post image"]')
        if img_tag is None:
            return None, None, None
        img_url = img_tag['src']
                
        # Extract subreddit name
        subreddit_name = url.split("/r/")[1].split("/")[0]

        return title, img_url, subreddit_name
    else:
        return None, None, None

#Commands
def MemeCmds():
  @tree.command(name='rick', description='Summons the DEMON :O"')
  async def rick(interaction):
          send_request()
          await interaction.response.send_message("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
  
  @tree.command(name='propaganda', description='For use only in dire situations..."')
  async def propaganda(interaction):
          send_request()
          await interaction.response.send_message("https://www.youtube.com/watch?v=4UrYHrELE5Y")
  
  @tree.command(name='elbow', description='Elmo but cursed')
  async def elbow(interaction):
          send_request()
          await interaction.response.send_message(random.choice(Elbow_IMGs))
  
  @tree.command(name='catreview', description='Reviews cats')
  async def catreview(interaction):
          send_request()
          await interaction.response.send_message(random.choice(Cat_IMGs))
  
  @tree.command(name='img', description='Random memes (pulls images from various subreddits)')
  async def IMG(interaction):
      print("Starting IMG command...")
      try:
          await interaction.response.defer()
          send_request()
          print("Request sent!")
          title, img_url, subreddit_name = return_image_and_title(url, headers)
          print("Title, img_url, and subreddit_name obtained!")
          if title and img_url and subreddit_name:
              embed1 = discord.Embed(title=f"**r/{subreddit_name}**", description=f"{title[:50]}{'...' if len(title) > 50 else ''}",color=0x2de639)
              embed1.set_image(url=f"{img_url}")
              print("Sending Meme!")
              if interaction.response.is_done():
                  print("Interaction ready!")
                  await interaction.response.send_message(embed=embed1)
          else:
              embed2 = discord.Embed(title="**Having trouble connecting to Reddit services! Try again later!**", description="",color=0xc70000)
              print("Sending Error!")
              if interaction.response.is_done():
                  print("Interaction 2 ready!")
                  await interaction.response.send_message(embed=embed2)
      except Exception as e:
          print(e)


  
  @tree.command(name='vid', description='Random Videos from an old deleted command.')
  async def VID(interaction):
          send_request()
          await interaction.response.send_message(random.choice(starter_encouragements))
  
  @tree.command(name='bruh', description='random memes from an old deleted command.')
  async def bruh(interaction):
          send_request()
          await interaction.response.send_message(random.choice(Cursed_IMGs))
  
  @tree.command(name='height', description='guesses ur height, the bot is never wrong (trust)')
  async def height(interaction):
        send_request()
        if interaction.user.id == 463901590039035905:
          await interaction.response.send_message('Your Height is: **2ft/4**, LMAO fugin shortass')
        else:
          Height = random.choice(PHC)
          await interaction.response.send_message(f'Your Height is: {Height}')