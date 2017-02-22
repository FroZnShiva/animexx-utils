import requests

Host = 'ssl.animexx.de'
CertificateFile = './certificates/*.animexx.de'

def bake_cookies(sessionId, autologin):
	cookies = requests.cookies.RequestsCookieJar()
	cookies.set('force_https', '1', domain = Host, path = '/')
	cookies.set('PHPSESSID', sessionId, domain = Host, path = '/')
	cookies.set('autologin', autologin, domain = Host, path = '/')
	return cookies
