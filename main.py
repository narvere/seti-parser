import requests, lxml, json, random
from time import sleep
# from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"
}

url = "https://magazin.seti.ee/modules/Board/index.php?pa=viewannonces&lid=1893157"

# n = 500
# for i in range(n):
#     req = requests.get(url, headers)
#     print(f"Попытка нр {i}")
#     sleep(random.randrange(2, 4))


# src = req.text
# print(src)
# with open(f"data/index.html", "w") as file:
#     file.write(req.text)

# with open(f"data/index.html") as file:
#     src = file.read()
# soup = BeautifulSoup(src, "lxml")
#
# tbody_all = soup.find( class_="bg2").text
# print(tbody_all)
n = 0
respond = "<Response [200]>"
while True:
    shit = f"https://magazin.seti.ee/modules/Board/index.php?pa=view&cid=32&class=&ord=&debut={n}"
    respond = requests.get(shit, headers)
    print(respond)
    print(shit)
    print(n)
    n += 50
    sleep(random.randrange(2, 4))
    # sleep(random.randrange(2, 4))
    # if respond:
    #     print("True")