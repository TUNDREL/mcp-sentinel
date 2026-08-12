import asyncio
import json

from mcp import ClientSession
import httpx2
from mcp.client.streamable_http import streamable_http_client


async def try_once():
    url = "https://game.spacemolt.com/mcp"
    http_client = httpx2.AsyncClient(timeout=httpx2.Timeout(30.0, read=300.0))
    async with streamable_http_client(url, http_client=http_client) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            result = await session.list_tools()
            print(f"Tool count this call: {len(result.tools)}")
            print(f"next_cursor present: {result.next_cursor is not None}")
            if result.next_cursor:
                print(f"next_cursor value: {result.next_cursor}")

            bypass_matches = [
                t.name for t in result.tools
                if "bypass" in (t.description or "").lower()
            ]
            for t in result.tools:
                if "bypass" in (t.description or "").lower():
                    print(f"\nFull tool: {t.name}")
                    print(f"Description: {t.description}\n")
            print(f"Tools with 'bypass' in description: {bypass_matches}")


async def main():
    for attempt in range(1, 4):
        try:
            await try_once()
            return
        except* Exception as eg:
            print(f"Attempt {attempt} failed: {list(eg.exceptions)}")
            if attempt < 3:
                await asyncio.sleep(2 * attempt)


asyncio.run(main())