import asyncio
import aiohttp
import aiofiles

async def download_one(session,filepath,fileurl):
	async with session.get(fileurl) as resp:
		if resp.status == 200:
			f = await aiofiles.open(filepath,'wb+')
			await f.write(await resp.read())
			await f.close()

async def download_all(images):
	async with aiohttp.ClientSession() as session:
		tasks = []
		for filepath,fileurl in images:
			task = asyncio.ensure_future(download_one(session,filepath,fileurl))
			tasks.append(task)
		await asyncio.gather(*tasks)



def download(filelist):
	asyncio.get_event_loop().run_until_complete(download_all(filelist))    


if __name__ == "__main__":
    files = [('asdf3.png','https://cdnb.artstation.com/p/assets/images/images/008/415/569/large/bach-do-rwby-white-rose-christmas-by-dishwasher1910-daqztp3.jpg?1512608214'),
                ('asdf4.png','https://cdna.artstation.com/p/assets/images/images/008/221/838/large/bach-do-rwby-holidays-2016-by-dishwasher1910-dapt9lm.jpg?1511286887'),]
    download(files)

    