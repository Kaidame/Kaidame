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
        import kaidame.Core.Webserver as webStart
        webStart.initialize({
            'http_port': kaidame.server_port,
            'http_host': kaidame.server_host,
            'http_root': kaidame.server_root,
            'http_user': kaidame.server_user,
            'http_pass': kaidame.server_pass,
        })



