'''
test sequence :
 
1. create a user with user manager w/initial wallet.
   save user id, admin key, invoice key to db, connect data w/ TG username
2. activate lnurlp and lnurlw on new user
3. activate lndhub extension

store data via supabase

- receive by 
      - bolt11 invoice
      - lnurlp link
      - laisee send
- send by 
      - lnurlw link (laisee)
      - LN address: user@domain.com
      - laisee send. 


- export to wallet
- check balance


==========================================

Telegram comands for: 

match telegram  user id with keys for
 1. get wallet balance "get wallet details" from main wallet
 2. get wallet transactions (from user manager) 

 pay another telegram user - 

 3. /send - create invoice on receiving user, then pay an invoice (outgoing) from main wallet
    - enable /send <amt> @username on telegram

 4. /receive - create an invoice (incoming) from main wallet - 
    /receive (lnurl | (any | <satoshis>) [<description>...])
    Generates a BOLT11 invoice with given satoshi value.

 5. /balance  - gets wallet balance and txs
   /transactions

 6. /bluewallet aka /lndhub  - return 

 6. LN Address:  create a pay link with lnurlp extension, update github and db
    provide warning to end user about meta data

  enable /send <amt> username@laisee.org


next stage

 1. decode/check/get invoices (stage 2) 

'''
