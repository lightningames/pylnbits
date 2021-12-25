import json
import logging

from aiohttp.client import ClientSession

from pylnbits.utils import delete_url, get_url, post_url, put_url

"""
Rest API methods for LNbits LNURLp Pay Extension

- List pay links
- Get a pay link
- Create a pay link
- Update a pay link
- Delete a pay link

"""

###################################
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logging.getLogger("pylnbits").setLevel(level=logging.WARNING)
logger = logging.getLogger(__name__)
###################################


class LnurlPay:
    def __init__(self, config, session: ClientSession = None):
        self._config = config
        self._lnbits_url = config.lnbits_url
        self._invoice_headers = config.invoice_headers()
        self._admin_headers = config.admin_headers()
        self._session = session
        self._upath = "/lnurlp/api/v1/links"

    async def list_paylinks(self):
        """
        GET /lnurlp/api/v1/links
        Returns list pay links. Returns 200 OK app/json [<pay_link_object>, ...]
        """
        try:
            path = self._lnbits_url + self._upath
            res = await get_url(self._session, path, self._invoice_headers)
            return res
        except Exception as e:
            logger.info(e)
            return e

    async def get_paylink(self, pay_id: str):
        """
        GET /lnurlp/api/v1/links/<pay_id>
        Returns list pay links. Returns 200 OK app/json
        {"lnurl": <string>}
        """
        try:
            path = self._lnbits_url + self._upath + "/" + pay_id
            res = await get_url(self._session, path, self._invoice_headers)
            return res
        except Exception as e:
            logger.info(e)
            return e

    async def create_paylink(self, body: str):
        """
        POST /lnurlp/api/v1/links

        Body (application/json)
        {"description": <string> "amount": <integer> "max": <integer>
         "min": <integer> "comment_chars": <integer>}

        Returns Returns 201 CREATED app/json
        {"lnurl": <string>}
        """
        try:
            path = self._lnbits_url + self._upath
            res = await post_url(self._session, path=path, headers=self._admin_headers, body=json.dumps(body))
            return res
        except Exception as e:
            logger.info(e)
            return e

    async def update_paylink(self, pay_id: str, body: str):
        """
        PUT /lnurlp/api/v1/links/<pay_id>

        Body (application/json)
        {"description": <string> "amount": <integer>}

        Returns Returns 200 OK app/json
        {"lnurl": <string>}
        """
        try:
            path = self._lnbits_url + self._upath + "/" + pay_id
            res = await put_url(self._session, path=path, headers=self._admin_headers, body=json.dumps(body))
            return res
        except Exception as e:
            logger.info(e)
            return e

    async def delete_paylink(self, pay_id: str):
        """
        DELETE /lnurlp/api/v1/links/<pay_id>

        Returns Returns 204 NO CONTENT
        """
        try:
            path = self._lnbits_url + self._upath + "/" + pay_id
            res = await delete_url(self._session, path=path, headers=self._admin_headers)
            return res
        except Exception as e:
            logger.info(e)
            return e
