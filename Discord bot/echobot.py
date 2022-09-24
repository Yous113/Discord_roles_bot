from email import message
import discord

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = discord.Client(intents=intents)

TOK_FILE = "token.txt"

def get_token():
  tokfile = open(TOK_FILE, 'r')
  token = tokfile.read()
  tokfile.close()
  return token

def reverse(s):
  return s[::-1]

@client.event
async def on_ready():
    print("Connected!")


@client.event
async def on_message(message):
    contents = message.content
    author = message.author.id


@client.event
async def on_raw_reaction_add(payload):
    message_id = payload.message_id
    if message_id == 1019925207412121600:
      guild_id = payload.guild_id
      guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)
      role = discord.utils.get(guild.roles, name = payload.emoji.name)
      if role is not None:
        member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
        if member is not None:
          await member.add_roles(role)
          print("done")
        else:
          print("member not found.")
          pass
      else:
        print("Role not found.")
        pass
    if message_id == 1021679077276532756:
      guild_id = payload.guild_id
      guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)
      if payload.emoji.name == "🎲":
        role = discord.utils.get(guild.roles, name = "Gaming")
      elif(payload.emoji.name == "📔"):
        role = discord.utils.get(guild.roles, name = "Reading")
      elif(payload.emoji.name == "🎙️"):
        role = discord.utils.get(guild.roles, name = "Streaming")
      elif(payload.emoji.name == "🖥️"):
        role = discord.utils.get(guild.roles, name = "Movies")
      elif(payload.emoji.name == "💽"):
        role = discord.utils.get(guild.roles, name = "Podcasts")
      
      if role is not None:
        member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
        if member is not None:
          await member.add_roles(role)
          print("done")
        else:
          print("member not found.")
          pass
      else:
       print("Role not found.")
       pass


@client.event
async def on_raw_reaction_remove(payload):
  message_id = payload.message_id
  if message_id == 1019925207412121600:
    guild_id = payload.guild_id
    guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)
    role = discord.utils.get(guild.roles, name = payload.emoji.name)
    if role is not None:
      member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
      if member is not None:
        await member.remove_roles(role)
        print("done")
      else:
        print("member not found.")
        pass
    else:
      print("Role not found.")
      pass
  if message_id == 1021679077276532756:
    guild_id = payload.guild_id
    guild = discord.utils.find(lambda g : g.id == guild_id, client.guilds)
    if payload.emoji.name == "🎲":
      role = discord.utils.get(guild.roles, name = "Gaming")
    elif(payload.emoji.name == "📔"):
      role = discord.utils.get(guild.roles, name = "Reading")
    elif(payload.emoji.name == "🎙️"):
      role = discord.utils.get(guild.roles, name = "Streaming")
    elif(payload.emoji.name == "🖥️"):
      role = discord.utils.get(guild.roles, name = "Movies")
    elif(payload.emoji.name == "💽"):
      role = discord.utils.get(guild.roles, name = "Podcasts")
      
    if role is not None:
      member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
      if member is not None:
        await member.remove_roles(role)
        print("done")
      else:
        print("member not found.")
        pass
    else:
     print("Role not found.")
     pass

  
     
token = get_token()
client.run(token)

