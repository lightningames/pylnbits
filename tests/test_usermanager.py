from os.path import join, realpath
import sys; sys.path.insert(0, realpath(join(__file__, "../../")))
from config import Config
from lnbits.user_manager import UserManager
from aiohttp.client import ClientSession
import asyncio

# TODO: make this a proper unit test with pytest

async def main():
    
    c = Config(config_file="config.yml")
    url = c.lnbits_url
    headers = c.headers()
    print(f'api_key: {c.api_key}')
    print(f'headers: {c.headers()}')
    
    async with ClientSession() as session:
        um = UserManager(url, headers, session)
        userinfo = await um.get_users()
        print(f'userinfo : {userinfo}')

        uid = userinfo[0]['id']
        print(f'uid: {uid}')
        walletinfo = await um.get_wallets(uid)
        print(walletinfo)

        wid = walletinfo[0]['id']
        txinfo = await um.get_tx(wid)
        print(txinfo)    


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
