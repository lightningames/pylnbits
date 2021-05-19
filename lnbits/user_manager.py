import requests
import logging


'''
Rest API methods for LNbits User Manager Extension

GET users
GET wallets
GET transactions
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
                  lnbits_url: str=None, 
                  headers: dict=None):
        self._lnbits_url = lnbits_url
        self._headers = headers
    

    def get_users(self):
        try:
            upath = "/usermanager/api/v1/users"
            path = self._lnbits_url+upath
            res = requests.get(path, headers=self._headers)
            return res.json()
        except Exception as e:
            logger.info(e)
            return e


    def get_wallets(self, user_id):
        try:
            wpath = "/usermanager/api/v1/wallets/" + user_id
            path = self._lnbits_url + wpath
            res = requests.get(path, headers=self._headers)
            return res.json()
        except Exception as e:
            logger.info(e)
            return e


    def get_tx(self, wallet_id):
        try:
            tpath = "/usermanager/api/v1/wallets" + wallet_id
            path = self._lnbits_url + tpath
            res = requests.get(path, headers=self._headers)
            return res.json()
        except Exception as e:
            logger.info(e)
            return e
