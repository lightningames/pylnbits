import asyncio

from aiohttp.client import ClientSession

from pylnbits.config import Config
from pylnbits.user_wallet import UserWallet

# TODO: make this a proper unit test with pytest


async def main():

    c = Config(config_file="config.yml")
    url = c.lnbits_url
    print(f"url: {url}")
    print(f"headers: {c.headers()}")
    print(f"admin_headers: {c.admin_headers()}")

    async with ClientSession() as session:
        uw = UserWallet(c, session)
        # works
        userwallet = await uw.get_wallet_details()
        print(f"user wallet info : {userwallet}")

        # works - update the hash for your test case
        payment_hash = "edefef3766537446c70e51af9b414fb3b319baf515f1ff9852c0289eae3665a1"
        res = await uw.check_invoice(payment_hash)
        print(f"check invoice response: {res}")

        # works
        # res = await uw.create_invoice(False, 150, "testcreatetwo", "http://google.com")
        # print(f'\nCreate invoice RESPONSE: {res}\n\n')

        # pay an invoice - add balance and check\
        bolt = "lnbc800n1ps23r2dpp5ahh77dmx2d6yd3cw2xheks20kwe3nwh4zhcllxzjcq5fat3kvkssdqsd9h8vmmfvdjk7mn9cqzpgrzjq02snzwz4petaly54yzjkm358rqa5as9hkgydjvxxmvlpuk6dfd9cz0y2cqq0qsqqyqqqqlgqqqqqqgq9qsp5cut63ftfcffwkrr2w9r50w5e40m93k3er75mc70ysxps7yercs9s9qyyssqs7qk3cz97nm5m6ehzedcxhttx87l7x5kk38gvwkzzv4lhrhddtqq3sk43nnvsddagf36ledw9vhlpqxuu5s53pj6sz926mwqxf8chsgp2m9j8w"  # noqa
        # body = {"out": True, "bolt11": bolt}
        res = await uw.pay_invoice(True, bolt)
        print(res)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
