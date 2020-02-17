import requests

url = "https://stepic.org/media/attachments/course67/3.6.3/"
r = requests.get("https://stepic.org/media/attachments/course67/3.6.3/699991.txt")
s = r.text
while ('We' not in s):
    r = requests.get(url + s)
    s = r.text
    print(s)