import join
import asyncio
import gcspam
import leave



print("what would you like to do? 1) spam gc's")
choice = input("choose number that corresponds with option ")

if choice == "1":
    asyncio.run(gcspam.gcspaminit())
if choice == "2":
    asyncio.run(join.joininit())
if choice == "3":
    asyncio.run(leave.leaveinit())
else:
    exit()
