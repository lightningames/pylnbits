# utils


async def get_url(session, path, headers):
    async with session.get(path, headers=headers) as resp:
        res = await resp.json()
        return res


async def post_url(session, path, headers, body):
    async with session.post(path, headers=headers, data=body) as resp:
        res = await resp.json()
        return res


async def delete_url(session, path, headers):
    async with session.delete(path, headers=headers) as resp:
        res = await resp.text()
        return res
