from aiohttp.client import ClientSession
import logging
import json
from config import Config

'''
Rest API methods for LNbits User Wallet
(lnbits page where users can enable extensions)

- Get wallet details
- Create an invoice (incoming)
- Pay an invoice (outgoing)
- Check an invoice (incoming or outgoing)

'''
###################################
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger('lnbot').setLevel(level=logging.WARNING)
logger = logging.getLogger(__name__)
###################################


class UserWallet:
    def __init__(self,
                  config:  Config=None, 
                  session: ClientSession = None):
        self._config = config
        self._session = session
        self._headers = config.headers()
        self._admin_headers = config.admin_headers()
        self._lnbits_url = config.lnbits_url


    async def get_url(self, path):
        async with self._session.get(path, headers=self._headers) as resp:
            res = await resp.json()
            return res

    async def post_url(self, path, body, admin_key):
        headers = self._headers
        if admin_key:
            headers = self._admin_headers
        print('\nPost_Url in UserWallet')
        print(f'headers: {self._headers}\n')
        print(f'path: {path}')
        print(f'headers: {headers}')
        async with self._session.post(path, headers=headers, data=body) as resp:
            res = await resp.json()
            return res


    async def get_wallet_details(self):
        try:
            upath = "/api/v1/wallet"
            path = self._lnbits_url + upath
            res = await self.get_url(path)
            return res
        except Exception as e:
            logger.info(e)
            return e

    async def check_invoice(self, hash: str):
        try:
            upath = "/api/v1/payments/" + hash
            path = self._lnbits_url + upath
            res = await self.get_url(path)
            return res
        except Exception as e:
            logger.info(e)
            return e


    async def create_invoice(self, direction: bool, amt: int, memo: str, webhook: str):
        '''
        curl -X POST https://bits.bitcoin.org.hk/api/v1/payments 
        -d '{"out": false, "amount": 100, "memo": "poo", "webhook": "http://google.com"}'
        -H "X-Api-Key: f7f740104bba47e9ac9bb3fa......."  # only needs Invoice/read key
        -H "Content-type: application/json"
        '''

        try:
            upath = "/api/v1/payments"
            path = self._lnbits_url + upath
            body = {"out": direction, 
                    "amount": amt,
                    "memo": memo, 
                    "webhook": webhook}
            j = json.dumps(body)
            res = await self.post_url(path, j, admin_key=False)
            return res
        except Exception as e:
            logger.info(e)
            return e


    async def pay_invoice(self, direction: bool, bolt11: str):
        '''
        curl -X POST https://bits.bitcoin.org.hk/api/v1/payments 
        -d '{"out": true, "bolt11": <string>}' 
        -H "X-Api-Key: b811bd2580a0431c96d3c4......"  # TODO: needs admin key!
        -H "Content-type: application/json"
        '''
        try:
            upath = "/api/v1/payments"
            path = self._lnbits_url + upath
            body = {"out": direction, "bolt11": bolt11}
            j = json.dumps(body)
            print(f'body: {j}')
            res = await self.post_url(path, j, admin_key=True)
            return res
        except Exception as e:
            logger.info(e)
            return e




