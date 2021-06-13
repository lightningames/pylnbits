import asyncio

from aiohttp.client import ClientSession

from pylnbits.config import Config
from pylnbits.user_manager import UserManager

# TODO: make this a proper unit test with pytest


async def main():

    c = Config(config_file="config.yml")
    url = c.lnbits_url
    print(f"url: {url}")
    print(f"in_key: {c.in_key}")
    print(f"headers: {c.headers()}")

    async with ClientSession() as session:
        um = UserManager(c, session)

        # get users
        userinfo = await um.get_users()
        print(f"Test User Manager: userinfo: {userinfo}\n")

        # get user info
        for user in userinfo:
            uid = user["id"]
            print(f"uid: {uid}")
            walletinfo = await um.get_wallets(uid)
            print(f"Test User Manager: get wallets: {walletinfo}\n")

            # Transaction info
            wid = walletinfo[0]["id"]
            txinfo = await um.get_tx(wid)
            print(f"User Manager - Tx info: {txinfo}, wallet id: {wid}")

        # Post Create User + Initial
        admin_id = walletinfo[0]["admin"]
        user_name = "testuser1"
        wallet_name = "testwallet1"

        print(f"admin_id: {admin_id}, username: {user_name}, walletname: {wallet_name}")

        created_status = await um.post_user_initial(admin_id, user_name, wallet_name)
        print(f"User + Initial: created wallet: {created_status}\n")

        # Post Create Wallet
        user_id = admin_id
        # Body (application/json) - "admin_id" is a YOUR user ID
        create_status = await um.post_wallet(user_id, wallet_name, admin_id)
        print(f"Wallet Create: {create_status}\n")

        # Post activate extension
        extension = "bleskomat"
        active = True
        user_id = "03ea3a3de6ab4b1abb14f53dc3cd6629"  # create_status['user']

        activate_status = await um.post_activate_ext(user_id, extension, active)
        print(
            f"Activate extension: {activate_status},\n"
            + f"Activate inputs: extension {extension},\n"
            + f"active {active}, userid: {user_id} \n"
        )

        # Delete wallet
        wallet_id = "a8f5286b714e40bbb7ff08e5e203632d"
        del_result = await um.delete_wallet(wallet_id)
        print(f"delete wallet: wallet_id {wallet_id} , result: {del_result}\n")

        # Delete users and their wallets
        user_id = "4ea4eddcc0a84a8a867d1e75c142e610"
        result = await um.delete_user(user_id)
        print(f"delete user and wallets: user_id {user_id}, result {result}\n")

    # TODO FINISH TESTS


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
