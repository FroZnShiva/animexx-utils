import requests
import ssl

from requests.adapters import HTTPAdapter
from requests.packages.urllib3.poolmanager import PoolManager

Host = 'ssl.animexx.de'
CertificateFile = './certificates/*.animexx.de'

class HttpsAdapter(HTTPAdapter):
	def init_poolmanager(self, connections, maxsize, block=False):
		self.poolmanager = PoolManager(
			num_pools = connections,
			maxsize = maxsize,
			block = block,
			ssl_version = ssl.PROTOCOL_TLSv1_2,
		)

def new_session():
	session = requests.Session()
	session.mount('https://', HttpsAdapter())
	return session

def fetch(url, cookies):
	session = new_session()
	response = session.get(url, cookies = cookies, verify = CertificateFile)
	return response

def bake_cookies(sessionId, autologin):
	cookies = requests.cookies.RequestsCookieJar()
	cookies.set('force_https', '1', domain = Host, path = '/')
	cookies.set('PHPSESSID', sessionId, domain = Host, path = '/')
	cookies.set('autologin', autologin, domain = Host, path = '/')
	return cookies
