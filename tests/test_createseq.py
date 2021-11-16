"""
test sequence:

1. create a user with user manager w/initial wallet.
2. save user id, admin key, invoice key to db, connect data w/ TG username
3. activate lnurlp, lnurlw, lndhub extension on new user

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
# user_name and wallet_name is telegram username