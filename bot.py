# token-  MTA1ODQ0MTUxMDk1NTI3NDMzMA.GEbK2w.cCcoTturqserYLhpsuGbT9gfW736iV6vqGdy9k

import discord

# Set up the intents for the bot
intents = discord.Intents.default()
intents.members = True
intents.messages = True

# Create the Discord client
client = discord.Client(intents=intents)

# Define the character stats, abilities, and items for the RPG game
# You may want to create classes or data structures to represent these elements
character_stats = {
    "strength": 10,
    "dexterity": 10,
    "intelligence": 10
}

abilities = ["fireball", "heal", "shield"]

items = ["health potion", "mana potion"]

# Define an event handler for when the bot is ready
@client.event
async def on_ready():
    print("The bot is ready!")

# Define an event handler for when a message is sent
@client.event
async def on_message(message):
    # Check if the message is "!start"
    if message.content == "!start":
        # Generate a mention for the user who sent the message
        mention = message.author.mention
        # Send a message to the channel welcoming the user to the game
        await message.channel.send(f"{mention}, welcome to Hex RPG! Get ready to embark on an epic adventure filled with danger and adventure.")

# Run the bot
client.run("MTA1ODQ0MTUxMDk1NTI3NDMzMA.GEbK2w.cCcoTturqserYLhpsuGbT9gfW736iV6vqGdy9k")
