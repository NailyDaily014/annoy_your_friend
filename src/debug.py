import re
import secrets
import requests
import session_storage
from fake_useragent import UserAgent
ua = UserAgent()
def urls(number):
    return [
# {
#     "info": {"type": "sms"},
#     "method": "post",
#     "url": "https://api.cian.ru/validation-codes/v1/send-code/",
#     "headers": { 'User-Agent': ua.random, 'Accept': '*/*', 'Accept-Language': 'en-US,en;q=0.5', 'Content-Type': 'application/json', 'Origin': 'https://surgut.cian.ru', 'Referer': 'https://surgut.cian.ru/', 'Sec-Fetch-Dest': 'empty','l-Site': 'same-site', },
#     "cookies": { '_CIAN_GK': '5dbd8832-1213-42e8-b451-900c101a2f10', 'sopr_session': '979627d016fd4683', 'cookie_agreement_accepted': '1', },
#     "json": { 'phone': f'+{number}', 'type': 'authenticateCode', },
# }

    ]