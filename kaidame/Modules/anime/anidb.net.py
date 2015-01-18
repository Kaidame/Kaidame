#anidb.net Module
#pulls data from anidb and stores it in the local database for the anime series added.
#AUTHOR dorbian
#TODO make it work :)
#---

REQUIRES = "showtitle"
SUPPLIES = "extended"
DATADUMP = True
DATADUMPLINK = "http://anidb.net/api/anime-titles.xml.gz"
DATADUMPLIMIT = "24H"

import kaidame.Lib.requests

