import asyncio
import os
import random
import string
import proxyprocess

try:
    from httpx import AsyncClient
    from tasksio import TaskPool
    import requests
except ImportError:
    os.system('pip install httpx')
    os.system('pip install tasksio')
    os.system('pip install requests')



async def rc(len):
    return os.urandom(len).hex()[len:]

async def getid(invcode):
    headers = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate',
        'accept-language': 'en-GB',
        'content-type': 'application/json',
        'origin': 'https://discord.com',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.1.9 Chrome/83.0.4103.122 Electron/9.4.4 Safari/537.36',
   }

    r = requests.get(f"https://discord.com/api/v9/invites/{invcode}?inputValue={invcode}&with_counts=true&with_expiration=true", headers=headers, timeout=100).json()
    guild = r["guild"]
    guildid = guild["id"]
    return guildid

async def leave(invcode, token, broxy):
    guildid = await getid(invcode)
    print(guildid)
    headers = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US',
        'authorization': f"{token}",
        'cookie': f'__dcfduid={await rc(43)}; __sdcfduid={await rc(96)}; __stripe_mid={await rc(18)}-{await rc(4)}-{await rc(4)}-{await rc(4)}-{await rc(18)}; locale=en-GB; __cfruid={await rc(40)}-{"".join(random.choice(string.digits) for i in range(10))}',
        'content-type': 'application/json',
        'origin': 'https://discord.com',
        'referer': f'https://discord.com/api/v9/users/@me/guilds/{guildid}',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.1.9 Chrome/83.0.4103.122 Electron/9.4.4 Safari/537.36',
        'x-debug-options': 'bugReporterEnabled',
        'x-super-properties': "yJvcyI6IkxpbnV4IiwiYnJvd3NlciI6IkRpc2NvcmQgQ2xpZW50IiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X3ZlcnNpb24iOiIwLjAuMTciLCJvc192ZXJzaW9uIjoiNS4xNS4yOC0xLU1BTkpBUk8iLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLUdCIiwid2luZG93X21hbmFnZXIiOiJLREUsdW5rbm93biIsImRpc3RybyI6IlwiTWFuamFybyBMaW51eFwiIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTIxNTUzLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==",
    }

    try:
        res = await broxy.request(method="DELETE", url=f"https://discord.com/api/v9/users/@me/guilds/{guildid}", json={"lurking": "false"}, headers=headers)
        print(res)
        return res
    except Exception as e:
        print(e)
        pass


async def startpp(invcode, token, proxy):
    async with AsyncClient(proxies={'https://': 'http://' + proxy}) as broxy:
        res = await leave(invcode, token, broxy)
    if res.status_code == 204:
        print(f"left server with token '{token}'")
    else:
        print(res.text)


async def getinfo():
    with open('data/tokens.txt', 'r') as tokns:
        tokens = [line.rstrip('\n') for line in tokns]
    print("loaded")

    invcode = input("what invite would you like to leave? (last string, no discord.gg/): ")

    async with TaskPool(2_00) as pool:
        for token in tokens:
            await pool.put(startpp(invcode, token, proxyprocess.GetProxy()))
    input("done leaving server, press enter to exit! ")
    quit()

def leaveinit():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(getinfo())