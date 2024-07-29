import asyncio

from aiohttp.client import ClientSession

from pylnbits.config import Config
from pylnbits.split_payments import SplitPayments

async def main():

    c = Config(config_file="config.yml")
    url = c.lnbits_url
    print(f"url: {url}")
    print(f"headers: {c.headers()}")
    print(f"admin_headers: {c.admin_headers()}")

    async with ClientSession() as session:
        sp = SplitPayments(c, session)

        # get list of target wallets
        targetwallets = await sp.get_target_wallets()
        print(f"Target wallets : {targetwallets}")

        # add target wallets
        addwallets = await sp.add_target_wallet("me@example.com", "Me", 50)
        print(f"Updated list of target wallets: {addwallets}")

        # delete list of target wallets
        # deletewallets = await sp.delete_target_wallets()
        # print(f"status: {deletewallets}")


loop = asyncio.get_event_loop()
loop.run_until_complete(main())