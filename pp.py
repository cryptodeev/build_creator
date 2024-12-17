import asyncio

async def create_print(info):
  for text in info:
    print(text)

asyncio.run(create_print(['sup', 'everyone']))

print('thanks for using')
