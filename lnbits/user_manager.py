from aiohttp.client import ClientSession
import logging
from config import Config

'''
Rest API methods for LNbits User Manager Extension

GET users
GET wallets
GET transactions

todo:

POST user + initial wallet
POST wallet
DELETE user and their wallets
DELETE wallet
POST activate extension
'''

###################################
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger('lnbot').setLevel(level=logging.WARNING)
logger = logging.getLogger(__name__)
###################################


class UserManager:
    def __init__(self,
                  config:  Config = None,
                  session: ClientSession = None):
        self._config = config
        self._lnbits_url = config.lnbits_url
        self._headers = config.headers()
        self._session = session


    async def get_url(self, path):
        async with self._session.get(path, headers=self._headers) as resp:
            res = await resp.json()
            return res


    async def get_users(self):
        try:
            upath = "/usermanager/api/v1/users"
            path = self._lnbits_url + upath
            res = await self.get_url(path)
            return res
        except Exception as e:
            logger.info(e)
            return e


    async def get_wallets(self, user_id):
        try:
            wpath = "/usermanager/api/v1/wallets/" + user_id
            path = self._lnbits_url + wpath
            res = await self.get_url(path)
            return res
        except Exception as e:
            logger.info(e)
            return e


    async def get_tx(self, wallet_id):
        try:
            tpath = "/usermanager/api/v1/wallets" + wallet_id
            path = self._lnbits_url + tpath
            res = await self.get_url(path)
            return res
        except Exception as e:
            logger.info(e)
            return e