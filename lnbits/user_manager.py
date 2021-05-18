import requests
import logging
import yaml
import os

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

os.chdir("..")
path  = os.getcwd()
config_file = path + '/config.yml'
with open(config_file, 'rb') as f:
    config = yaml.safe_load(f)
f.close()

api_key = config['api_key']
lnbits_url = config['lnbits_url']

headers = {"X-Api-Key" : api_key,
           "Content-type" : "application/json"}


def get_users():
    try:
        upath = "/usermanager/api/v1/users"
        path = lnbits_url+upath
        res = requests.get(path, headers=headers)
        return res.json()
    except Exception as e:
        logger.info(e)
        return e


def get_wallets(user_id):
    try:
        wpath = "/usermanager/api/v1/wallets/" + user_id
        path = lnbits_url + wpath
        res = requests.get(path, headers=headers)
        return res.json()
    except Exception as e:
        logger.info(e)
        return e


def get_tx(wallet_id):
    try:
        tpath = "/usermanager/api/v1/wallets" + wallet_id
        path = lnbits_url + tpath
        res = requests.get(path, headers=headers)
        return res.json()
    except Exception as e:
        logger.info(e)
        return e
