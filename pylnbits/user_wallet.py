import json
import logging

from aiohttp.client import ClientSession
from lnurl import Lnurl

from pylnbits.utils import get_url, post_url

# pylnbits/user_wallet.py

"""
The user_wallet.py handles
Rest API methods for LNbits User Wallet
(lnbits page where users can enable extensions)

- Get wallet details
- Create an invoice (incoming)
- Pay an invoice (outgoing)
- Check an invoice (incoming or outgoing)

- Decode an invoice (new)
- Get invoices (incoming or outgoing) (new) 
- Get invoice(s) by memo (incoming or outgoing (new) 

- Drain Funds LNURL-withdraw QR code (?) 
- Export to Phone with QR Code (?) 
"""
###################################
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logging.getLogger("pylnbits").setLevel(level=logging.WARNING)
logger = logging.getLogger(__name__)
###################################


class UserWallet:
    def __init__(self, config, session: ClientSession = None):
        """__init__
        """
        self._session = session
        self._config = config
        self._invoice_headers = config.invoice_headers()
        self._admin_headers = config.admin_headers()
        self._lnbits_url = config.lnbits_url
        self.paypath = "/api/v1/payments"
        self.walletpath = "/api/v1/wallet"

    @property
    def config(self):
        """config property
        """
        return self._config

    async def get_wallet_details(self):
        """
        GET /api/v1/wallet

        Headers
        {"X-Api-Key": "Invoice key"}

        Returns 200 OK (application/json)
        {"id": <string>, "name": <string>, "balance": <int>}

        """
        try:
            # upath = "/api/v1/wallet"
            upath = self.walletpath
            path = self._lnbits_url + upath
            res = await get_url(self._session, path=path, headers=self._invoice_headers)
            return res
        except Exception as e:
            logger.info(e)
            return e

    async def check_invoice(self, hash: str):
        """
        Check an invoice (incoming or outgoing)

        GET /api/v1/payments/<payment_hash>

        Headers: invoice key

        Returns 200 OK (application/json)
        {"paid": <bool>}
        """
        try:
            # ppath = "/api/v1/payments/"
            upath = self.paypath + "/" + hash
            path = self._lnbits_url + upath
            res = await get_url(self._session, path=path, headers=self._invoice_headers)
            return res
        except Exception as e:
            logger.info(e)
            return e

    async def create_invoice(self, direction: bool, amt: int, memo: str, webhook: str):
        """
        Create an invoice(incoming)

        POST /api/v1/payments

        Headers
        {"X-Api-Key": "Invoice Key"}

        Body (application/json)
        {"out": false, "amount": <int>, "memo": <string>}

        Returns 201 CREATED (application/json)
        {"payment_hash": <string>, "payment_request": <string>}

        curl -X POST https://bits.bitcoin.org.hk/api/v1/payments
        -d '{"out": false, "amount": 100, "memo": "poo", "webhook": "http://google.com"}'
        -H "X-Api-Key: f7f740104bba47e9ac9bb3fa......."  # only needs Invoice/read key
        -H "Content-type: application/json"
        """

        try:
            # upath = "/api/v1/payments"
            path = self._lnbits_url + self.paypath
            body = {"out": direction, "amount": amt, "memo": memo, "webhook": webhook}
            j = json.dumps(body)
            res = await post_url(self._session, path=path, headers=self._invoice_headers, body=j)
            return res
        except Exception as e:
            logger.info(e)
            return e

    async def pay_invoice(self, direction: bool, bolt11: str):
        """
        Pay an invoice (outgoing)

        POST /api/v1/payments

        Headers
        {"X-Api-Key": "Admin key"}

        Body (application/json)
        {"out": true, "bolt11": <string>}

        Returns 201 CREATED (application/json)
        {"payment_hash": <string>}

        curl -X POST https://bits.bitcoin.org.hk/api/v1/payments
        -d '{"out": true, "bolt11": <string>}'
        -H "X-Api-Key: b811bd2580a0431c96d3c4......"  # TODO: needs admin key!
        -H "Content-type: application/json"
        """
        try:
            # upath = "/api/v1/payments"
            path = self._lnbits_url + self.paypath
            body = {"out": direction, "bolt11": bolt11}
            j = json.dumps(body)
            #  print(f"body: {j}")
            res = await post_url(self._session, path=path, headers=self._admin_headers, body=j)
            return res
        except Exception as e:
            logger.info(e)
            return e

    async def get_decoded(self, bolt11: str):
        """
        POST /api/v1/payments/decode

        Body (application/json)
        {"data": <string>}

        Returns 200 (application/json)

        Headers: invoice key
        """
        try:
            decode_url = self._lnbits_url + self.paypath + "/decode"
            payload = {"data": bolt11}
            j = json.dumps(payload)
            #res =  requests.post(decode_url, json=payload, headers=self._invoice_headers)
            res = await post_url(self._session, path=decode_url, body=j, headers=self._invoice_headers)
            return res
        except Exception as e:
            print("Exception in get_decoded() ", e)
            return e

    # get payment hash from bolt11
    async def get_payhash(self, bolt11: str):
        """
        Only returns the payment hash not entire decoded invoice
        """
        decoded = await self.get_decoded(bolt11)
        # print(decoded)
        if "payment_hash" in decoded:
            payhash = decoded["payment_hash"]
            return payhash
        else:
            return None

    async def get_invoices(self):
        """
        Get invoices (incoming or outgoing)

        GET /api/v1/payments

        Headers: invoice key

        Returns 200 OK (application/json)
        [{<invoices>}]
        """
        try:
            # ppath = "/api/v1/payments/"
            path = self._lnbits_url + self.paypath
            res = await get_url(self._session, path=path, headers=self._invoice_headers)
            return res
        except Exception as e:
            logger.info(e)
            return e

    async def get_invoicesbymemo(self, memo: str):
        """
        GET /api/v1/payments?memo=<memo>

        Returns 200 OK (application/json)
        [{<invoices>}]

        Headers: invoice key
        """
        try:
            path = self._lnbits_url + self.paypath + "?memo=" + memo
            res = await get_url(self._session, path=path, headers=self._invoice_headers)
            return res
        except Exception as e:
            logger.info(e)
            return e

    # from lnaddress
    def get_payurl(self, email: str):
        """
        Construct Lnurlp link from email address provided.
        """
        try:
            parts = email.split("@")
            domain = parts[1]
            username = parts[0]
            transform_url = "http://" + domain + "/.well-known/lnurlp/" + username
            print("Transformed URl: " + transform_url)
            return transform_url
        except Exception as e:
            print("Exception, possibly malformed LN Address: " + str(e))

    # generates bolt11 invoice from payurl and amount to pay
    async def get_bolt11_from_payurl(self, purl: str, amount: int):
        json_content = await get_url(self._session, path=purl, headers=self._invoice_headers)
        lnurlpay = json_content["callback"]

        millisats = amount * 1000
        payquery = lnurlpay + "?amount=" + str(millisats)

        # get bech32-serialized lightning invoice
        pr_dict = await get_url(self._session, path=payquery, headers=self._invoice_headers)
        # check keys returned for status
        if "status" in pr_dict:
            reason = pr_dict["reason"]
            return reason
        elif "pr" in pr_dict:
            bolt11 = pr_dict["pr"]
            return bolt11



    # from LNURLPay link
    async def get_bolt11_from_lnurlp(self, lnurlp_string: str, amount: int):
        """
        fail state
        {'reason': 'Amount not between min_sendable and max_sendable', 'status': 'ERROR'}

        success state
        {'pr': 'lnbc1......azgfe0',
        'routes': [], 'successAction': {'description': 'Thanks love for the lightning!',
        'tag': 'url', 'url': 'https:/.......'}}
        """
        try:
            lnurl = Lnurl(lnurlp_string)
            purl = lnurl.url
            return await self.get_bolt11_from_payurl(purl, amount)

        except Exception as e:
            print("Exception as: ", str(e))
            return e


    # from lnaddress
    async def get_bolt11(self, email: str, amount: int):
        """
        fail state
        {'reason': 'Amount 100 is smaller than minimum 100000.', 'status': 'ERROR'}

        success state
        {'pr': 'lnbc1......azgfe0',
        'routes': [], 'successAction': {'description': 'Thanks love for the lightning!',
        'tag': 'url', 'url': 'https:/.......'}}
        """
        try:
            purl = self.get_payurl(email)
            return await self.get_bolt11_from_payurl(purl, amount)

        except Exception as e:
            print("Exception as: ", str(e))
            return e