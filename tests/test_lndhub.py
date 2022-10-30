# test lndhub link creation
import asyncio
from aiohttp.client import ClientSession
from pylnbits.config import Config
from pylnbits.lndhub import LndHub

# Example code

async def main():
    c = Config(config_file="config.yml")
    url = c.lnbits_url
    print(f"url: {url}")
    print(f"headers: {c.headers()}")
    print(f"admin_headers: {c.admin_headers()}")

    async with ClientSession() as session:
        lh = LndHub(c)
        adminhub = lh.admin()
        print(f'admin lndhub: {adminhub} ')
        invoicehub = lh.invoice()
        print(f'invoice lndhub: {invoicehub} ')


loop = asyncio.get_event_loop()
loop.run_until_complete(main())