"""
Rest API methods for LNbits LndHub Extension
Integrates with Blue Wallet, Zeus

"""
# todo: check that extension is enabled


class LndHub:
    def __init__(self, config):
        self._invoice_key = config.in_key
        self._admin_key = config.admin_key
        self._lnbits_url = config.lnbits_url

    def admin(self):
        url = "lndhub://admin:" + self._admin_key + "@" + self._lnbits_url + "/lndhub/ext/"
        return url

    def invoice(self):
        url = "lndhub://invoice:" + self._invoice_key + "@" + self._lnbits_url + "/lndhub/ext/"
        return url
