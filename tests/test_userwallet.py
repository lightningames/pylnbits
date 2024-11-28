import pytest

from aiohttp.client import ClientSession

from pylnbits.config import Config
from pylnbits.user_wallet import UserWallet

"""
Tests: 
 
 Get wallet details
 Check invoice
 Pay invoice
 Pay lnurl
 Pay lightning address
 Create an invoice
 Decode an invoice
 Get payment hash
 Get invoices (incoming or out)
 Get invoice(s) by memo (incoming or out)
"""

class TestUserWallet:

    @pytest.fixture(autouse=True)
    async def setup_vars(self):
        c = Config(config_file="config.yml")
        session = ClientSession()
        self.uw = UserWallet(c, session)
        yield
        await session.close()
    
    # get wallet details
    async def test_get_wallet_details(self):
        userwallet = await self.uw.get_wallet_details()
        assert userwallet is not None, "Failed to get wallet details"
        print(f"\nuser wallet info : {userwallet}")
    
    # check invoice
    async def test_check_invoice(self):
        payment_hash = "edefef3766537446c70e51af9b414fb3b319baf515f1ff9852c0289eae3665a1"
        res = await self.uw.check_invoice(payment_hash)
        assert "paid" in res, res.get("detail", "Check failed")
        print(f"\nInvoice status: {res['paid']}. \n\nFull check invoice response: \n{res}")

    # pay invoice
    async def test_pay_invoice(self):
        # bolt = "lnbc800n1ps23r2dpp5ahh77dmx2d6yd3cw2xheks20kwe3nwh4zhcllxzjcq5fat3kvkssdqsd9h8vmmfvdjk7mn9cqzpgrzjq02snzwz4petaly54yzjkm358rqa5as9hkgydjvxxmvlpuk6dfd9cz0y2cqq0qsqqyqqqqlgqqqqqqgq9qsp5cut63ftfcffwkrr2w9r50w5e40m93k3er75mc70ysxps7yercs9s9qyyssqs7qk3cz97nm5m6ehzedcxhttx87l7x5kk38gvwkzzv4lhrhddtqq3sk43nnvsddagf36ledw9vhlpqxuu5s53pj6sz926mwqxf8chsgp2m9j8w"  
        bolt = input("Enter invoice to pay: ")
        res = await self.uw.pay_invoice(True, bolt)
        assert "payment_hash" in res, res.get("detail", "Failed to pay")
        print(f"\nOutput:\n{res}")

    # pay lnurl
    async def test_pay_lnurl(self):
        # Test LNURL. Replace with your own.
        # paylnurl = "LNURL1DP68GURN8GHJ7ER9D4HJUMRWVF5HGUEWVDHK6TMVDE6HYMRS9UUXJ6JVGGUSYQG89P"
        paylnurl = input("Enter LNURL to pay: ")
        # pay_lnurl(lnurl, amount, comment, description)
        res = await self.uw.pay_lnurl(paylnurl, 1, "hello", "world")
        assert "payment_hash" in res, "Failed to pay LNURL"
        print(f"\nOutput:\n{res}")

    # pay lnaddress
    async def test_pay_lnaddress(self):
        # Test lightning address. Replace with your own. 
        # lnaddress = "testln@demo.lnbits.com"
        lnaddress = input("Enter lightning address to pay: ")
        # pay_lnaddress(lnurl, amount, comment, description)
        res = await self.uw.pay_lnaddress(lnaddress, 1, "sunshine", "hello")
        assert "payment_hash" in res, "Failed to pay lightning address"
        print(f"\nOutput:\n{res}")

    # create invoice
    async def test_create_invoice(self):
        # create_invoice(direction, amount, memo, webhook)
        res = await self.uw.create_invoice(False, 10, "testcreatetwo", "http://google.com")
        assert "payment_hash" in res, res
        print(f"\nInvoice output: \n{res}")

    # decode
    async def test_get_decoded(self):
        # Test data. You can replace with LNURL or bolt11
        # data = "lnbc800n1ps23r2dpp5ahh77dmx2d6yd3cw2xheks20kwe3nwh4zhcllxzjcq5fat3kvkssdqsd9h8vmmfvdjk7mn9cqzpgrzjq02snzwz4petaly54yzjkm358rqa5as9hkgydjvxxmvlpuk6dfd9cz0y2cqq0qsqqyqqqqlgqqqqqqgq9qsp5cut63ftfcffwkrr2w9r50w5e40m93k3er75mc70ysxps7yercs9s9qyyssqs7qk3cz97nm5m6ehzedcxhttx87l7x5kk38gvwkzzv4lhrhddtqq3sk43nnvsddagf36ledw9vhlpqxuu5s53pj6sz926mwqxf8chsgp2m9j8w"
        # data = "LNURL1DP68GURN8GHJ7ER9D4HJUMRWVF5HGUEWVDHK6TMVDE6HYMRS9UUXJ6JVGGUSYQG89P"
        data = input("Enter invoice or LNURL to decode: ")
        res = await self.uw.get_decoded(data)
        assert "payment_hash" in res or "domain" in res, res.get("message", "Decode failed")
        print(f"\nDecoded output: \n{res}")

    # get payment hash
    async def test_get_payhash(self):
        bolt = "lnbc800n1ps23r2dpp5ahh77dmx2d6yd3cw2xheks20kwe3nwh4zhcllxzjcq5fat3kvkssdqsd9h8vmmfvdjk7mn9cqzpgrzjq02snzwz4petaly54yzjkm358rqa5as9hkgydjvxxmvlpuk6dfd9cz0y2cqq0qsqqyqqqqlgqqqqqqgq9qsp5cut63ftfcffwkrr2w9r50w5e40m93k3er75mc70ysxps7yercs9s9qyyssqs7qk3cz97nm5m6ehzedcxhttx87l7x5kk38gvwkzzv4lhrhddtqq3sk43nnvsddagf36ledw9vhlpqxuu5s53pj6sz926mwqxf8chsgp2m9j8w"  
        res = await self.uw.get_payhash(bolt)
        assert res is not None, f"Failed to get payment hash: {res}"
        print(f"\nPayment hash: {res}")

    # get invoices
    async def test_get_invoices(self):
        res = await self.uw.get_invoices()
        assert res is not None, "Failed to get invoices"
        print(f"\nList of invoices: \n{res}")

    # get invoices by memo
    async def test_get_invoicesbymemo(self):
        # memo = "hello"
        memo = input("Enter memo to find: ")
        res = await self.uw.get_invoicesbymemo(memo)
        assert res is not None, "Failed to get invoices"
        print(f"\nList of invoices: \n{res}")