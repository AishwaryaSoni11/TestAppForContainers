from datetime import datetime, timedelta
from discord.ext import commands
import json
import discord
import st_desktop
import st_mobile
import sx_desktop
import sx_mobile

client = commands.Bot(command_prefix='!')


@client.event
async def on_ready():
    print('Bot is online...')


@client.command()
async def user(ms, seller_lvl, currency, account_type):
    user = ms.message.author.id
    czas = datetime.now() + timedelta(hours=1)
    server = ('{:%H:%M:%S}'.format(czas))

    #seller_lvl validation:
    try:
        available_lvl = [1, 2, 3, 4, 5]
        if int(seller_lvl) in available_lvl:
            level_status = True
        else:
            raise Exception
    except Exception as e:
        level_status = False
        embed = discord.Embed(title='An error was detected while selecting the seller level', color=0xD4D1C7)
        embed.add_field(name=f'Try:', value=f'euro, gbp, usd', inline=True)
        embed.set_footer(
            icon_url='https://play-lh.googleusercontent.com/N69vGy7o68mlkKKnVEzO6wIKlw9K0K0yOa9q_mSRnmnUc4pnHhQnECqwMXaVb9mz9g8=w240-h480-rw',
            text=f'Stockx Scraper [Michal#6406] | {server}')
        await ms.send(embed=embed)

    #currency validation:
    try:
        available_currency = ['gbp', 'eur', 'usd']
        if str(currency) in available_currency:
            currency_status = True
        else:
            raise Exception
    except Exception as e:
        currency_status = False
        embed = discord.Embed(title='An error was detected while selecting the currency', color=0xD4D1C7)
        embed.add_field(name=f'Try:', value=f'eur, gbp, usd', inline=True)
        embed.set_footer(
            icon_url='https://play-lh.googleusercontent.com/N69vGy7o68mlkKKnVEzO6wIKlw9K0K0yOa9q_mSRnmnUc4pnHhQnECqwMXaVb9mz9g8=w240-h480-rw',
            text=f'Stockx Scraper [Michal#6406] | {server}')
        await ms.send(embed=embed)

    #currency validation:
    try:
        available_account_type = ['private', 'business']
        if str(account_type) in available_account_type:
            account_type_status = True
        else:
            raise Exception
    except Exception as e:
        account_type_status = False
        embed = discord.Embed(title='An error was detected while selecting the account type', color=0xD4D1C7)
        embed.add_field(name=f'Try:', value=f'eur, gbp, usd', inline=True)
        embed.set_footer(
            icon_url='https://play-lh.googleusercontent.com/N69vGy7o68mlkKKnVEzO6wIKlw9K0K0yOa9q_mSRnmnUc4pnHhQnECqwMXaVb9mz9g8=w240-h480-rw',
            text=f'Stockx Scraper [Michal#6406] | {server}')
        await ms.send(embed=embed)

    #saving information to json file:
    if level_status and currency_status and account_type_status == True:
        try:
            with open("users.json", "r") as file:
                data = json.load(file)
                data[str(user)] = {'seller_level': seller_lvl, 'currency': currency, 'account_type': account_type}
            with open("users.json", "w") as file:
                json.dump(data, file, indent=4)
        except Exception as e:
            embed = discord.Embed(title=f'An error was detected while saving information to json file {e}', color=0xD4D1C7)
            embed.set_footer(
                icon_url='https://play-lh.googleusercontent.com/N69vGy7o68mlkKKnVEzO6wIKlw9K0K0yOa9q_mSRnmnUc4pnHhQnECqwMXaVb9mz9g8=w240-h480-rw',
                text=f'Stockx Scraper [Michal#6406] | {server}')
            await ms.send(embed=embed)
        else:
            embed = discord.Embed(title='The data has been saved successfully', color=0xD4D1C7)
            embed.set_footer(
                icon_url='https://play-lh.googleusercontent.com/N69vGy7o68mlkKKnVEzO6wIKlw9K0K0yOa9q_mSRnmnUc4pnHhQnECqwMXaVb9mz9g8=w240-h480-rw',
                text=f'Stockx Scraper [Michal#6406] | {server}')
            await ms.send(embed=embed)
    else:
        pass


