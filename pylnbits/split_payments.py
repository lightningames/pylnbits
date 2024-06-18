import json
import logging

from aiohttp.client import ClientSession

from pylnbits.utils import delete_url, get_url, post_url

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