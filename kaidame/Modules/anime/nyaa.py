__author__ = 'Dorbian'
from kaidame.Lib.bs4 import BeautifulSoup
import kaidame.Lib.requests as requests
import kaidame
from json import JSONEncoder

class SiteLoader():

    def __init__(self):
        self.url = "http://nyaa.se/"
        self.searchpage = "?page=search"
        self.cat = "&cats="
        self.animecat = "1"
        self.query = "&term="
        self.filter = "&filter="
        self.nextpage = "&offset="

    def searchsite(self, squery, stype):
        if stype == "Anime":
            lcat = self.animecat

        r = requests.get("{0}{1}{2}{3}{4}0&{5}{6}".format(
            self.url, self.searchpage, self.cat, lcat, self.filter, self.query, squery))

        data = r.text

        soup = BeautifulSoup(data)

        trow = soup.find_all('tr', class_="trusted tlistrow")
        for row in trow:
            cells = row.find_all("td")
            for ttr in row:
                episodeurl = ttr.find(title='download').get_text().encode('utf-8')
            #eppcat = cells.find().get_text().encode('utf-8')
            episode = cells[1].get_text().encode('utf-8')
            episodesize = cells[3].get_text().encode('utf-8')
            seeders = cells[4].get_text().encode('utf-8')
            leechers = cells[5].get_text().encode('utf-8')
            downloads = cells[6].get_text().encode('utf-8')
            dlstr = JSONEncoder().encode({
                {0}
            })
            print('{0}:\nURL:{1}\nSize:{2}\nS{3}\\L{4}\nDownloaded:{5}\n'.format(
                episode, episodeurl, episodesize, seeders, leechers, downloads))

            if int(seeders) < 2:
                LowS = True
            if int(leechers) / 5 < 2:
                LowL = True

            try:
                if LowS is True and LowL is True:
                    print("Not enough data to download\n")
            except:
                pass


