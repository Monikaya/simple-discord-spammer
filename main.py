import os
import time
import join
import asyncio
import gcspam
import leave
import channelspam
import login
import sendfriend
import remfriend

async def checkfiles():
    try:
        os.mkdir("data")
    except FileExistsError:
        pass
    try:
        with open('data/groups.txt', 'r'):
            pass
    except FileNotFoundError:
        open("data/groups.txt", "x")

    try:
        with open('data/proxies.txt', 'r'):
            pass
    except FileNotFoundError:
        open("data/proxies.txt", "x")

    try:
        with open('data/tokens.txt', 'r'):
            pass
    except FileNotFoundError:
        open("data/tokens.txt", "x")

if __name__ == '__main__':
    asyncio.run(checkfiles())
    print("Loaded settings")
    time.sleep(1)
    os.system("clear")
    print("Simple Discord Spammer\nBy Aquazarine")
    time.sleep(2)
    print("What would you like to do?\n"
          "1) Spam gc's\n"
          "2) Join a server\n"
          "3) Leave a server\n"
          "4) Spam a channel\n"
          "5) Login to a Discord token\n"
          "6) Spam friend requests\n"
          "7) Remove friends\n"
          "0) Exit program")
    choice = input("Choose number that corresponds with option: ")

    if choice == "1":
        asyncio.run(gcspam.gcspaminit())
    if choice == "2":
        asyncio.run(join.joininit())
    if choice == "3":
        asyncio.run(leave.leaveinit())
    if choice == "4":
        asyncio.run(channelspam.spaminit())
    if choice == "5":
        asyncio.run(login.main())
    if choice == "6":
        asyncio.run(sendfriend.sendfriendinit())
    if choice == "7":
        asyncio.run(remfriend.remfriendinit())
    if choice == "0":
        exit()
    else:
        exit()

