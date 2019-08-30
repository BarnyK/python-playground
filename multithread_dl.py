import requests
import multiprocessing
import time

session = None


def set_global_session():
    global session
    if not session:
        session = requests.Session()


def download_file(file):
    with session.get(file[1]) as response:
        with open(file[0],'wb+') as f:
        	f.write(response.content)


def download(files):
    with multiprocessing.Pool(initializer=set_global_session) as pool:
        pool.map(download_file, files)


if __name__ == "__main__":
    url_list = [('asdf1.png','https://cdnb.artstation.com/p/assets/images/images/008/415/569/large/bach-do-rwby-white-rose-christmas-by-dishwasher1910-daqztp3.jpg?1512608214'),
                ('asdf2.png','https://cdna.artstation.com/p/assets/images/images/008/221/838/large/bach-do-rwby-holidays-2016-by-dishwasher1910-dapt9lm.jpg?1511286887'),]
    download(url_list)