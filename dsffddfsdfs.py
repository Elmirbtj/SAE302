import time
import concurrent.futures
import requests



img_urls = ['https://thumbs.dreamstime.com/b/sed-lumineux-du-soleil-avec-le-jpg-jaune-de-la-lumi%C3%A8re-169481284.jpg']

def download_image(img_url):   # pool de threads
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[len(img_url.split('/'))-1]
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print(f"{img_name} was downloaded")
start = time.perf_counter()
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(download_image, img_urls)
    end = time.perf_counter()
print(f"Tasks ended in {round(end - start, 2)} second(s)")