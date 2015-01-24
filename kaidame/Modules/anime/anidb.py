#anidb.net Module
#pulls data from anidb and stores it in the local database for the anime series added.
#AUTHOR dorbian
#TODO make it work :)
#---

import urllib
import kaidame
import os
import gzip
import kaidame.Core.Database as DB
import sys
import datetime
from bs4 import BeautifulSoup

REQUIRES = "showtitle"
SUPPLIES = "extended"
DATADUMP = True
DATADUMPLINK = "http://anidb.net/api/anime-titles.xml.gz"
DATASOURCE = os.path.join(kaidame.cachedir, "anime-titles.xml.gz")
DATADESTINATION = os.path.join(kaidame.cachedir, "anime-titles.xml")
DATADUMPLIMIT = "24H"
DOWNLOAD = "NO" #(NZB, TORRENT)

# # query from a class
# session.query(User).filter_by(name='ed').all()
#
# # query with multiple classes, returns tuples
# session.query(User, Address).join('addresses').filter_by(name='ed').all()
#
# # query using orm-enabled descriptors
# session.query(User.name, User.fullname).all()


def getdata():
    testfile = urllib.URLopener()
    testfile.retrieve(DATADUMPLINK, DATASOURCE)
    kaidame.log("Downloading anidb Database to {0}".format(DATASOURCE), "INFO")
    timeout = DB.Options(anidbsync=datetime.datetime.utcnow())
    session = DB.Session()
    session.add(timeout)
    session.commit()


def extract():
    inF = gzip.open(DATASOURCE, 'rb')
    kaidame.log("extracting {0}".format(DATASOURCE), "INFO")
    outF = open(DATADESTINATION, 'wb')
    outF.write(inF.read())
    inF.close()
    outF.close()

#ed_user = User(name='ed', fullname='Ed Jones', password='edspassword')

    #X main = Column(String)
    # mainshort = Column(String)
    # title = Column(String)
    # titleshort = Column(String)
    #X officialen = Column(String)
    #X officialjp = Column(String)
    # imdbid = Column(String)
    # tvrageid = Column(String)
    #X anidbid = Column(String)
    # malid = Column(String)
    # wikilink = Column(String)

    #AnimeTitles(anidbid=AnimeID, main=maintitle,

def list_import():
    handler = open(DATADESTINATION).read()
    soup = BeautifulSoup(handler)

    for anime in soup.findAll('anime'):
        dblink = 'anidb={0}'.format(anime['aid'])
        title_attrs = dict(anime.attrs)
        anidbid = title_attrs['aid']
        f_anime = anime.findAll('title')

        for title in anime.findAll('title'):
            # print title
            #f_anime_dict = dict(title.attrs)
            #print f_anime_dict
            # print title.attrs['type']
            # print title.attrs['xml:lang']
            # print title.get_text()
            # print anidbid
            # print '-------'

            if title.attrs['type'] == 'main':
                mainlang = title.attrs['xml:lang']
                maintitle = title.get_text()
            elif title.attrs['type'] == 'official' and title.attrs['xml:lang'] == 'ja':
                officialjp = title.get_text()
            elif title.attrs['type'] == 'official' and title.attrs['xml:lang'] == 'en':
                officialen = title.get_text()

        # if not officialjp in locals():
        #     officialjp = ''
        #
        # if not officialen in locals():
        #     officialen = ''
        #
        # if not maintitle in locals():
        #     maintitle = ''

        print u'ID:{0}\nMain:{1}\nJP:{2}\nEN:{3}'.format(anidbid, maintitle, officialjp, officialen)