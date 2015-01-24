import kaidame
#from kaidame import *
#from kaidame.Core import *

if __name__ == '__main__':
    #processing = Proc()

    #Threader.Thread(1, 'init', initialize())
    #processing.start(initialize(), 'lock', 'init')
    #initialize()

    #cmd = kaidame.Core.Processing.CommandServer()
    #cmd.start()

    init = kaidame.initialize()
    if init == True:
        kaidame.log("Booting webserver", "INFO")
        #Boot the webserver
        import kaidame.Core.Webserver as webStart
        webStart.initialize()

        #import kaidame.Modules.Anime.nyaa as nyaa
        #parsert = nyaa.SiteLoader()
        #parsert.searchsite("Durarara", "Anime")

        import kaidame.Modules.Anime.anidb as anidb
        anidb.check_valid()
        #anidb.getdata()
        #anidb.extract()
        #anidb.list_import()

