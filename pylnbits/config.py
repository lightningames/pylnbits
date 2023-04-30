import os

from yaml import safe_load
"""
Config is where you set the LNBits user API keys for the pylnbits library
"""


class Config:
    def __init__(self, config_file: str = "",
                        in_key: str = None, 
                        admin_key: str = None, 
                        lnbits_url: str = None):

        """

        """
        self._config_file = config_file
        self._in_key = in_key
        self._lnbits_url = lnbits_url
        self._admin_key = admin_key

        try:
            if config_file:
                if not os.path.exists(config_file):
                    raise FileNotFoundError(f"Config file: {config_file} not found!")
                
                with open(config_file, "rb") as f:
                    cfile = safe_load(f)
                    print(cfile)
                f.close()

                # add file error checking
                self._in_key = cfile["in_key"]
                self._lnbits_url = cfile["lnbits_url"]
                self._admin_key = cfile["admin_key"]
        
        except Exception as e:
            print(e)
            return e

    @property
    def in_key(self):
        return self._in_key

    @property
    def admin_key(self):
        return self._admin_key

    @property
    def lnbits_url(self):
        return self._lnbits_url

    # regular headers
    def headers(self):
        data = {"Content-type": "application/text"}
        return data

    # invoice key
    def invoice_headers(self):
        data = {"X-Api-Key": self._in_key, "Content-type": "application/json"}
        return data

    # admin key
    def admin_headers(self):
        data = {"X-Api-Key": self._admin_key, "Content-type": "application/json"}
        return data


if __name__ == "__main__":
    c = Config(
        in_key="test",
        admin_key="test",
        lnbits_url="https://legend.lnbits.com"
    )

    print(f"{c.in_key=}")
    print(f"{c.admin_key=}")
    print(f"{c.lnbits_url=}")
    print(f"{c.headers()=}")
    print(f"{c.invoice_headers()=}")
    print(f"{c.admin_headers()=}")
