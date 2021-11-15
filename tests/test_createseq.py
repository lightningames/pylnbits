"""
test sequence:

1. create a user with user manager w/initial wallet.
   save user id, admin key, invoice key to db, connect data w/ TG username
2. activate lnurlp and lnurlw on new user
3. activate lndhub extension

- check balance
- receive by 
      - bolt11 invoice
      - lnurlp link
      - laisee send

- check balance
- send by 
      - lnurlw link (laisee)
      - LN address: user@domain.com
      - laisee send. 
- check balance

- export to wallet

"""