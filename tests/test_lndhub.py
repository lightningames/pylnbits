import pytest

from aiohttp.client import ClientSession

from pylnbits.config import Config
from pylnbits.lndhub import LndHub

"""
Tests: 
 
 Get admin hub link
 Get invoice hub link
"""

class TestLndHub:

    @pytest.fixture(autouse=True)
    async def setup_vars(self):
        c = Config(config_file="config.yml")
        session = ClientSession()
        self.lh = LndHub(c)
        yield
        await session.close()

    # admin
    async def test_admin(self):
        adminhub = self.lh.admin()
        assert adminhub, f"Failed to get adminhub link {adminhub}"
        print(f'\nadmin lndhub: {adminhub} ')

    # invoice
    async def test_invoice(self):
        invoicehub = self.lh.invoice()
        assert invoicehub, f"Failed to get adminhub link {invoicehub}"
        print(f'\ninvoice lndhub: {invoicehub} ')
