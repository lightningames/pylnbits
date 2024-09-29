import pytest

from aiohttp.client import ClientSession

from pylnbits.config import Config
from pylnbits.user_manager import UserManager

"""
Tests: 
 
 Get users
 Get user info
 POST user + initial wallet
 POST create wallet
 POST activate extension
 Delete wallet
 Delete user + wallets
"""

class TestUserManager:

    @pytest.fixture(autouse=True)
    async def setup_vars(self):
        c = Config(config_file="config.yml")
        session = ClientSession()
        self.um = UserManager(c, session)
        userinfo = await self.um.get_users()
        self.uid = userinfo[0]["id"] if len(userinfo) > 0 else None

        # ENTER YOUR USER ID HERE FOR TESTS TO WORK
        self.admin_id = "ACCOUNT-USER-ID-HERE"

        yield
        await session.close()
    
    # POST user + initial wallet
    async def test_post_user_initial(self):
        user_name = "testuser1"
        wallet_name = "testwallet1"

        created_status = await self.um.post_user_initial(self.admin_id, user_name, wallet_name)
        assert "id" in created_status, created_status.get("id","Failed to create user and wallet")
        print(f"\nUser + Initial: created wallet: {created_status}\n")

    
    # Get users
    async def test_get_users(self):
        userinfo = await self.um.get_users()
        assert userinfo is not None, "Failed to get users"
        print(f"Test User Manager: userinfo: {userinfo}\n")

    # Get user info
    async def test_get_user_info(self):
        print(f"\nuid: {self.uid}")
        # get wallet info
        walletinfo = await self.um.get_wallets(self.uid)
        assert len(walletinfo) > 0, f"Failed to get wallet info: {walletinfo}"
        print(f"\nTest User Manager: get wallets: {walletinfo}")

        wid = walletinfo[0]["id"]

        # get transaction info
        txinfo = await self.um.get_tx(wid)
        assert txinfo is not None, "Failed to get transaction info"
        print(f"\nUser Manager - Tx info: {txinfo}, wallet id: {wid}")
        print(type(txinfo))

    # POST create wallet
    async def test_post_wallet(self):
        walletinfo = await self.um.get_wallets(self.uid)
        admin_id = walletinfo[0]["admin"]
        wallet_name = "testwallet1"

        create_status = await self.um.post_wallet(self.uid, wallet_name, admin_id)
        assert "id" in create_status, create_status.get("id", "Failed to create wallet")
        print(f"\nWallet Create: {create_status}\n")

    # POST activate extension
    async def test_post_activate_ext(self):
        extension = "bleskomat"
        active = True

        activate_status = await self.um.post_activate_ext(self.uid, extension, active)
        assert "extension" in activate_status, activate_status.get("detail", f"Failed to activate extension: {activate_status}")
        print(
            f"\nActivate extension: {activate_status},\n"
            + f"Activate inputs: extension {extension},\n"
            + f"active {active}, userid: {self.uid} \n"
        )

    # Delete wallet
    async def test_delete_wallet(self):
        walletinfo = await self.um.get_wallets(self.uid)
        wallet_id = walletinfo[0]["id"]

        del_result = await self.um.delete_wallet(wallet_id)
        assert "detail" in del_result, f"Delete wallet failed: {del_result}"
        print(f"\ndelete wallet: wallet_id {wallet_id} , result: {del_result}\n")

    # Delete user + wallets
    async def test_delete_user(self):
        result = await self.um.delete_user(self.uid)
        assert result == "null", f"Delete user + wallet failed: {result}"
        print(f"\ndelete user and wallets: user_id {self.uid}, result: {result}\n")