import json
import logging

from aiohttp.client import ClientSession

from pylnbits.utils import delete_url, put_url, get_url, get_url_resp, post_url

"""
Rest API methods for LNbits LNURLw Withdraw Extension

- List withdraw links 
- Get a withdraw link 
- Create a withdraw link 
- Update a withdraw link 
- Delete a withdraw link 

- Get hash check 
- Get image to embed

"""

###################################
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logging.getLogger("pylnbits").setLevel(level=logging.WARNING)
logger = logging.getLogger(__name__)
###################################


class LnurlWithdraw:
    def __init__(self, config, session: ClientSession = None):
        self._config = config
        self._lnbits_url = config.lnbits_url
        self._invoice_headers = config.invoice_headers()
        self._admin_headers = config.admin_headers()
        self._session = session
        self._upath = "/withdraw/api/v1/links"


    # List withdraw links 
    async def list_withdrawlinks(self):
        """
        GET /withdraw/api/v1/links
        Returns list withdraw links. Returns 200 OK app/json [<withdraw_link_object>, ...]
        """
        try:
            path = self._lnbits_url + self._upath
            res = await get_url(self._session, path, self._invoice_headers)
            return res
        except Exception as e:
            logger.info(e)
            return e


    # Get a withdraw link 
    async def get_withdrawlink(self, withdraw_id: str):
        """
        GET /withdraw/api/v1/links/<pay_id>
        Returns list pay links. Returns 200 OK app/json
        {"lnurl": <string>}
        """
        try:
            path = self._lnbits_url + self._upath + "/" + withdraw_id
            # print(f"GET WITHDRAWL LINK PATH: {path}")
            res = await get_url_resp(self._session, path, self._invoice_headers)
            return res
        except Exception as e:
            logger.info(e)
            return e


    # Create a withdraw link 
    async def create_withdrawlink(self, body: str):
        """
        POST /withdraw/api/v1/links

        Body (application/json)
        {"title": <string>, "min_withdrawable": <integer>, 
        "max_withdrawable": <integer>, "uses": <integer>,
        "wait_time": <integer>, "is_unique": <boolean>}

        Returns Returns 201 CREATED app/json
        {"id": < string> , "is_unique": <boolean>, "k1": <str>, 
        "lnurl": <string>, "max_withdrawable": <int>, 
        "min_withdrawable": <int>, "number": <int>,
        "open_time": <int>, "title": <str>, "unique_hash": <str>, 
        "used": <int>, "uses": <int>, "usescsv": <str>, 
        "wait_time": <int>, "wallet": <str> "}

        Batch Print Page link: https://<lnbits-url>/withdraw/print/<id>
        Shareable link for single QR: https://<lnbits-url>/withdraw/<id>

        """
        try:
            path = self._lnbits_url + self._upath
            res = await post_url(self._session, path=path, headers=self._admin_headers, body=json.dumps(body))
            return res
        except Exception as e:
            logger.info(e)
            return str(e)


    # Update a withdraw link 
    async def update_withdrawlink(self, withdraw_id: str, body: str):
        """
        PUT /withdraw/api/v1/links/<pay_id>

        Body (application/json)
        {"title": <string>, "min_withdrawable": <integer>, 
        "max_withdrawable": <integer>, "uses": <integer>, 
        "wait_time": <integer>, "is_unique": <boolean>}

        Returns Returns 200 OK app/json
        {"lnurl": <string>}
        """
        try:
            path = self._lnbits_url + self._upath + "/" + withdraw_id
            res = await put_url(self._session, path=path, headers=self._admin_headers, body=json.dumps(body))
            return res
        except Exception as e:
            logger.info(e)
            return e


    # Delete a withdraw link 
    async def delete_withdrawlink(self, withdraw_id: str):
        """
        DELETE /withdraw/api/v1/links/<withdraw_id>

        Returns Returns 204 NO CONTENT
        """
        try:
            path = self._lnbits_url + self._upath + "/" + withdraw_id
            print(path)
            res = await delete_url(self._session, path=path, headers=self._admin_headers)
            return res
        except Exception as e:
            logger.info(e)
            return e


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
            res = await get_url(self._session, path=path, headers=self._invoice_headers)
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
            res = await get_url_resp(self._session, path=path, headers=self._invoice_headers)
            return res
        except Exception as e:
            logger.info(e)
            return e
