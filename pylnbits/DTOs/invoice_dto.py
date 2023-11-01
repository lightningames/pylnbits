"""
InvoiceDTO stands for Invoice Data Transfer Object
"""


class InvoiceDTO:
    def __init__(self, wallet, currency, status="draft"):
        self.id = ""
        self.wallet = wallet
        self.status = status
        self.currency = currency
        self.company_name = ""
        self.first_name = ""
        self.last_name = ""
        self.email = ""
        self.phone = ""
        self.address = ""
        self.items = []

    def to_dict(self):
        return self.__dict__