@client.command()
async def info(ms):
    user = str(ms.message.author.id)
    czas = datetime.now() + timedelta(hours=1)
    server = ('{:%H:%M:%S}'.format(czas))
    with open('users.json', 'r') as file:
        data = json.load(file)
        for i in data:
            if i == user:
                seller = str(data[user]['seller_level']).upper()
                curency = str(data[user]['currency']).upper()
                type = str(data[user]['account_type']).upper()
                embed = discord.Embed(title=f'User current information', color=0xD4D1C7)
                embed.add_field(name=f'Seller level:',
                                value=f'```{seller}```',
                                inline=False)
                embed.add_field(name=f'Currency:',
                                value=f'```{curency}```',
                                inline=False)
                embed.add_field(name=f'Account type',
                                value=f'```{type}```',
                                inline=True)
                embed.set_footer(
                    icon_url='https://play-lh.googleusercontent.com/N69vGy7o68mlkKKnVEzO6wIKlw9K0K0yOa9q_mSRnmnUc4pnHhQnECqwMXaVb9mz9g8=w240-h480-rw',
                    text=f'Stockx Scraper [Michal#6406] | {server}')
                await ms.send(embed=embed)
            else:
                continue


@client.command()
async def stockx(ms, sku):
    user = str(ms.message.author.id)
    sku = sku
    date = datetime.today()
    czas = datetime.now() + timedelta(hours=1)
    server = ('{:%H:%M:%S}'.format(czas))
    with open('users.json', 'r') as file:
        data = json.load(file)
        for i in data:
            if i == user:
                level = data[user]['seller_level']
                currency = data[user]['currency']
                account = data[user]['account_type']
            else:
                continue

    sx_desktop.proxy_format()
    sx_desktop.user_data(level, currency, account)
    url_key = sx_desktop.get_data(sku)
    final_info = sx_desktop.fetch_data(url_key[0])

    currency_symbol = ''
    match currency:
        case 'gbp':
            currency_symbol = '£'
        case 'eur':
            currency_symbol = '€'
        case 'usd':
            currency_symbol = '$'

    embed = discord.Embed(url=f'https://stockx.com/{url_key[0]}', title=f'{url_key[3]} - {url_key[2]}',
                          color=0xD4D1C7)

    embed.add_field(name=f'Seller level:',
                    value=f'```{level}```',
                    inline=True)

    embed.add_field(name=f'Currency:',
                    value=f'```{currency}```'.upper(),
                    inline=True)

    embed.add_field(name=f'Account type:',
                    value=f'```{account}```'.upper(),
                    inline=True)

    embed.add_field(name=f'Sizes',
                    value=f'{final_info[0]}```',
                    inline=True)

    embed.add_field(name=f'Lowest ask [{currency_symbol}]',
                    value=f'{final_info[1]}```',
                    inline=True)

    embed.add_field(name=f'Payout [PLN]',
                    value=f'{final_info[2]}```',
                    inline=True)

    embed.set_thumbnail(url=url_key[1])
    embed.set_footer(
        icon_url='https://play-lh.googleusercontent.com/N69vGy7o68mlkKKnVEzO6wIKlw9K0K0yOa9q_mSRnmnUc4pnHhQnECqwMXaVb9mz9g8=w240-h480-rw',
        text=f'Stockx Scraper [Michal#6406] | {server}')
    await ms.send(embed=embed)


