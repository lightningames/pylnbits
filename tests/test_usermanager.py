# TODO: make this a proper unit test
from os.path import join, realpath
import sys; sys.path.insert(0, realpath(join(__file__, "../../")))
from lnbits.user_manager import get_tx, get_users, get_wallets


# tests, temporarily here, move to separate file later
if __name__ == "__main__":
    userinfo = get_users()
    print(userinfo)

    uid = '1edb7b765e8741dfae914ae250f89a63'
    walletinfo = get_wallets(uid)
    print(walletinfo)

    wid = '67745574e65441ed8aa34de062d015b7'
    txinfo = get_tx(wid)
    print(txinfo)    
