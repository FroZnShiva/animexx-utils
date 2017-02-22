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

def new_session(sessionId, autologin):
	session = requests.Session()
	session.mount('https://', HttpsAdapter())
	session.cookies.set('force_https', '1', domain = Host, path = '/')
	session.cookies.set('PHPSESSID', sessionId, domain = Host, path = '/')
	session.cookies.set('autologin', autologin, domain = Host, path = '/')
	return session

def fetch(url, sessionId = None, autologin = None, session = None):
	if not session:
		assert(sessionId is not None and autologin is not None)
		session = new_session(sessionId, autologin)
	response = session.get(url, verify = CertificateFile)
	return response
