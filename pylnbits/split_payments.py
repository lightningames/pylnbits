import json
import logging

from aiohttp.client import ClientSession

from pylnbits.utils import delete_url, get_url, put_url

"""
Rest API methods for LNbits Split Payments Extension

GET target wallets
PUT target wallet
DELETE target wallets
"""

###################################
logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logging.getLogger("pylnbits").setLevel(level=logging.WARNING)
logger = logging.getLogger(__name__)
###################################

class SplitPayments:
    def __init__(self, config, session: ClientSession = None):
        """__init__

            Initializes a Split Payments extension via API

        """
        self._session = session
        self._config = config
        self._lnbits_url = config.lnbits_url
        self._invoice_headers = config.invoice_headers()
        self._admin_headers = config.admin_headers()
        self.splitpath = "/splitpayments/api/v1/targets"

    # Return list of target wallets
    async def get_target_wallets(self):
        """
        GET /splitpayments/api/v1/targets

        Headers
        {"X-Api-Key": "Admin key"}

        Returns an array 
        200 OK (application/json)
        [{'wallet': <string>, 'source': <string>, 'percent': <float>, 'alias': <string>}]

        """
        try:
            upath = self.splitpath
            path = self._lnbits_url + upath
            res = await get_url(self._session, path=path, headers=self._admin_headers)
            return res
        except Exception as e:
            logger.info(e)
            return e
    
    # Add target wallet
    async def add_target_wallet(self, wallet: str, alias: str, percent: float):
        """
        PUT /splitpayments/api/v1/targets

        Headers
        {"X-Api-Key": "Admin key"}

        Returns null 
        200 OK (application/json)
        
        `wallet` can either be a lightning address, lnurl, lnbits internal wallet id.
        `percent` can up to 6 decimal places
        """
        try:
            upath = self.splitpath
            path = self._lnbits_url + upath

            # check if there are other targets to avoid overwriting
            targets = await self.get_target_wallets()
            data = [{"wallet": wallet, "alias" : alias, "percent": percent}]
            if targets is not None:
                data = targets + data
            body = {"targets": data}
            j = json.dumps(body)
            res = await put_url(self._session, path=path, headers=self._admin_headers, body=j)
            
            # response body is null when successful. Return the updated list
            if res is None:
                updatedlist = await self.get_target_wallets()
                return {"targets" : updatedlist}
            return res
        except Exception as e:
            logger.info(e)
            return e
        
    # Delete all target wallets
    async def delete_target_wallets(self):
        """
        DELETE /splitpayments/api/v1/targets

        Headers
        {"X-Api-Key": "Admin key"}

        Returns null 
        200 OK
        """
        try:
            upath = self.splitpath
            path = self._lnbits_url + upath
            res = await delete_url(self._session, path=path, headers=self._admin_headers)
            # response body is null when successful.
            return res
        except Exception as e:
            logger.info(e)
            return e