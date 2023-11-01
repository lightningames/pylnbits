import json
import logging

from aiohttp.client import ClientSession
# from lnurl import Lnurl

from pylnbits.utils import delete_url, get_url, post_url

"""
Rest API methods for LNbits Invoices Extension

1. List invoices                - GET invoices
2. Fetch single invoice         - GET invoice/{invoice_id}
3. Create Invoice               - POST invoice
4. Update Invoice               - POST invoice/{invoice_id}
5. Create Invoice Payment       - POST invoice/{invoice_id}/payments
6. Check Invoice Payment Status - GET  invoice/{invoice_id}/payments/{payment_hash}
7. Delete Invoice               - DELETE invoice/{invoice_id}
"""

###################################
logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logging.getLogger("pylnbits").setLevel(level=logging.WARNING)
logger = logging.getLogger(__name__)
###################################


class Invoices:
    def __init__(self, config, session: ClientSession = None):
        """__init__

            Initializes a invoices extension via API

        """
        self._session = session
        self._config = config
        self._lnbits_url = config.lnbits_url
        self._invoice_headers = config.invoice_headers()
        self._admin_headers = config.admin_headers()

    # returns JSON list of Invoices
    async def get_invoices(self):
        """
            GET /invoices/api/v1/invoices

            Headers
            {"X-Api-Key": <invoice_key>}

            Returns 200 OK (application/json)
            [<invoice_object>, ...]
        """
        try:
            upath = "/invoices/api/v1/invoices"
            path = self._lnbits_url + upath
            res = await get_url(session=self._session,
                                path=path, headers=self._invoice_headers)
            return res
        except Exception as e:
            logger.info(e)
            return e

    # Returns an Invoice
    async def get_invoice(self, invoice_id):
        """
            GET /invoices/api/v1/invoice/{invoice_id}

            Headers
            {"X-Api-Key": <invoice_key>}
            Body (application/json)

            Returns 200 OK (application/json)
            {invoice_object}
        """
        try:
            upath = "/invoices/api/v1/invoice/" + invoice_id
            path = self._lnbits_url + upath
            res = await get_url(session=self._session, path=path,
                                headers=self._invoice_headers)
            return res
        except Exception as e:
            logger.info(e)
            return e

    # Creates an Invoice
    async def create_invoice(self, invoice_dto):
        """
            POST /invoices/api/v1/invoice

            Headers
            {"X-Api-Key": <invoice_key>}

            Body (application/json)
            {invoice_object}
                {"wallet": wallet, "status": status, "currency": currency,
                "company_name": company_name,
                "first_name": first_name, "last_name": last_name,
                "email": email, "phone": phone, "address": address,
                "items": [{"description": description, "amount": amount}, ..],
                }

            Returns 200 OK (application/json)
            {invoice_object}
        """
        try:
            upath = "/invoices/api/v1/invoice"
            path = self._lnbits_url + upath
            jbody = json.dumps(invoice_dto.to_dict())
            res = await post_url(session=self._session, path=path,
                                 headers=self._invoice_headers, body=jbody)
            return res
        except Exception as e:
            logger.info(e)
            return e

    # Update an Invoice
    async def update_invoice(self, invoice_dto):
        """
        POST /invoices/api/v1/invoice/{invoice_id}

        Headers
        {"X-Api-Key": <invoice_key>}

        Body (application/json)
        {invoice_object}
            {"wallet": wallet, "status": status, "currency": currency,
             "company_name": company_name, "first_name": first_name,
             "last_name": last_name,
             "email": email, "phone": phone, "address": address,
             "items": [{"description": description, "amount": amount}, ..],
        }

        Returns 200 OK (application/json)
        {invoice_object}
            POST /invoices/api/v1/invoice

        """
        try:
            upath = "/invoices/api/v1/invoice/" + invoice_dto.id
            path = self._lnbits_url + upath
            jbody = json.dumps(invoice_dto.to_dict())
            res = await post_url(session=self._session, path=path,
                                 headers=self._invoice_headers, body=jbody)
            return res
        except Exception as e:
            logger.info(e)
            return e

    # Creates an Invoice Payment
    async def create_invoice_payment(self, invoice_id, famount=300):
        """
            POST /invoices/api/v1/invoice/{invoice_id}/payments?famount=300

            Headers
            {"X-Api-Key": <invoice_key>}
            Body (application/json)

            Returns 200 OK (application/json)
            {payment_object}

        """
        try:
            upath = "/invoices/api/v1/invoice/" + invoice_id + "/payments?famount="
            upath = upath + str(famount)
            path = self._lnbits_url + upath
            jbody = "{}"
            res = await post_url(session=self._session, path=path,
                                 headers=self._invoice_headers, body=jbody)
            return res
        except Exception as e:
            logger.info(e)
            return e

    # Returns Invoice_payment_status
    async def get_invoice_payment_status(self, invoice_id, payment_hash):
        """
            GET /invoices/api/v1/invoice/{invoice_id}/payments/{payment_hash}

            Headers
            {"X-Api-Key": <invoice_key>}
            Body (application/json)

            Returns 200 OK (application/json)
            {invoice_object}
        """
        try:
            upath = "/invoices/api/v1/invoice/" + invoice_id + "/payments/"
            upath = upath + payment_hash
            path = self._lnbits_url + upath
            res = await get_url(session=self._session, path=path,
                                headers=self._invoice_headers)
            return res
        except Exception as e:
            logger.info(e)
            return e

    # Delete an Invoice
    async def delete_invoice(self, invoice_id):
        """
        DELETE /invoices/api/v1/invoice/{invoice_id}

        Headers
        {"X-Api-Key": <admin_key>}

        Body (application/json)

        Returns
            200 OK (application/json)
        """
        try:
            upath = "/invoices/api/v1/invoice/" + invoice_id
            path = self._lnbits_url + upath
            res = await delete_url(session=self._session, path=path,
                                   headers=self._admin_headers)
            return res
        except Exception as e:
            logger.info(e)
            return e
