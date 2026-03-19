import requests
from pprint import pprint
PHONE = "79374903539"
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
        print("serv1")
def serv2():
    try:
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
    except:
        print("serv2")
def serv3():
    try:
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
    except:
        print("serv3")
def serv4():
    try:
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
    except:
        print("serv4")
def serv5():
    try:
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
    except:
        print("serv5")
def serv6():
    try:
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
    except:
        print("serv6")
def serv7():
    try:
        cookies = {
        '_GPSLSC': 'Qr8wCGAZr1!3N5KWYuEGf!vp531Cn8Kr!L0_pR2dQbZ!lS8zMAdnCG!Qr0yfDXPyx!uh8fSmytpE!mwFhmvD-YP!f9prmllK9_!RDsctNFT8b',
        'PHPSESSID': 'j9cHjQnauakoNQQBmSWoGjgHDPUMFbaQ',
        'BITRIX_SM_TZ': 'Asia/Yekaterinburg',
        'sbjs_migrations': '1418474375998%3D1',
        'sbjs_current_add': 'fd%3D2026-03-19%2019%3A04%3A48%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.pizzaldo.ru%2Fcatalog%2Fpizza%2F%3Fysclid%3Dmmxjkqz4o5327456236%7C%7C%7Crf%3Dhttps%3A%2F%2Fyandex.ru%2F',
        'sbjs_first_add': 'fd%3D2026-03-19%2019%3A04%3A48%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.pizzaldo.ru%2Fcatalog%2Fpizza%2F%3Fysclid%3Dmmxjkqz4o5327456236%7C%7C%7Crf%3Dhttps%3A%2F%2Fyandex.ru%2F',
        'sbjs_current': 'typ%3Dreferral%7C%7C%7Csrc%3Dyandex.ru%7C%7C%7Cmdm%3Dreferral%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%2F%7C%7C%7Ctrm%3D%28none%29',
        'sbjs_first': 'typ%3Dreferral%7C%7C%7Csrc%3Dyandex.ru%7C%7C%7Cmdm%3Dreferral%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%2F%7C%7C%7Ctrm%3D%28none%29',
        'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F146.0.0.0%20Safari%2F537.36%20Edg%2F146.0.0.0',
        'sbjs_session': 'pgs%3D1%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.pizzaldo.ru%2Fcatalog%2Fpizza%2F%3Fysclid%3Dmmxjkqz4o5327456236',
        't_source': 'referral%7Cyandex.ru',
        '_ga': 'GA1.2.80662755.1773929089',
        '_gid': 'GA1.2.1299857072.1773929089',
        '_gat': '1',
        '_dc_gtm_test': '1',
        '_ym_uid': '1773929089882178216',
        '_ym_d': '1773929089',
        '_ym_isad': '2',
        '_ym_visorc': 'w',
        '_ga_LTKVQQPHG2': 'GS2.2.s1773929089$o1$g0$t1773929089$j60$l0$h0',
        }

        headers = {
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-language': 'ru,en;q=0.9,en-GB;q=0.8,en-US;q=0.7',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': 'https://www.pizzaldo.ru',
            'priority': 'u=1, i',
            'referer': 'https://www.pizzaldo.ru/catalog/pizza/?ysclid=mmxjkqz4o5327456236',
            'sec-ch-ua': '"Chromium";v="146", "Not-A.Brand";v="24", "Microsoft Edge";v="146"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0',
            'x-requested-with': 'XMLHttpRequest',
            # 'cookie': '_GPSLSC=Qr8wCGAZr1!3N5KWYuEGf!vp531Cn8Kr!L0_pR2dQbZ!lS8zMAdnCG!Qr0yfDXPyx!uh8fSmytpE!mwFhmvD-YP!f9prmllK9_!RDsctNFT8b; PHPSESSID=j9cHjQnauakoNQQBmSWoGjgHDPUMFbaQ; BITRIX_SM_TZ=Asia/Yekaterinburg; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2026-03-19%2019%3A04%3A48%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.pizzaldo.ru%2Fcatalog%2Fpizza%2F%3Fysclid%3Dmmxjkqz4o5327456236%7C%7C%7Crf%3Dhttps%3A%2F%2Fyandex.ru%2F; sbjs_first_add=fd%3D2026-03-19%2019%3A04%3A48%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.pizzaldo.ru%2Fcatalog%2Fpizza%2F%3Fysclid%3Dmmxjkqz4o5327456236%7C%7C%7Crf%3Dhttps%3A%2F%2Fyandex.ru%2F; sbjs_current=typ%3Dreferral%7C%7C%7Csrc%3Dyandex.ru%7C%7C%7Cmdm%3Dreferral%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%2F%7C%7C%7Ctrm%3D%28none%29; sbjs_first=typ%3Dreferral%7C%7C%7Csrc%3Dyandex.ru%7C%7C%7Cmdm%3Dreferral%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%2F%7C%7C%7Ctrm%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F146.0.0.0%20Safari%2F537.36%20Edg%2F146.0.0.0; sbjs_session=pgs%3D1%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.pizzaldo.ru%2Fcatalog%2Fpizza%2F%3Fysclid%3Dmmxjkqz4o5327456236; t_source=referral%7Cyandex.ru; _ga=GA1.2.80662755.1773929089; _gid=GA1.2.1299857072.1773929089; _gat=1; _dc_gtm_test=1; _ym_uid=1773929089882178216; _ym_d=1773929089; _ym_isad=2; _ym_visorc=w; _ga_LTKVQQPHG2=GS2.2.s1773929089$o1$g0$t1773929089$j60$l0$h0',
        }

        params = {
            'action': 'auth',
        }
        data = {
            'CSRF': '',
            'ACTION': 'REGISTER',
            'MODE': 'PHONE',
            'PHONE': f"+{PHONE[0]} {PHONE[1:4]} {PHONE[4:7]} {PHONE[7:9]} {PHONE[9:11]}",
            'PASSWORD': 'qwerty',
            'PASSWORD2': 'qwerty',
        }

        response = requests.post('https://www.pizzaldo.ru/catalog/pizza/', params=params, cookies=cookies, headers=headers, data=data)
        print(response.json())
    except:
        print("serv7")
#serv1()
#serv2()
#serv3()
#serv4()
#serv5()
#serv6()
#serv7()