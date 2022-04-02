import join
import asyncio
import gcspam
import leave
import channelspam
import login
import sendfriend
import remfriend

def checkfiles():
    try:
        with open('data/groups.txt', 'r'):
            pass
    except FileNotFoundError:
        open("data/groups.txt", "a+").write(" ")

    try:
        with open('data/proxies.txt', 'r'):
            pass
    except FileNotFoundError:
        open("data/proxies.txt", "a+").write(" ")

    try:
        with open('data/tokens.txt', 'r'):
            pass
    except FileNotFoundError:
        open("data/tokens.txt", "a+").write(" ")

if __name__ == '__main__':
    checkfiles()
    print("what would you like to do?\n"
          "1) Spam gc's\n"
          "2) Join a server\n"
          "3) Leave a server\n"
          "4) Spam a channel\n"
          "5) Login to a Discord token\n"
          "6) Spam friend requests\n"
          "7) Remove friends")
    choice = input("Choose number that corresponds with option ")

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
    else:
        exit()