@client.command()
async def sx(ms, sku):
    user = str(ms.message.author.id)
    sku = sku
    date = datetime.today()
    czas = datetime.now() + timedelta(hours=1)
    server = ('{:%H:%M:%S}'.format(czas))
    with open('users.json', 'r') as file:
        data = json.load(file)
        for i in data:
            if i == user:
                level = data[user]['seller_level']
                currency = data[user]['currency']
                account = data[user]['account_type']
            else:
                continue

    sx_mobile.proxy_format()
    sx_mobile.user_data(level, currency, account)
    url_key = sx_mobile.get_data(sku)
    final_info = sx_mobile.fetch_data(url_key[0])

    embed = discord.Embed(url=f'https://stockx.com/{url_key[0]}', title=f'{url_key[3]} - {url_key[2]}',
                          color=0xD4D1C7)

    embed.add_field(name=f'Seller level:',
                    value=f'```{level}```',
                    inline=True)

    embed.add_field(name=f'Currency:',
                    value=f'```{currency}```'.upper(),
                    inline=True)

    embed.add_field(name=f'Account type:',
                    value=f'```{account}```'.upper(),
                    inline=True)

    embed.add_field(name=f'[Sizes] Payout',
                    value=f'{final_info}```',
                    inline=True)

    embed.set_thumbnail(url=url_key[1])
    embed.set_footer(
        icon_url='https://play-lh.googleusercontent.com/N69vGy7o68mlkKKnVEzO6wIKlw9K0K0yOa9q_mSRnmnUc4pnHhQnECqwMXaVb9mz9g8=w240-h480-rw',
        text=f'Stockx Scraper [Michal#6406] | {server}')
    await ms.send(embed=embed)


@client.command()
async def sneakit(ms, sku):
    sku = sku
    date = datetime.today()
    czas = datetime.now() + timedelta(hours=1)
    server = ('{:%H:%M:%S}'.format(czas))

    st_desktop.proxy_format()
    sneakit_code = st_desktop.get_id(sku)
    final_info = st_desktop.fetch_payout(sneakit_code[0])


    embed = discord.Embed(url=f'https://sneakit.com/product/{sneakit_code[0]}', title=f'{sneakit_code[1]}',
                          color=0xD4D1C7)

    embed.add_field(name=f'Sizes',
                    value=f'{final_info[0]}```',
                    inline=True)

    embed.add_field(name=f'Lowest ask [€]',
                    value=f'{final_info[1]}```',
                    inline=True)

    embed.add_field(name=f'Payout [PLN]',
                    value=f'{final_info[2]}```',
                    inline=True)

    embed.set_thumbnail(url=sneakit_code[2])
    embed.set_footer(icon_url='https://res.cloudinary.com/crunchbase-production/image/upload/c_lpad,h_170,w_170,f_auto,b_white,q_auto:eco,dpr_1/gljbl14ek9eiqfohe11n',
                     text=f'Sneakit Scraper [Michal#6406] | {server}')
    await ms.send(embed=embed)


@client.command()
async def kit(ms, sku):
    sku = sku
    date = datetime.today()
    czas = datetime.now() + timedelta(hours=1)
    server = ('{:%H:%M:%S}'.format(czas))

    st_mobile.proxy_format()
    sneakit_code = st_mobile.get_id(sku)
    final_info = st_mobile.fetch_payout(sneakit_code[0])


    embed = discord.Embed(url=f'https://sneakit.com/product/{sneakit_code[0]}', title=f'{sneakit_code[1]}',
                          color=0xD4D1C7)

    embed.add_field(name=f'[Sizes] Payout',
                    value=f'{final_info}```',
                    inline=True)

    embed.set_thumbnail(url=sneakit_code[2])
    embed.set_footer(icon_url='https://res.cloudinary.com/crunchbase-production/image/upload/c_lpad,h_170,w_170,f_auto,b_white,q_auto:eco,dpr_1/gljbl14ek9eiqfohe11n',
                     text=f'Sneakit Scraper [Michal#6406] | {server}')
    await ms.send(embed=embed)


client.run('OTI1NDQwMzc0MjQ2MzU0OTc0.G-BdS1.klB0X18MFj70nfpzauMRSXXBCuyVIYANtzb-ds')