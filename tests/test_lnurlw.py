# test lnurl withdraw
import asyncio

from aiohttp.client import ClientSession

from pylnbits.config import Config
from pylnbits.lnurl_w import LnurlWithdraw

import json
# TODO: make this a proper unit test with pytest

async def main():
    c = Config(config_file="config.yml")
    url = c.lnbits_url
    print(f"url: {url}")
    print(f"headers: {c.headers()}")
    print(f"admin_headers: {c.admin_headers()}")

    async with ClientSession() as session:
        lw = LnurlWithdraw(c, session)

        # list links        
        links = await lw.list_withdrawlinks()
        print("list all links: " , str(links), "\n\n")

        # get withdraw link 
        """
        Sample Response:
        {'id': 'TqEZDGaahmg7v856SLSCEZ', 'is_unique': 1, 
        'k1': 'RK3LDiYniu53xjg3FDjvNy', 
        'lnurl': 'LNURL1DP68GURN8GHJ7MRWVF5HGUEWDPSHQCTC9E5K7TMHD96XSERJV9MJ7CTSDYHHVVF0D3H82UNV9ANXW36TV3Y9GAME2P88SJM6D9J8QS6DD9TKKT6KGD9K6A26X4UH5UZ4FGUY2JRZW5EKYA6J2CZARS9N', 
        'max_withdrawable': 10, 'min_withdrawable': 10, 'number': 0, 
        'open_time': 1636960974, 'title': 'Sats Withdraw Test', 
        'unique_hash': 'fgGKdHTwyPNxKzidpCMiWk', 'used': 0, 'uses': 10,
         'usescsv': '1,2,3,4,5,6,7,8,9,10', 'wait_time': 3600, 
         'wallet': 'da21fe8072044a2e8fc093b3c024f9ca'} 
        """
        withdraw_id = links[0]['id']
        print(f'withdraw_id for get_link: {withdraw_id}')
        getlink = await lw.get_withdrawlink(withdraw_id)
        print("get withdrawl link: ", str(getlink), "\n")


        # create link
        body = {"title": "autocreatelink", 
                "min_withdrawable": 100,
                "max_withdrawable": 10000, 
                "uses": 10, 
                "wait_time": 3600, 
                "is_unique": True }

        newlink = await lw.create_withdrawlink(body)
        print(f"create withdraw link with body: {body}, result link: {newlink} \n")
        withdraw_id = newlink['id']

        # update newly created link above
        body = {"title": "autoupdatelink", 
                "min_withdrawable": 10, 
                "max_withdrawable": 1000, 
                "uses": 1, 
                "wait_time": 2400, 
                "is_unique": True}
        update_result = await lw.update_withdrawlink(withdraw_id, body)
        print(f'update withdraw link with intial id: {withdraw_id}, body: {body} \n result: {update_result}\n\n')

        # delete above created link
        delete_result = await lw.delete_withdrawlink(withdraw_id)
        print(f'delete withdraw link id: {withdraw_id}, result: {delete_result}\n\n')


        
        # get 'unique_hash' from link info, in get link
        hash =  links[0]['unique_hash']
        lnurl_id =  links[0]['id']
        print(f'hash: {hash}, lnurl_id: {lnurl_id}\n')
        
        # get_hash_check
        # sample response:  {'hash': True, 'lnurl': True} 
        response = await lw.get_hash_check(hash, lnurl_id)
        print("hash check response: ", str(response), "\n\n")

        # get_image_embed, returns in SVG format. 
        img = await lw.get_image_embed(lnurl_id)
        print("SVG image: ", str(img), "\n\n")


loop = asyncio.get_event_loop()
loop.run_until_complete(main())