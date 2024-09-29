import pytest

from aiohttp.client import ClientSession

from pylnbits.config import Config
from pylnbits.lnurl_w import LnurlWithdraw

"""
Tests: 
 
 Get list of withdraw links
 Get withdraw link
 Create withdraw link
 Update withdraw link (PUT)
 Delte withdraw link
 Get hash check
 Get image embed
"""

class TestLnurlWithdraw:

    @pytest.fixture(autouse=True)
    async def setup_vars(self):
        c = Config(config_file="config.yml")
        session = ClientSession()
        self.lw = LnurlWithdraw(c, session)
        links = await self.lw.list_withdrawlinks()
        self.withdraw_id = links["data"][0]["id"] if links["total"] > 0 else None
        self.hash = links["data"][0]["unique_hash"] if links["total"] > 0 else None
        yield
        await session.close()
    
    # create withdraw link
    async def test_create_withdrawlink(self):
        body = {"title": "autocreatelink", 
                "min_withdrawable": 100,
                "max_withdrawable": 10000, 
                "uses": 10, 
                "wait_time": 3600, 
                "is_unique": True }

        newlink = await self.lw.create_withdrawlink(body)
        assert newlink is not None, f"Failed to create link: {newlink}"
        print(f"\ncreate withdraw link with body: {body}\n\nresult link: {newlink} \n")
        if len(newlink) > 0:
                withdraw_id = newlink["id"]
                print(f'withdraw id: {withdraw_id}')

    # list links
    async def test_list_withdrawlinks(self):
        links = await self.lw.list_withdrawlinks()
        assert links["total"] >= 0, links.get("detail", f"Failed to list links. Response: {links}")
        print("\nlist all links: " , str(links), "\n\n")

    # get withdraw link
    async def test_get_withdrawlink(self):
        getlink = await self.lw.get_withdrawlink(self.withdraw_id)
        assert getlink, f"Failed to get link: {getlink}"
        print(f'\nwithdraw_id for get_link: {self.withdraw_id}')
        print("\nget withdrawl link: ", getlink, "\n")

    # update withdraw link
    async def test_update_withdrawlink(self):
        body = {"title": "autoupdatelink", 
                "min_withdrawable": 10, 
                "max_withdrawable": 1000, 
                "uses": 1, 
                "wait_time": 2400, 
                "is_unique": True}
                
        update_result = await self.lw.update_withdrawlink(self.withdraw_id, body)
        assert update_result is not None, f"Failed to update: {update_result}"
        print(f'\nupdate withdraw link with initial id: {self.withdraw_id} \n\nbody: {body} \n\n result: {update_result}\n\n')

    # get hash check
    async def test_get_hash_check(self):
        response = await self.lw.get_hash_check(self.hash, self.withdraw_id)
        assert response is not None, f"Failed to check hash: {response}"
        print("\nhash check response: ", str(response), "\n\n")

    # get svg image
    async def test_get_image_embed(self):
        img = await self.lw.get_image_embed(self.withdraw_id)
        assert img, f"Failed to get img: {img}"
        print("SVG image: ", str(img), "\n\n")

    # delete link
    async def test_delete_withdrawlink(self):
        delete_result = await self.lw.delete_withdrawlink(self.withdraw_id)
        assert delete_result, f"Failed to delete: {delete_result}"
        print(f'\ndelete withdraw link id: {self.withdraw_id}, result: {delete_result}\n\n')