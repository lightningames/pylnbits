import json
import logging

from aiohttp.client import ClientSession

from pylnbits.utils import delete_url, get_url, post_url

"""
Rest API methods for LNbits User Manager Extension

GET users
GET wallets
GET transactions
POST wallet
POST user + initial wallet

DELETE user and their wallets
DELETE wallet
POST activate extension
"""

###################################
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logging.getLogger("pylnbits").setLevel(level=logging.WARNING)
logger = logging.getLogger(__name__)
###################################


class UserManager:
    def __init__(self, config, session: ClientSession = None):
        self._config = config
        self._lnbits_url = config.lnbits_url
        self._headers = config.headers()
        self._admin_headers = config.admin_headers()
        self._session = session

    async def get_users(self):
        try:
            upath = "/usermanager/api/v1/users"
            path = self._lnbits_url + upath
            res = await get_url(session=self._session, path=path, headers=self._headers)
            return res
        except Exception as e:
            logger.info(e)
            return e

    async def get_wallets(self, user_id):
        try:
            wpath = "/usermanager/api/v1/wallets/" + user_id
            path = self._lnbits_url + wpath
            res = await get_url(session=self._session, path=path, headers=self._headers)
            return res
        except Exception as e:
            logger.info(e)
            return e

    async def get_tx(self, wallet_id):
        try:
            tpath = "/usermanager/api/v1/wallets" + wallet_id
            path = self._lnbits_url + tpath
            res = await get_url(session=self._session, path=path, headers=self._headers)
            return res
        except Exception as e:
            logger.info(e)
            return e

    async def post_user_initial(self, admin_id, user_name, wallet_name):
        try:
            tpath = "/usermanager/api/v1/users"
            path = self._lnbits_url + tpath
            body = {"admin_id": admin_id, "user_name": user_name, "wallet_name": wallet_name}
            jbody = json.dumps(body)
            res = await post_url(session=self._session, path=path, headers=self._headers, body=jbody)
            return res
        except Exception as e:
            logger.info(e)
            return e

    async def post_wallet(self, user_id, wallet_name, admin_id):
        try:
            tpath = "/usermanager/api/v1/wallets"
            path = self._lnbits_url + tpath
            body = {"user_id": user_id, "wallet_name": wallet_name, "admin_id": admin_id}
            jbody = json.dumps(body)
            res = await post_url(session=self._session, path=path, headers=self._headers, body=jbody)
            return res
        except Exception as e:
            logger.info(e)
            return e

    async def delete_user(self, user_id):
        try:
            tpath = "/usermanager/api/v1/users/" + user_id
            path = self._lnbits_url + tpath
            res = await delete_url(session=self._session, path=path, headers=self._headers)
            return res
        except Exception as e:
            logger.info(e)
            return e

    async def delete_wallet(self, wallet_id):
        try:
            tpath = "/usermanager/api/v1/wallets/" + wallet_id
            path = self._lnbits_url + tpath
            res = await delete_url(session=self._session, path=path, headers=self._headers)
            return res
        except Exception as e:
            logger.info(e)
            return e

    async def post_activate_ext(self, user_id: str, extension: str, active: int):
        try:
            tpath = "/usermanager/api/v1/extensions"
            path = self._lnbits_url + tpath
            body = {"userid": user_id, "extension": extension, "active": active}
            jbody = json.dumps(body)
            res = await post_url(session=self._session, path=path, headers=self._headers, body=jbody)
            return res
        except Exception as e:
            logger.info(e)
            return e
