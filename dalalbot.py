# Python 3
import discord
# from google.cloud import translate_v2 as tl
from discord.ext import commands
import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv("DALAL_TOKEN")

client = discord.Client()
bot = commands.Bot(command_prefix="!")
# translate_client = tl.Client()

game = discord.Game("with your mom")

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')
    await client.change_presence(status=discord.Status.idle, activity=game)

#     for guild in client.guilds:
#         for channel in guild.channels:
#             if channel.name == "information":
#                 info = """
# **WELCOME TO DALALSMP!**
 
# This is an SMP made for Vibgyor High! Yes, the school sucks but Minecraft doesn't!
 
# This minecraft server is a whitelisted pure vanilla server with no plugins.
# To get into the whitelist, you have to head over to #bot-commands and type !apply whitelist
# You will have to fill out a form. After a couple hours (anywhere from 1 to 48), we will accept or decline your application.
# If you get denied, you can reapply in 3 days. Else, congratulations! You are part of our community!
 
# *About the server*:
# - The IP is dalal.netherrealm.gq and PORT is 19132.
# - You will have to apply for the whitelist to play.
# - Once your application gets accepted, you can hop on the server and play!
# - There are rules #rules
# - If you don't follow them, you'll 100% get banned.
# - Backups are taken once per hour.
# - Donations will be accepted once there is a proper store.
# - Thanks for playing!
# """
#                 await channel.send(info)

#     for guild in client.guilds:
#         for channel in guild.channels:
#             if channel.name == "rules":
#                 rules = """
# **RULES**
 
# **Server Rules**:
 
# *Gameplay related rules*:
# 1. Spawn is spawn. No building is allowed within the coordinates x:100 and z:100. (You can see your coordinates at the top left labelled Position. The first and last numbers are what x and z are. The middle is y.)
 
# 2. PVP (Player vs Player) or hitting other players is not allowed, unless both parties are okay with it. You CANNOT spawn kill, kill or trap innocent players who have no interest in fighting you.
 
# 3. No combat-logging. If you have agreed to a fight, you can't just chicken out and leave the game without finishing. If you win, well and good. If you lose, better luck next time. Combat logging is just bad sportsman ship.
 
# 4. ABSOLUTELY NO GRIEFING. If a player has built something, you can't TOUCH it without their approval. If its in your land (more about land claiming later), you can get it removed by contacting us.
 
# 5. No laggy mob farms
 
# 6. Keep it family friendly. Make sure there are no signs, books or structures that violate this rule. If you do see one, take a screenshot of it and then feel free to destroy it. Please take a screenshot before and after its demise and send it to us #contact-staff
 
# 7. No modifications that give you an advantage over other players (like xray or hacks). Night vision packs are allowed.
 
# 8. Do use your common sense. Don't try to bypass these rules. We can ban you for violating an unwritten rule.
 
# *Chat related rules*:
# 1. No swearing. Hey, we're kids after all!
 
# 2. No cyberbullying. We have ZERO tolerance for cyberbullying
 
# 3. No advertising.
 
# **Discord rules**:
# 1. No swearing
 
# 2. All commands have to be executed in !bot-commands (except !timed-message)
 
# 3. No advertising
 
# 4. No cyberbullying
 
# 5. Do use your common sense. Don't try to bypass these rules. We can ban you for violating an unwritten rule.
 
# """
#                 await channel.send(rules)

#     for guild in client.guilds:
#         for channel in guild.channels:
#             if channel.name == "contact-staff":
#                 contact_staff = """
# **How to contact staff?**
 
# For sending screenshots: COMING SOON
# For immediate contact: Aarnav Pai, 8B or Neel Susmith, 8B
 
# Other ways: EMAIL: netherrealmmcs@gmail.com
 
# Report Players: COMING SOON
# Staff Application: COMING SOON
 
# """
#                 await channel.send(contact_staff)

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f"""Hello {member.name}, welcome to NetherRealm!
**To connect to the server, use the IP: pe.netherrealm.gq PORT: 19132**
Website: http://netherrealmpe.gq/
        """
    )
    await member.dm_channel.send(
        f'Also, don\'t forget to follow the rules in #rules, or you get banned'
    )
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    with open("logs.txt", 'a') as f:
        f.write(f"{message.channel}: {message.author}: {message.author.name}: {message.content}\n")
    f.close()
    
    if message.content.lower() == "!ip":
        ipGET = requests.get("http://ip-api.com/json")
        ip = json.loads(ipGET.content)["query"]
        await message.channel.send("**IP: dalal.netherrealm.gq\nPORT: 19132**\nIf the above IP does not work, use " + ip)
        
    if message.content.lower() == "thanks dalal bot" or message.content.lower() == "thanks dalalbot":
        await message.channel.send("You're welcome!")
    
    if message.content.lower() == "!website":
        await message.channel.send("netherrealmpe.gq")
    
    if message.content[0:10] == "!announce ":

        for guild in client.guilds:
            for member in guild.members:
                for role in member.roles:
                    if role.name == "ADMIN":
                        for guild in client.guilds:
                            for channel in guild.channels:
                                if channel.name == "announcements":
                                    await channel.send(message.content[10::])
                                    await message.channel.send("Announced!")
                                    await message.channel.purge(limit=2)
        
    if message.content[0:14] == "!timedmessage ":
        for guild in client.guilds:
            for member in guild.members:
                for role in member.roles:
                    if role.name == "VIP":
                        try:
                            # print(message.content[message.content.find("(") + 1:message.content.find(")")])
                            time = int(message.content[message.content.find("(") + 1:message.content.find(")")])
                            await message.channel.purge(limit=1)
                            await message.channel.send(f"**THIS MESSAGE WILL DELETE AFTER {time} SECONDS!**\n {message.content[message.content.find(')') + 2::]}", delete_after=time)
                        except Exception as e:
                            await message.channel.send("Command failed to execute! Check if you're using the correct syntax!")

    # if message.content[0:14] == "!sendmessage (":
    #     for guild in client.guilds:
    #         for member in guild.members:
    #             for role in member.roles:
    #                 if role.name == "ADMIN":
    #                     channel_name = message.content[message.content.find("(") + 1:message.content.find(")")]
    #                     for guild in client.guilds:
    #                         for channel in guild.channels:
    #                             if channel.name == channel_name:
    #                                 await channel.send(message.content.find(")") + 2)
    #                 else:
    #                     await message.channel.send("You can't execute that command!")

    if message.content[0:13] == "!sendmessage ":
        for guild in client.guilds:
            for member in guild.members:
                for role in member.roles:
                    if role.name == "ADMIN":
                        await message.channel.purge(limit=1)
                        await message.channel.send(message.content[13::])

    if message.content == "!help" or message.content == "help":
        help_msg = """**---NetherRealm Discord Help---**

*Commands:*
- !ip: Get the ip
- !website: Get the website
- !timedmessage (<time>) <message>: Send a message that will self destruct in <time> seconds!

Rules: #rules
Announcements: #announcements
Website: http://netherrealmpe.gq
IP: dalal.netherrealm.gq | PORT: 19132
        """
        await message.channel.send(help_msg)

    if message.content == "!purge":
        for guild in client.guilds:
            for member in guild.members:
                for role in member.roles:
                    if role.name == "ADMIN":
                        await message.channel.purge(limit=1000)

client.run(token)
