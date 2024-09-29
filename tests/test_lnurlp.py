import pytest

from aiohttp.client import ClientSession

from pylnbits.config import Config
from pylnbits.lnurl_p import LnurlPay

"""
Tests: 
 
 Get list of paylinks
 Get paylink
 Create paylink
 Update paylink
 Delete paylink
"""

class TestLnurlPay:

    @pytest.fixture(autouse=True)
    async def setup_vars(self):
        c = Config(config_file="config.yml")
        session = ClientSession()
        self.lp = LnurlPay(c, session)
        links = await self.lp.list_paylinks()
        self.pay_id = links[0]["id"] if len(links) else None
        yield
        await session.close()

    # list links
    async def test_list_paylinks(self):
        links = await self.lp.list_paylinks()
        assert len(links) > 0, f"Failed to list links. Response: {links}"
        print("\nlist all links: " , str(links), "\n\n")

    # get pay link
    async def test_get_paylink(self):
        print(f'\npay_id for get_link: {self.pay_id}')
        
        getlink = await self.lp.get_paylink(pay_id=str(self.pay_id))
        assert getlink, f"Failed to get link: {getlink}"
        print("\nget pay link: ", getlink, "\n")

    # create pay links
    async def test_create_paylink(self):
        body = {"description": "auto pay link",
                "amount": 100,
                "max": 10000,
                "min": 100,
                "comment_chars": 100}
        newlink = await self.lp.create_paylink(body=body)
        assert "id" in newlink, f"Failed to create link: {newlink}"
        print(f"\ncreate pay link with body: {body}, result link: {newlink} \n")

    # update pay link
    async def test_update_paylink(self):
        body = {"description": "update auto paylink",
                "amount": 150, 
                "max": 10000,
                "min": 100,
                "comment_chars": 100}
        
        update_result = await self.lp.update_paylink(pay_id=str(self.pay_id), body=body)
        assert "id" in update_result, f"Failed to update pay link: {update_result}"
        print(f'\nupdate pay link with initial id: {self.pay_id}\n\nbody: {body} \n\nresult: {update_result}\n\n')

    # delete paylink
    async def test_delete_paylink(self):
        delete_result = await self.lp.delete_paylink(pay_id=str(self.pay_id))
        assert delete_result, f"Failed to delete paylink {delete_result}"
        print(f'delete pay link id: {self.pay_id}, result: {delete_result}\n\n')