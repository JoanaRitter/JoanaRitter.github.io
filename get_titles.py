import urllib.request
import re
import ssl

urls = [
    "https://www.youtube.com/watch?v=O9uXr5s8-CY",
    "https://www.alura.com.br/podcast/hackathons-nasa-e-manchas-de-oleo-hipsters-ponto-tech-178-a387",
    "https://www.youtube.com/watch?v=G8ludLzmGiw",
    "https://www.youtube.com/watch?v=xa5E-uP7Sw4",
    "https://www.youtube.com/watch?v=4LhWp0XlSyQ",
    "https://www.youtube.com/watch?v=lxMKqV5oh7M"
]

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

for url in urls:
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        html = urllib.request.urlopen(req, context=ctx).read().decode('utf-8')
        title = re.search(r'<title.*?>(.*?)</title>', html, re.IGNORECASE | re.DOTALL)
        if title:
            print(f"{url} -> {title.group(1).strip()}")
        else:
            print(f"{url} -> No title found")
    except Exception as e:
        print(f"{url} -> Error: {e}")
