from os.path import join, realpath
import sys; sys.path.insert(0, realpath(join(__file__, "../../")))
from config import Config
from lnbits.user_wallet import UserWallet
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
        uw = UserWallet(url, headers, session)
        # works
        userwallet = await uw.get_wallet_details()
        print(f'user wallet info : {userwallet}')

        # works
        payment_hash = "4493d1d2db45cfee4e705cf9dcad30bba7b2fa5b5ff112765b9ae82b33ac6797"
        res = await uw.check_invoice(payment_hash)
        print(f'check invoice response: {res}')

        # internal lnbits error with curl
        body = {"out": False, "amount": 150, "memo": 'testcreate'}
        res = await uw.create_invoice(False, 150, 'testcreate')
        print(f'create invoice response: {res}\n\n')

        # pay an invoice - add balance and check
        bolt = 'lnbc2u1ps2fdy2pp5gjfar5kmgh87unnstnuaetfshwnm97jmtlc3yajmnt5zkvavv7tsdqjw3jhxarfdemx76trv5cqzpgrzjq02snzwz4petaly54yzjkm358rqa5as9hkgydjvxxmvlpuk6dfd9cz0y2cqq0qsqqyqqqqlgqqqqqqgq9qsp5g0q0yqe8wyjs4cm7axu80s70drdftdzgrdwtryq9jz9sfttla7ks9qyyssqv9crlg6wqy33amn647u4cdq7g38sghjhnxvqwalzyz7q4slccvtydhjp85xan86e2jh8cem799ywcfk0gx6ttr57pyq9dlxkphagn6gpzz22s7'
        body = {"out": True, "bolt11": bolt}
        res = await uw.pay_invoice(True, bolt)
        print(res)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
