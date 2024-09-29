import pytest

from aiohttp.client import ClientSession

from pylnbits.config import Config
from pylnbits.split_payments import SplitPayments

"""
Tests: 
 
 Get list of target wallets
 Add target wallets
 Delete all target wallets
"""

class TestSplitPayments:

    @pytest.fixture(autouse=True)
    async def setup_vars(self):
        c = Config(config_file="config.yml")
        session = ClientSession()
        self.sp = SplitPayments(c, session)
        yield
        await session.close()
    
    # get list of target wallets
    async def test_get_target_wallets(self):
        targetwallets = await self.sp.get_target_wallets()
        assert targetwallets is not None, f"Failed to get target wallets {targetwallets}"
        print(f"Target wallets : {targetwallets}")

    # add target wallets
    async def test_add_target_wallet(self):
        lnaddress = "me@example.com"
        alias = "Me"
        split = 50
        addwallets = await self.sp.add_target_wallet(lnaddress, alias, split)
        assert "targets" in addwallets, f"Failed to add target wallet {addwallets}"
        print(f"\nUpdated list of target wallets: {addwallets}")

    # delete list of target wallets
    async def test_delete_target_wallets(self):
        deletewallets = await self.sp.delete_target_wallets()
        assert deletewallets == "null", f"Failed to delete target wallets: {deletewallets}"
        print(f"\nTarget wallets deleted. Response: {deletewallets}")