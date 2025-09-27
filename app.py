import requests
import sys

# Kullanım: python app.py urls.txt
with open(sys.argv[1], "r", encoding="utf-8") as f:
    urls = f.read().splitlines()

for url in urls:
    try:
        r = requests.get(url, timeout=5)
        print(f"{url} → {r.status_code}")
    except Exception as e:
        print(f"{url} → Hata: {e}")
