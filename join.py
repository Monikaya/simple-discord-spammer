import asyncio
import os
import random
import string

import requests
from httpx import AsyncClient

import proxyprocess
from proxyprocess import *
from tasksio import TaskPool


async def rc(len):
    return os.urandom(len).hex()[len:]

async def join(invcode, token, broxy):
    headers = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate',
        'accept-language': 'en-GB',
        'authorization': f"{token}",
        'cookie': f'__dcfduid={await rc(43)}; __sdcfduid={await rc(96)}; __stripe_mid={await rc(18)}-{await rc(4)}-{await rc(4)}-{await rc(4)}-{await rc(18)}; locale=en-GB; __cfruid={await rc(40)}-{"".join(random.choice(string.digits) for i in range(10))}',
        'content-type': 'application/json',
        'origin': 'https://discord.com',
        'referer': f'https://discord.com/api/v9/invites/{invcode}',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.1.9 Chrome/83.0.4103.122 Electron/9.4.4 Safari/537.36',
        'x-debug-options': 'bugReporterEnabled',
        'x-context-properties': 'eyJsb2NhdGlvbiI6IkpvaW4gR3VpbGQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijc4NDMwNDcxNzE1NjQ1MDMwNSIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI4MzQ1NjM2MzEzMjQ1OTQxOTYiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjB9',
        'x-super-properties': "eyJvcyI6IkxpbnV4IiwiYnJvd3NlciI6IkZpcmVmb3giLCJkZXZpY2UiOiIiLCJzeXN0ZW1fbG9jYWxlIjoiZW4tVVMiLCJicm93c2VyX3VzZXJfYWdlbnQiOiJNb3ppbGxhLzUuMCAoWDExOyBMaW51eCB4ODZfNjQ7IHJ2Ojk1LjApIEdlY2tvLzIwMTAwMTAxIEZpcmVmb3gvOTUuMCIsImJyb3dzZXJfdmVyc2lvbiI6Ijk1LjAiLCJvc192ZXJzaW9uIjoiIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjEwODkyNCwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0=",
    }

    try:
        res = await broxy.post(f"https://discord.com/api/v9/invites/{invcode}", headers=headers, json={}, timeout=100)
        return res
    except Exception as e:
        print(e)
        pass


async def startpp(invcode, token, proxy):
    async with AsyncClient(proxies={'https://': 'http://' + proxy}) as broxy:
        res = await leave(invcode, token, broxy)
#    if res.status_code == 204:
#        print("thingie sent")
#    else:
#        print(res.text)


async def main():
    with open('data/tokens.txt', 'r') as tokns:
        tokens = [line.rstrip('\n') for line in tokns]
    print("tokens did done")

    invcode = "e5qPztaV"

    async with TaskPool(2_00) as pool:
        for token in tokens:
            await pool.put(startpp(invcode, token, proxyprocess.GetProxy()))


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
