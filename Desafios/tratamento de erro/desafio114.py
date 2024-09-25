import urllib
import urllib.error
import urllib.request

try:
    site = urllib.request.urlopen('https://www.pudim.com.br/')
except urllib.error.URLError:
    print('Deu errado')
else:
    print('Tudo OK')