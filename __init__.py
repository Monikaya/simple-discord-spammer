import join
import asyncio
import gcspam
import leave
import channelspam



print("what would you like to do? "
      "1) spam gc's"
      "2) join a server"
      "3) leave a server"
      "4) spam a channel")
choice = input("choose number that corresponds with option ")

if choice == "1":
    asyncio.run(gcspam.gcspaminit())
if choice == "2":
    asyncio.run(join.joininit())
if choice == "3":
    asyncio.run(leave.leaveinit())
if choice == "4":
    asyncio.run(channelspam.spaminit())
else:
    exit()
