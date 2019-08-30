import requests
import asyncio

"""
Has to take in a list of tuples, 
each tuple having format (filepath, url of the download)

"""

def download_one(url,filepath):
    try:
        x = requests.get(url)
        with open(filepath,'wb+') as f:
            f.write(x.content)
    except:
        pass

async def dl(lista):
    loop = asyncio.get_event_loop()
    futures = [loop.run_in_executor(None,
                                    download_one,
                                    url,
                                    filepath)
               for filepath,url in lista]
    for response in await asyncio.gather(*futures):
        pass


def download(url_list):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(dl(url_list))

if __name__ == "__main__":
    url_list = [('asdf3.png','https://cdnb.artstation.com/p/assets/images/images/008/415/569/large/bach-do-rwby-white-rose-christmas-by-dishwasher1910-daqztp3.jpg?1512608214'),
                ('asdf4.png','https://cdna.artstation.com/p/assets/images/images/008/221/838/large/bach-do-rwby-holidays-2016-by-dishwasher1910-dapt9lm.jpg?1511286887'),]
    download(url_list)



