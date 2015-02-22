from BeautifulSoup import BeautifulSoup
from subprocess import call
import urllib2


html_page = urllib2.urlopen('http://www.pokemondb.net/pokedex/all')
soup = BeautifulSoup(html_page)
for link in soup.findAll('a'):
    if 'pokedex' in link.get('href'):
	# soup.findAll('iframe', attrs={'src': re.compile("^http://")})
        print(link.get('href'))