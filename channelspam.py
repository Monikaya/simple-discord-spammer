import asyncio
import os
import random
import string
import threading
import time

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


async def spam(chnlid, token, broxy, guildid, msgcontent):
    payload = {"content": f"{msgcontent}", "nonce": "".join(random.choice(string.digits) for _ in range(18)),
               "tts": "false"}
    headers = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-GB',
        'authorization': f"{token}",
        'cookie': f'__dcfduid={await rc(43)}; __sdcfduid={await rc(96)}; __stripe_mid={await rc(18)}-{await rc(4)}-{await rc(4)}-{await rc(4)}-{await rc(18)}; locale=en-GB; __cfruid={await rc(40)}-{"".join(random.choice(string.digits) for i in range(10))}',
        'content-type': 'application/json',
        'origin': 'https://discord.com',
        'referer': f'https://discord.com/channels/{guildid}/{chnlid}',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.1.9 Chrome/83.0.4103.122 Electron/9.4.4 Safari/537.36',
        'x-debug-options': 'bugReporterEnabled',
        'x-context-properties': 'eyJsb2NhdGlvbiI6IkpvaW4gR3VpbGQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6IjY3ODAyMTEwODAzNzA1ODU2MCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI3Mzc0MjE2MTc5MDIzODcyNzEiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjB9',
        'x-super-properties': "eyJvcyI6IkxpbnV4IiwiYnJvd3NlciI6IkZpcmVmb3giLCJkZXZpY2UiOiIiLCJzeXN0ZW1fbG9jYWxlIjoiZW4tVVMiLCJicm93c2VyX3VzZXJfYWdlbnQiOiJNb3ppbGxhLzUuMCAoWDExOyBMaW51eCB4ODZfNjQ7IHJ2Ojk1LjApIEdlY2tvLzIwMTAwMTAxIEZpcmVmb3gvOTUuMCIsImJyb3dzZXJfdmVyc2lvbiI6Ijk1LjAiLCJvc192ZXJzaW9uIjoiIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjEwODkyNCwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0=",
    }

    try:
        res = await broxy.post(f"https://discord.com/api/v9/channels/{chnlid}/messages", headers=headers, timeout=100,
                               json=payload)
        print(res)
        return res
    except Exception as e:
        print(e)
        pass


async def startpp(chnlid, token, proxy, guildid, msgcontent):
    async with AsyncClient(proxies={'https://': 'http://' + proxy}) as broxy:
        res = await spam(chnlid, token, broxy, guildid, msgcontent)

    if res.status_code == 200:
        print("sent message")
    else:
        print("prolly rate limited")


async def getinfo(chnlid, tokens, guildid, msgcontent):
    async with TaskPool(2_00) as pool:
        for token in tokens:
            await pool.put(startpp(chnlid, token, proxyprocess.GetProxy(), guildid, msgcontent))
        return


def between_callback(chnlid, tokens, guildid, msgcontent):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(getinfo(chnlid, tokens, guildid, msgcontent))
    loop.close()


def spaminit():
    thread_list = list()
    with open('data/tokens.txt', 'r') as tokns:
        tokens = [line.rstrip('\n') for line in tokns]
    print("loaded")

    guildid = input("what is the guild id?: ")
    chnlid = input("what channel id would you like to spam: ")
    msgcontent = input("what would you like your message to say?: ")
    instances = True
    while instances:
        t = threading.Thread(target=between_callback, args=(chnlid, tokens, guildid, msgcontent))
        t.start()
        time.sleep(2)
        print(t.name + ' started!')
        thread_list.append(t)
    for thread in thread_list:
        thread.join()

