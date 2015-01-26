__author__ = 'Dorbian'
import os
import sys
import kaidame
import cherrypy

from Webconfig import WebInterface


def initialize():

    cherrypy.config.update({
        'log.screen': True,
        'server.thread_pool': 10,
        'server.socket_port': kaidame.server_port,
        'server.socket_host': kaidame.server_host,
        'engine.autoreload.on': False,
    })

    conf = {
        '/': {
            'tools.staticdir.root': os.path.join(kaidame.rundir, os.path.join("kaidame", "Webdata"))
        },
        '/interfaces': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': "interfaces"
        },
        '/images': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': "images"
        },
        '/css': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': "css"
        },
        '/js': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': "js"
        },
        '/favicon.ico': {
            'tools.staticfile.on': True,
            'tools.staticfile.filename': "images/favicon.ico"
        }
    }

    if kaidame.server_pass != "":
        conf['/'].update({
            'tools.auth_basic.on': True,
            'tools.auth_basic.realm': 'Kaidame',
            'tools.auth_basic.checkpassword': cherrypy.lib.auth_basic.checkpassword_dict(
                {kaidame.server_user: kaidame.server_pass})
        })

    # Prevent time-outs
    cherrypy.engine.timeout_monitor.unsubscribe()
    cherrypy.tree.mount(WebInterface(), kaidame.server_root, config=conf)

    cherrypy.engine.autoreload.on = True

    try:
        cherrypy.process.servers.check_port(kaidame.server_host, kaidame.server_port)
        cherrypy.server.start()
    except IOError:
        print 'Failed to start on port: {0}. Is something else running?'.format(kaidame.server_port)
        sys.exit(0)
    #cherrypy.server.wait()
