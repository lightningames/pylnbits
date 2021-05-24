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
    print(f'url: {url}')
    print(f'api_key: {c.api_key}')
    print(f'headers: {c.headers()}')
    
    async with ClientSession() as session:
        um = UserManager(c, session)
        userinfo = await um.get_users()
        print(f'Test User Manager: userinfo: {userinfo}\n')

        for user in userinfo:
            uid = user['id']
            print(f'uid: {uid}')
            walletinfo = await um.get_wallets(uid)
            print(f'Test User Manager: get wallets: {walletinfo}\n')

        wid = walletinfo[0]['id']
        txinfo = await um.get_tx(wid)
        print(f'User Manager - Tx info: {txinfo}\n')


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
