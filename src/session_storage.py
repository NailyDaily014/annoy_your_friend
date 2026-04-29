import requests
import re
from fake_useragent import UserAgent

class SessionManager:
    def __init__(self):
        self.ua = UserAgent()
        self._sessions = {}
    
    def get_myspar(self):
        if 'myspar' not in self._sessions:
            s = requests.Session()
            r = s.get(
                'https://myspar.ru/catalog/pitstsa-4/',
                headers={'User-Agent': self.ua.random, 'Accept': 'text/html'}
            )
            self._sessions['myspar'] = {
                'cookies': dict(s.cookies),
                'sessid': re.search(r"'bitrix_sessid'\s*:\s*'([^']+)'", r.text).group(1)
            }
        return self._sessions['myspar']
session_manager = SessionManager()