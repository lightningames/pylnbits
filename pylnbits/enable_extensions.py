
enable extension for this user 
link : 

https://bits.bitcoin.org.hk/extensions?usr=dd09c7b0fe33480ab28252c9c9b85c6b&enable=lnurlp

create a lnurlp pay link

needs an admin key

POST /lnurlp/api/v1/links
Headers
{"X-Api-Key": <admin_key>}
Body (application/json)
{"description": <string> "amount": <integer> "max": <integer> "min": <integer> "comment_chars": <integer>}
Returns 201 CREATED (application/json)
{"lnurl": <string>}
