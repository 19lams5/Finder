import discord


def get_embed(page=0):

    page_limit = 3

    if page == 0:
        embed = discord.Embed(
            title="Bot Usage Instructions",
        )
        embed.add_field(
            name="AO3 Searching:",
            value="`ao3 [fic name]` or `ao3 [fic name] series` \
            \n **Example:**\n1) `ao3 rogue knight` \n2) `ao3 prince of slytherin series`"
        )

        embed.add_field(
            name="FFN Searching:",
            value="`ffn [fic name]` \
            \n **Example:**\n`ffn cadmean victory` "
        )
        embed.add_field(
            name="\u200b",
            value="**Search using URLs is also allowed**",
            inline=False
        )
        embed.add_field(
            name="Search using code blocks:",
            value="This will search ffn first and if it can't find it in ffn, it will search in ao3. " +
            "Use this when you are not sure if the fanfiction is from ffn or ao3.\n**Example:**\n" +
            "\`cadmean victory\` will default to ffnet.\n\`rogue knight ao3\` for ao3.\n\`prince of slytherin ao3 series\` for ao3 series."
        )

    elif page == 1:
        embed = discord.Embed(
            title="Bot Configuration",
            description="_**Do not give administrator permission to the bot.**_\nTo use these commands, you need administrator permission. \
            \nGo to the channel you want to add/remove and use the below commands."
        )
        embed.add_field(
            name="To allow the bot to respond to all the channels",
            value="`,allow_all`", inline=False
        )
        embed.add_field(
            name="To disallow the bot from responding to all the channels",
            value="`,disallow_all`", inline=False
        )
        embed.add_field(
            name="To allow the bot to respond to this channel",
            value="`,allow`", inline=False
        )

        embed.add_field(
            name="To disallow the bot from responding to this channel",
            value="`,disallow`", inline=False
        )

        embed.add_field(
            name="To delete a bot message if it violates the server rules, the user who requested the bot to find the fanfiction can reply to the offending bot message by clicking on `Reply` and replying with `del`.",
            value="\u200b", inline=False
        )

    elif page == 2:
        embed = discord.Embed(
            title="Bot Support",
            description="Join the Bot's Discord Support Server if you need any help in setting up the bot or want to suggest any new features." +
            "\n[Discord Support Server](https://discord.gg/bRzzr3EBqH)"
        )

    else:
        embed = discord.Embed(
            description="No more configuration options found!"
        )

    page_footer = "Page: "+str(page+1)+"/"+str(page_limit)
    embed.set_footer(text=page_footer)

    return embed, page_limit
