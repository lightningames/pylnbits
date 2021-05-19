from os.path import join, realpath
import sys; sys.path.insert(0, realpath(join(__file__, "../../")))
from config import Config
from lnbits.user_manager import UserManager

# TODO: make this a proper unit test
# tests, temporarily here

if __name__ == "__main__":
    
    c = Config(config_file="config.yml")
    url = c.lnbits_url
    headers = c.headers()
    print(c.api_key)
    print(c.headers())
    
    um = UserManager(url, headers)
    userinfo = um.get_users()
    print(userinfo)
    
    uid = userinfo[0]['id']
    walletinfo = um.get_wallets(uid)
    print(walletinfo)

    wid = walletinfo[0]['id']
    txinfo = um.get_tx(wid)
    print(txinfo)    
