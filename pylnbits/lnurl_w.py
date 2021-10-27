import json
import logging

from aiohttp.client import ClientSession
from pylnbits.utils import delete_url, get_url, post_url

"""
Rest API methods for LNbits LNURLw Withdraw Extension

- List withdraw links (todo)
- Get a withdraw link (todo)
- Create a withdraw link (todo)
- Update a withdraw link (todo)
- Delete a withdraw link (todo)

- Get hash check 
- Get image to embed

"""

###################################
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logging.getLogger("pylnbits").setLevel(level=logging.WARNING)
logger = logging.getLogger(__name__)
###################################

# sample lnurl_id = "L77CXXszd4tqo8hhj9kKe8"


class LnurlWithdraw:
    def __init__(self, config, session: ClientSession = None):
        self._config = config
        self._lnbits_url = config.lnbits_url
        self._headers = config.headers()
        self._admin_headers = config.admin_headers()
        self._session = session

    async def get_hash_check(self, hash: str, lnurl_id: str):
        """
        GET /withdraw/api/v1/links/<the_hash>/<lnurl_id>
        
        Headers {"X-Api-Key": <invoice_key>} 

        Returns 201 CREATED (application/json)
        {"status": <bool>}
        """
        try:
            upath = "/withdraw/api/v1/links/"
            path = self._lnbits_url + upath + hash + "/" + lnurl_id
            res = await get_url(self._session, path=path, headers=self._headers)
            return res
        except Exception as e:
            logger.info(e)
            return e

    async def get_image_embed(self, lnurl_id: str):
        """
        GET /withdraw/img/<lnurl_id>
        """
        try:
            upath = "/withdraw/img/"
            path = self._lnbits_url + upath + lnurl_id
            res = await get_url(self._session, path=path, headers=self._headers)
            # may not need headers
            return res
        except Exception as e:
            logger.info(e)
            return e
