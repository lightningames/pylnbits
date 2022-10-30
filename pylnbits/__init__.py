# pylnbits

"""
Modules exported by this package:

- `config.py`: where you set the LNBits user API keys for your instance of the pylnbits library
- `user_wallet.py`: handles Rest API methods for LNbits User Wallet (lnbits page where users can enable extensions)
    - Get wallet details
    - Create an invoice (incoming)
    - Pay an invoice (outgoing)
    - Check an invoice (incoming or outgoing)
    - Decode an invoice (new)
    - Get invoices (incoming or outgoing) (new) 
    - Get invoice(s) by memo (incoming or outgoing (new) 
- `user_manager.py`: For managing multiple users on LNBits, calls Rest API methods from LNbits User Manager Extension

    - GET users
    - GET user (single user)
    - GET wallets
    - GET transactions
    - POST wallet
    - POST user + initial wallet 
    - DELETE user and their wallets
    - DELETE wallet
    - POST activate extension

- `lnurl_p.py`: For creating and managing LNURLp links, calls Rest API methods for LNbits LNURLp Pay Extension
    - List pay links
    - Get a pay link
    - Create a pay link
    - Update a pay link
    - Delete a pay link

- `lnurl_w.py`: For creating and managing LNURLw links, handles Rest API methods for LNbits LNURLw Withdraw Extension:
    - List withdraw links 
    - Get a withdraw link 
    - Create a withdraw link 
    - Update a withdraw link 
    - Delete a withdraw link 
    - Get hash check 
    - Get image to embed

- `lndhub.py`: for fetching admin and invoice lndhub urls

"""