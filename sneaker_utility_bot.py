import discord
import time
#TITLE : Discord Sneaker Resell Utility Bot
#NAME : Nicolas De Jesus
#YEAR: 2
TOKEN = 'OTY4Mjg2ODEyNzM5MDc2MjE2.YmcpXg.H0uUbxHu9R_6QMQ2bjILSPessyw' #authorization key for bot to perform functions

client = discord.Client()
@client.event
async def on_ready(): #logs the bot into the server
    print("{0.user} has been initialized".format(client))

@client.event
async def on_message(message): #this function logs all user + bot messages
    username = str(message.author).split("#")[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print("{}, {}, {}".format(username, user_message, channel))

    if message.channel.name == "commands": #makes sure the bot only works in one channel
        if user_message.lower() == "!weekly": #prints a list of the sneaker releases in the first week of may, plus their estimated resell prices
            await message.channel.send("```css\n [Week 1 of May 2022]```"
                                       "```yaml\n▷May 04:\n◦Nike Dunk Low 'Fossil Rose' - Retail: $110 \n  Est Resell: $150"
                                       "\n▷May 05:\n◦Nike Dunk Low 'Court Purple' - Retail: $110 \n  Est Resell: $190"
                                       "\n◦Nike Dunk Low 'Next Nature' - Retail: $110 \n  Est Resell: $200"
                                       "\n◦Nike Dunk Low 'Animal' - Retail: $110 \n  Est Resell: $180"
                                       "\n◦Nike Dunk High 'Pink Prime' - Retail: $115 \n  Est Resell: $180"
                                       "\n▷May 07:\n◦Nike Air Max 1 'Pink Prime' - Retail: $150 \n  Est Resell: $200```")
            return

        elif user_message.lower()== "!mosthyped": #prints a statement regarding the most hyped sneaker of may
            await message.channel.send("Are you ready to hear what the most hyped sneaker is of the month {}!?".format(username))
            await message.channel.send("The **Off White x Nike Air Force 1 Mid** is the shoe everyone is after in the month of may!")
            return

        elif user_message.lower()== "!fees": #prints the amount of fees each service takes for selling on their platform
            await message.channel.send("```css\n [Fees]```"
                                       "\n```md\n [StockX] = 12.5% "
                                       "\n [eBay] = 8% if sale > $100"
                                       "\n [GOAT] = 9.5%"
                                       "\n [FlightClub] = 9.5% + 2.9% 'cashout fee'```")
            return


client.run(TOKEN)