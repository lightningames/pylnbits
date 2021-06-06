import json
import logging

from aiohttp.client import ClientSession

from pylnbits.utils import get_url, post_url

"""
Rest API methods for LNbits User Wallet
(lnbits page where users can enable extensions)

- Get wallet details
- Create an invoice (incoming)
- Pay an invoice (outgoing)
- Check an invoice (incoming or outgoing)

"""
###################################
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logging.getLogger("pylnbits").setLevel(level=logging.WARNING)
logger = logging.getLogger(__name__)
###################################


class UserWallet:
    def __init__(self, config, session: ClientSession = None):
        self._session = session
        self._config = config
        self._headers = config.headers()
        self._admin_headers = config.admin_headers()
        self._lnbits_url = config.lnbits_url

    async def get_wallet_details(self):
        try:
            upath = "/api/v1/wallet"
            path = self._lnbits_url + upath
            res = await get_url(self._session, path, self._headers)
            return res
        except Exception as e:
            logger.info(e)
            return e

    async def check_invoice(self, hash: str):
        try:
            upath = "/api/v1/payments/" + hash
            path = self._lnbits_url + upath
            res = await get_url(self._session, path, self._headers)
            return res
        except Exception as e:
            logger.info(e)
            return e

    async def create_invoice(self, direction: bool, amt: int, memo: str, webhook: str):
        """
        curl -X POST https://bits.bitcoin.org.hk/api/v1/payments
        -d '{"out": false, "amount": 100, "memo": "poo", "webhook": "http://google.com"}'
        -H "X-Api-Key: f7f740104bba47e9ac9bb3fa......."  # only needs Invoice/read key
        -H "Content-type: application/json"
        """

        try:
            upath = "/api/v1/payments"
            path = self._lnbits_url + upath
            body = {"out": direction, "amount": amt, "memo": memo, "webhook": webhook}
            j = json.dumps(body)
            res = await post_url(self._session, path=path, headers=self._headers, body=j)
            return res
        except Exception as e:
            logger.info(e)
            return e

    async def pay_invoice(self, direction: bool, bolt11: str):
        """
        curl -X POST https://bits.bitcoin.org.hk/api/v1/payments
        -d '{"out": true, "bolt11": <string>}'
        -H "X-Api-Key: b811bd2580a0431c96d3c4......"  # TODO: needs admin key!
        -H "Content-type: application/json"
        """
        try:
            upath = "/api/v1/payments"
            path = self._lnbits_url + upath
            body = {"out": direction, "bolt11": bolt11}
            j = json.dumps(body)
            print(f"body: {j}")
            res = await post_url(self._session, path=path, headers=self._admin_headers, body=j)
            return res
        except Exception as e:
            logger.info(e)
            return e
