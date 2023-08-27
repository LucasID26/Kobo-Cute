from asyncio import gather
from config import USER_AGENT
import httpx
from aiohttp import ClientSession

# Aiohttp Async Client
session = ClientSession()

# HTTPx Async Client
fetch = httpx.AsyncClient(
    http2=True,
    verify=False,
    headers={"User-Agent": USER_AGENT},
    timeout=httpx.Timeout(10),
)

class httpy:
  async def get(url: str, *args, **kwargs):
    async with session.get(url, *args, **kwargs) as resp:
      try:
        data = await resp.json()
      except Exception:
        data = await resp.text()
    return data


  async def head(url: str, *args, **kwargs):
    async with session.head(url, *args, **kwargs) as resp:
      try:
        data = await resp.json()
      except Exception:
        data = await resp.text()
    return data


  async def post(url: str, *args, **kwargs):
    async with session.post(url, *args, **kwargs) as resp:
      try:
        data = await resp.json()
      except Exception:
        data = await resp.text()
    return data
  
  async def download_url(url: str, nama: str, *args, **kwargs):
    response = await session.get(url, *args, **kwargs)
    filename = f"downloads/{nama}"
    if response.status == 200:
      with open(filename, 'wb') as f:
        while True:
          chunk = await response.content.read(1024*1024)
          if not chunk:
            break
          f.write(chunk)
      return filename
    else:
      return response

async def multiget(url: str, times: int, *args, **kwargs):
    return await gather(*[get(url, *args, **kwargs) for _ in range(times)])


async def multihead(url: str, times: int, *args, **kwargs):
    return await gather(*[head(url, *args, **kwargs) for _ in range(times)])


async def multipost(url: str, times: int, *args, **kwargs):
    return await gather(*[post(url, *args, **kwargs) for _ in range(times)])


async def resp_get(url: str, *args, **kwargs):
    return await session.get(url, *args, **kwargs)


async def resp_post(url: str, *args, **kwargs):
    return await session.post(url, *args, **kwargs)

