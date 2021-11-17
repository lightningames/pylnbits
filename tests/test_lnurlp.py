# test lnurlp  pay link
import asyncio

from aiohttp.client import ClientSession

from pylnbits.config import Config
from pylnbits.lnurl_p import LnurlPay

import json
# TODO: make this a proper unit test with pytest

async def main():
    c = Config(config_file="config.yml")
    url = c.lnbits_url
    print(f"url: {url}")
    print(f"headers: {c.headers()}")
    print(f"admin_headers: {c.admin_headers()}")

    async with ClientSession() as session:
        lw = LnurlPay(c, session)

        # list links        
        links = await lw.list_paylinks()
        print("list all links: " , str(links), "\n\n")

        # get pay link 
        pay_id = links[0]['id']
        print(f'pay_id for get_link: {pay_id}')
        getlink = await lw.get_paylink(pay_id=str(pay_id))
        print("get pay link: ", str(getlink), "\n")

        # create pay link
        body = {"description": "auto pay link",
                "amount": 100,
                "max": 10000,
                "min": 100,
                "comment_chars": 100}

        newlink = await lw.create_paylink(body=body)
        print(f"create pay link with body: {body}, result link: {newlink} \n")
        pay_id = newlink['id']

        # update newly created link above
        body = {"description": "update auto paylink",
                "amount": 150}
        update_result = await lw.update_paylink(pay_id=str(pay_id), body=body)
        print(f'update pay link with intial id: {pay_id}, body: {body} \n result: {update_result}\n\n')

        # delete above created link
        delete_result = await lw.delete_paylink(pay_id=str(pay_id))
        print(f'delete pay link id: {pay_id}, result: {delete_result}\n\n')



loop = asyncio.get_event_loop()
loop.run_until_complete(main())