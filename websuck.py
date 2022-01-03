import time
import zlib
import websockets
import json
import asyncio
import os

ZLIB_SUFFIX = b'\x00\x00\xff\xff'
buffer = bytearray()
inflator = zlib.decompressobj()


def on_websocket_message(msgs):
    buffer = bytearray()
    buffer.extend(msgs)

    #if len(msgs) < 4 or msgs[-4:] != ZLIB_SUFFIX:
    #    return

    msgs = inflator.decompress(buffer)
    buffer = bytearray()
    #print(msgs)
    return msgs

async def websuck():
    async with websockets.connect("wss://gateway.discord.gg/?encoding=json&v=9&compress=zlib-stream") as websussy:
        await websussy.send('{"op":2,"d":{"token":"OTIzODQ4ODc5MjEwOTEzODI0.Yc_3EQ.XZDXRcsEZoyX13obLhSMBCUSsss","capabilities":253,"properties":{"os":"Linux","browser":"Firefox","device":"","system_locale":"en-US","browser_user_agent":"Mozilla/5.0 (X11; Linux x86_64; rv:95.0) Gecko/20100101 Firefox/95.0","browser_version":"95.0","os_version":"","referrer":"","referring_domain":"","referrer_current":"","referring_domain_current":"","release_channel":"stable","client_build_number":108924,"client_event_source":null},"presence":{"status":"online","since":0,"activities":[],"afk":false},"compress":false,"client_state":{"guild_hashes":{},"highest_last_message_id":"0","read_state_version":0,"user_guild_settings_version":-1,"user_settings_version":-1}}}')
        pp = await websussy.recv()
        on_websocket_message(pp)
        await websussy.send('{"op":14,"d":{"guild_id":"678021108037058560","channels":{"737421617902387271":[[0,99]]}}}')
        msgs = await websussy.recv()
        #print(msgs)
        users = on_websocket_message(msgs)

asyncio.run(websuck())
