import asyncio

from aiohttp.client import ClientSession
from pylnbits.config import Config
from pylnbits.invoices import Invoices
from pylnbits.DTOs.invoice_dto import InvoiceDTO

async def main():

    c = Config(config_file="config.yml")
    url = c.lnbits_url
    print(f"url: {url}")
    print(f"headers: {c.headers()}")
    print(f"admin_headers: {c.admin_headers()}")

    async with ClientSession() as session:

        inv = Invoices(c, session)
        print(f"\n")

        # get invoices
        invoices = await inv.get_invoices()
        print(f"Invoices:\n{invoices}\n")

        # get invoice
        # update the invoice_id for your test case
        invoice_id = "8vYb8ui5fpEa6ELKoHt6CB"
        res = await inv.get_invoice(invoice_id)
        print(f"Invoice:\n{res}\n")

        # create invoice
        invoice_dto = InvoiceDTO("wallet", "EUR", "draft")
        invoice_dto.company_name = 'my_company_name10'
        invoice_dto.first_name = 'my_first_name'
        invoice_dto.last_name = 'my_last_name'
        invoice_dto.email = 'my_email@email.com'
        invoice_dto.address = 'my_address'
        invoice_dto.phone = 'my_phone_number'
        invoice_dto.items = [{"description": "item1", "amount": 5}, {"description": "item2", "amount": 3}]
        res = await inv.create_invoice(invoice_dto)
        print(f"Created invoice \n{res}\n")

        # update invoice
        # update the invoice_id for your test case
        invoice_dto = InvoiceDTO("wallet", "EUR", "draft")
        invoice_dto.id = 'NWQt8WbEXLLBP5kR7v25tD'
        invoice_dto.company_name = 'my_company_name10_1'
        invoice_dto.first_name = 'my_first_name1'
        invoice_dto.last_name = 'my_last_name1'
        invoice_dto.email = 'my_email@email.com1'
        invoice_dto.address = 'my_address1'
        invoice_dto.phone = 'my_phone_number1'
        invoice_dto.items = [{"description": "item33", "amount": 5}, {"description": "item24", "amount": 3}]
        res = await inv.update_invoice(invoice_dto)
        print(f"Updated invoice: \n{res}\n")

        # create invoice payment
        # update the invoice_id for your test case
        invoice_id = "oKHncemJR72iWjbMWuWdXm"
        res = await inv.create_invoice_payment(invoice_id)
        print(f"Invoice payment::\n{res}\n")

        # check invoice payment status
        # update the invoice_id and payment_hash for your test case
        invoice_id = "oKHncemJR72iWjbMWuWdXm"
        payment_hash = "1c4643d0f2be78e82556c4cddb1723d20d7bda3f9e2c591b00a92baf9b4992f1"
        res = await inv.get_invoice_payment_status(invoice_id, payment_hash)
        print(f"Invoice payment status:\n{res}\n")

        # delete invoice
        # update the invoice_id for your test case
        invoice_id = "CoxjMMnGKtjCyqAMv37rFK"
        res = await inv.delete_invoice(invoice_id)
        print(f"Delete Invoice result::\n{res}\n")


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
