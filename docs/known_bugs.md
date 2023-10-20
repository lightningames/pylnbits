
        Issues found:
        Version: LNbits version: 0.10.9, Commit version: docker
        Environment: https://testnet.plebnet.dev/invoices/?usr=e7608e844139462fbb10c8bcc37c8f00

        Issue #1
        Can not update items in existing Invoice.
        How to reproduce (Use Mozzila Firefox web browser, (Use Chrome web browser, Version 118.0.5993.70 (Official Build) (64-bit)):):
        1. Create invoice #1, add few items, save
        2. Try to edit Invoice #1 by adding additional items and try to Save
        3. Open Updated Invoce #1: See items list <- there is no now items

        Issue #2
        Can not delete existing Invoices
        How to reproduce (Use Chrome web browser, Version 118.0.5993.70 (Official Build) (64-bit)):
        1. Create Invoice
        2. Try to delete created Invoice
            Request URL visible in browser: https://testnet.plebnet.dev/invoices/api/v1/invoice/DqubfiNbS8W2DRicpwgVfD/delete
            Browser returns 404 Not Found
            {"detail":"Not Found"} 
        Requested URL should be DELETE /invoices/api/v1/invoice/{invoice_id} instead DELETE /invoices/api/v1/invoice/{invoice_id}/delete

