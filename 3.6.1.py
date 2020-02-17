import requests

r = requests.get("https://stepic.org/media/attachments/course67/3.6.2/008.txt")
print(r.text)
n = r.text.count('\n')
print(n)