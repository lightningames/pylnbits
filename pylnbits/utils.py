import json

"""
 utils for aiohttp. 
"""

# return as json response
async def get_url(session, path, headers):
    """
    aiohttp: for use with GET requests
    """
    async with session.get(path, headers=headers) as resp:
        # res = await resp.read()
        res = await resp.json()
        return res


# return as text response
async def get_url_resp(session, path, headers):
    async with session.get(path, headers=headers) as resp:
        res = await resp.text()
        return res


async def post_jurl(session, path, headers, json):
    """
    aiohttp: for use with JSON in POST requests
    """
    async with session.post(url=path, headers=headers, json=json) as resp:
        res = await resp.json()
        return res


async def post_url(session, path, headers, body):
    """
    aiohttp: for use with BODY in POST requests
    """
    async with session.post(url=path, headers=headers, data=body) as resp:
        res = await resp.json()
        return res


async def put_url(session, path, headers, body):
    """
    aiohttp: for use with BODY in PUT requests
    """
    async with session.put(url=path, headers=headers, data=body) as resp:
        res = await resp.json()
        return res


async def delete_url(session, path, headers) -> str:
    """
    aiohttp: for use with DELETE requests
    """
    async with session.delete(path, headers=headers) as resp:
        res = await resp.text()
        return res

# not defined: session.head, session.options, session.patch