import requests
from services import urls
PHONE = "79374903539"#Example 79222222222
for i in range(1):
    url_list = urls(PHONE)
    for service in url_list:
        try:
            body = service.get('json') or service.get('data')
            response = requests.request(
                method=service.get('method'),
                url=service['url'],
                headers=service.get('headers'),
                cookies=service.get('cookies'),
                data=body if 'data' in service and not 'json' in service else None,
                json=body if 'json' in service else None,
                timeout=5
            )
            print(response.status_code)
            print(response.text)
            if len(response.text)<200:
                print(response.text)
        except:
            print("Error")