import pytest

from aiohttp.client import ClientSession

from pylnbits.config import Config
from pylnbits.invoices import Invoices
from pylnbits.DTOs.invoice_dto import InvoiceDTO

"""
Tests: 
 
 Create invoice
 Get invoices
 Get invoice
 Create invoice payment
 Get payment status
 Update invoice
 Delete invoice
"""

class TestInvoices:

    @pytest.fixture(autouse=True)
    async def setup_vars(self):
        c = Config(config_file="config.yml")
        session = ClientSession()
        self.inv = Invoices(c, session)
        invoices = await self.inv.get_invoices()
        self.invoice_id = invoices[0]["id"] if invoices else None
        yield
        await session.close()

    # create invoice
    async def test_create_invoice(self):
        invoice_dto = InvoiceDTO("wallet", "EUR", "open")
        invoice_dto.company_name = 'my_company_name10'
        invoice_dto.first_name = 'my_first_name'
        invoice_dto.last_name = 'my_last_name'
        invoice_dto.email = 'my_email@email.com'
        invoice_dto.address = 'my_address'
        invoice_dto.phone = 'my_phone_number'
        invoice_dto.items = [{"description": "item1", "amount": 5},
                                {"description": "item2", "amount": 3}]
            
        res = await self.inv.create_invoice(invoice_dto)
        assert "id" in res, f"Failed to create invoice {res}"
        print(f"\nCreated invoice \n{res}\n")

    # get invoices
    async def test_get_invoices(self):
        invoices = await self.inv.get_invoices()
        assert len(invoices) > 0, f"Failed to get invoices: {invoices}"
        print(f"\nInvoices:\n{invoices}\n")
    
    # get invoice
    async def test_get_invoice(self):
        res = await self.inv.get_invoice(self.invoice_id)
        assert res, res.get("detail", f"Failed to get invoice: {res}")
        print(f"\nInvoice:\n{res}\n")

    # create invoice payment
    async def test_create_invoice_payment(self):
        result = await self.inv.get_invoice(self.invoice_id)
        
        # calculate total value of invoice items
        amount = 0
        for item in result["items"]:
            amount += item["amount"]
        
        res = await self.inv.create_invoice_payment(self.invoice_id, amount)
        assert "payment_request" in res, res.get("detail", f"Failed to get invoice payment details {res}")
        self.payment_hash = res["payment_hash"]
        print(f"\nInvoice payment::\n{res}\n")

    # payment status
    async def test_invoice_payment_status(self):
        await self.test_create_invoice_payment()
        res = await self.inv.get_invoice_payment_status(self.invoice_id, self.payment_hash)
        assert res, res.get("detail", f"Failed to get status: {res}")
        print(f"Invoice payment status:\n{res}\n")

    # update invoice
    async def test_update_invoice(self):
        invoice_dto = InvoiceDTO("wallet", "EUR", "draft")
        invoice_dto.id = self.invoice_id
        invoice_dto.company_name = 'my_company_name10_1'
        invoice_dto.first_name = 'my_first_name1'
        invoice_dto.last_name = 'my_last_name1'
        invoice_dto.email = 'my_email@email.com1'
        invoice_dto.address = 'my_address1'
        invoice_dto.phone = 'my_phone_number1'
        invoice_dto.items = [{"description": "item33", "amount": 5},
                             {"description": "item24", "amount": 3}]
        res = await self.inv.update_invoice(invoice_dto)
        assert "id" in res, f"Failed to create invoice {res}"
        print(f"\nUpdated invoice: \n{res}\n")

    # delete invoice
    async def test_delete_invoice(self):
        res = await self.inv.delete_invoice(self.invoice_id)
        assert res, f"Failed to delete: {res}"
        print(f"Delete Invoice result::\n{res}\n")