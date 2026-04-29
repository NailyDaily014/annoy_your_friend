# test_myspar.py
import requests
import re

PHONE = "79374903539"

s = requests.Session()

print("[1] GET myspar.ru/catalog/pitstsa-4/ ...")
resp = s.get(
    'https://myspar.ru/catalog/pitstsa-4/',
    headers={
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:140.0) Gecko/20100101 Firefox/140.0',
        'Accept': 'text/html',
    }
)
print(f"   Status: {resp.status_code}")
print(f"   PHPSESSID: {s.cookies.get('PHPSESSID')}")

match = re.search(r"'bitrix_sessid'\s*:\s*'([^']+)'", resp.text)
if not match:
    print("   ❌ sessid не найден!")
    exit()

sessid = match.group(1)
print(f"   bitrix_sessid: {sessid}")

print("\n[2] POST отправка SMS (с теми же куками)...")
resp_sms = s.post(
    'https://myspar.ru/local/ajax/user/auth/',
    headers={
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:140.0) Gecko/20100101 Firefox/140.0',
        'Accept': 'text/plain, */*; q=0.01',
        'X-Requested-With': 'XMLHttpRequest',
        'Content-Type': 'multipart/form-data; boundary=----geckoformboundarya6b30b5d30effb5b23a6d108d06f4449',
        'Origin': 'https://myspar.ru',
        'Referer': 'https://myspar.ru/catalog/pitstsa-4/',
    },
    data=f"------geckoformboundarya6b30b5d30effb5b23a6d108d06f4449\r\nContent-Disposition: form-data; name=\"sessid\"\r\n\r\n{sessid}\r\n------geckoformboundarya6b30b5d30effb5b23a6d108d06f4449\r\nContent-Disposition: form-data; name=\"step\"\r\n\r\n1\r\n------geckoformboundarya6b30b5d30effb5b23a6d108d06f4449\r\nContent-Disposition: form-data; name=\"phone\"\r\n\r\n+7 {PHONE[1:4]} {PHONE[4:7]}\u2013{PHONE[7:9]}\u2013{PHONE[9:11]}\r\n------geckoformboundarya6b30b5d30effb5b23a6d108d06f4449--\r\n",
)
print(f"   Status: {resp_sms.status_code}")
print(f"   Response: {resp_sms.text}")